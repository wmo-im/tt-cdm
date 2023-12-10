import csv
from datetime import datetime as dt
import json
import pandas as pd
import re




# a few utility functions
# Define a regular expression pattern to match angle brackets and http/https
pattern = re.compile(r'<http[s]?(://[^>]*)>')
# define function to fix id column (removing brackets and change of http to https)
def fix_ids(match):
    return "https" + match.group(1)

# function to create links object
def make_canonical(url_):
    links = [
        {
            "type": "text/html",
            "rel": "canonical",
            "href": url_
        }
    ]
    return json.dumps(links)


description_pattern = re.compile(r"^'(.*)'@en$")
def fix_description(match):
    return match.group(1)

tables = {
    "altitude": "AltitudeOrDepth",
    "application_area": "ApplicationArea",
    "climate_zone": "ClimateZone",
    "communication_method": "DataCommunicationMethod",
    # "equipment_type": "EquipmentType",  # not in WMDR
    "exposure": "Exposure",
    "facility_type": "FacilityType",
    # "feature_type": "FeatureType",  # not in WMDR
    "geopositioning_method": "GeopositioningMethod",
    "local_topography": "LocalTopography",  # download link broken in codes.wmo.int
    # "measurement_quality": "MeasurementQuality",  # not in WMDR
    # "media_type": "MediaType",  # not in WMDR
    # "observation_type": "ObservationType",  # not in WMDR
    # "observed_property": "ObservedProperty",  # use different vocab.
    "observing_method": "ObservingMethodAtmosphere",
    # "observing_procedure": "ObservingProcedure", # not a code table in WMDR
    "observing_program": "ProgramAffiliation",
    "operating_status": "InstrumentOperatingStatus",
    "reference_surface": "ReferenceSurfaceType",
    "relative_elevation": "RelativeElevation",  # download link broken in WMDR
    "representativeness": "Representativeness",
    "reporting_status": "ReportingStatus", # to add
    # "role": "Role",  # not in WMDR
    "source_of_observation": "SourceOfObservation", # to add
    # "source_type": "SourceType",  # not in WMDR
    # "status": "Status",  # not in WMDR
    "surface_cover": "SurfaceCoverGlob2009", # multiple
    "surface_roughness": "SurfaceRoughnessDavenport",
    "territory": "TerritoryName",
    "time_zone": "Timezone",
    "topographic_context": "TopographicContext", # to add
    "wmo_region": "WMORegion"
}


for table, inScheme in tables.items():
    # this needs to be here, it is updated later
    column_order = ["id", "inScheme", "name", "description", "links",
                    "_version", "_change_date", "_user", "_status",
                    "_comments"]
    # Download code list using pandas
    inScheme = f"https://codes.wmo.int/wmdr/{inScheme}"
    print(f"{inScheme}?_format=csv")
    code_list = pd.read_csv(f"{inScheme}?_format=csv")


    # constants / values not from codes.wmo.int
    user = "x-opencdms:admin:user:1"
    change_date = dt.now().isoformat()
    comments = "First automated ingest from codes.wmo.int. Data download on _change_date."
    version = 1
    status = "x-opencdms:reference_data:status:1"

    # apply fixes
    code_list['@id'] = code_list['@id'].apply(lambda x: pattern.sub(fix_ids,x))
    code_list['dct:description'] = code_list['dct:description'].apply(
        lambda x: description_pattern.sub(fix_description,x))
    code_list['rdfs:label'] = code_list['rdfs:label'].apply(
        lambda x: x.replace("'",""))
    code_list = code_list.assign(
        links = code_list['@id'].apply(lambda x: make_canonical(x)),
        inScheme = [inScheme] * code_list.shape[0],
        _version = [version] * code_list.shape[0],
        _change_date = [change_date] * code_list.shape[0],
        _user = [user] * code_list.shape[0],
        _status = [status] * code_list.shape[0],
        _comments = [comments] * code_list.shape[0]
    )

    if table == "territory":  # add ISO3c
        code_list = code_list.assign(
            ISO3c = code_list['skos:notation'],
            wmo_region = ['']*code_list.shape[0]
        )
        column_order = ["id", "inScheme", "name", "description",
                        "ISO3c", "wmo_region", "links",
                        "_version", "_change_date", "_user", "_status",
                        "_comments"]

    if table == "time_zone":  # add offset
        code_list = code_list.assign(
            offset = code_list['skos:notation'].apply(
                lambda x: float(x.replace("'","")))
        )
        column_order = ["id", "inScheme", "name", "description", "offset",
                        "links", "_version", "_change_date", "_user",
                        "_status", "_comments"]

    # drop unwanted columns
    code_list.drop(labels=["rdf:type","skos:notation"],axis=1, inplace=True)

    # rename other columns
    mapper = {
        "@id": "id",
        "dct:description": "description",
        "rdfs:label": "name"
    }


    # rename the columns
    code_list.rename(columns=mapper, inplace=True)
    code_list = code_list[column_order]

    # now save
    code_list.to_csv(f"./opencdms/test_data/{table}.csv", sep=",", na_rep="",
                     index=False, quoting = csv.QUOTE_NONNUMERIC,
                     quotechar = "'")
    #code_list.to_json(f"{table}.json")
