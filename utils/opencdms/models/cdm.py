# =============================================================================
# MIT License
#
# Copyright (c) 2023, OpenCDMS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================
from abc import ABC as AbstractBase
from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

Geography = NewType("Geography", str)

class DomainModelBase(AbstractBase):
    """
    Base class for OpenCDMS domain models.
    """

    def table_info(self) -> str:
        """Return table comment"""
        return self._comment

    def column_info(self, column: str) -> str:
        """Return column information"""
        return self._comments.get(column)


@dataclass
class ObservationType(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for observation type",
        "description": "Description of observation type",
        "links": "Link(s) to definition of observation type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class FacilityType(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "WMDS facility type, type of observing facility"


@dataclass
class FeatureType(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class WmoRegion(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Territory(DomainModelBase):
    id: int
    ISO3c: str
    name: str
    description: str
    wmo_region_id_id: Optional[int]
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "ISO3c": "ID / primary key",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "wmo_region_id_id": "WMO region that represents the territory",
        "links": "Link(s) to definition of feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObservedProperty(DomainModelBase):
    id: int
    short_name: str
    standard_name: Optional[str]
    units: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "short_name": "Short name representation of observed property, e.g. 'at'",
        "standard_name": "CF standard name (if applicable), e.g. 'air_temperature'",
        "units": "Canonical units, e.g. 'Kelvin'",
        "description": "Description of observed property",
        "links": "Link(s) to definition / source of observed property",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class ObservingProcedure(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of observing procedure",
        "description": "Description of observing procedure",
        "links": "Link(s) to further information",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Status(DomainModelBase):
    id: int
    name: str
    description: str
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for status",
        "description": "Description of the status",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class TimeZone(DomainModelBase):
    id: int
    abbreviation: str
    name: str
    offset: float
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "abbreviation": "Abbreviation for time zone",
        "name": "Name / description of timezone",
        "offset": "Offset from UTC (hours)",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class SourceType(DomainModelBase):
    id: str
    name: str
    description: str
    scheme: Optional[str]
    links: Optional[str]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of source type",
        "description": "Description of source type, e.g. file etc",
        "scheme": "IANA scheme (if applicable)",
        "links": "Links proviing further definition of source type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class User(DomainModelBase):
    id: str
    name: str
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of user/agent",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Media(DomainModelBase):
    id: Optional[str]
    media_type_id_id: Optional[int]
    description: Optional[str]
    created: Optional[datetime]
    creator: Optional[str]
    rights: Optional[int]
    source: Optional[str]
    data: Optional[blob]
    _comments = {
        "id": "",
        "media_type_id_id": "",
        "description": "",
        "created": "",
        "creator": "",
        "rights": "",
        "source": "",
        "data": ""
    }
    _comment = "store for digital media, e.g. photos, reports, videos, etc"


@dataclass
class MediaType(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Type of media uploaded"
    }
    _comment = "placeholder"


@dataclass
class Host(DomainModelBase):
    id: str
    name: str
    description: Optional[str]
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
    wigos_station_identifier: Optional[str]
    facility_type_id_id: Optional[str]
    date_established: Optional[datetime]
    date_closed: Optional[datetime]
    wmo_region_id_id: Optional[int]
    territory_id_id: Optional[int]
    time_zone_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Preferred name of host",
        "description": "Description of host",
        "links": "URI to host, e.g. to OSCAR/Surface",
        "location": "Location of station",
        "elevation": "Elevation of station above mean sea level in meters",
        "wigos_station_identifier": "WIGOS station identifier",
        "facility_type_id_id": "Type of observing facility, fixed land, mobile sea, etc",
        "date_established": "Date host was first established",
        "date_closed": "Date host was first established",
        "wmo_region_id_id": "WMO region in which the host is located",
        "territory_id_id": "Territory the host is located in",
        "time_zone_id_id": "Time zone the host is located in",
        "valid_from": "Date from which the details for this record are valid",
        "valid_to": "Date after which the details for this record are no longer valid",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "wmdr.observing_facility"


@dataclass
class HostEnvironment(DomainModelBase):
    id: str
    host_id: str
    climate_zone_id_id: Optional[int]
    surface_cover_id_id: Optional[int]
    surface_roughness_id_id: Optional[int]
    topography_id_id: Optional[int]
    season_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id": "Host associated with this record",
        "climate_zone_id_id": "Climate zone that the associated host is located in",
        "surface_cover_id_id": "Type of sueface cover",
        "surface_roughness_id_id": "Typical surface roughness of the site surrounding the host",
        "topography_id_id": "Topography of the environment surrounding the host",
        "season_id_id": "Season that is applicable to this record (e.g. all, winter, spring, summer, autumn)",
        "valid_from": "Date the this record is valid from",
        "valid_to": "date that this record is valid to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Description of the environment at the specified host"


@dataclass
class ClimateZone(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class SurfaceCover(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class SurfaceRoughness(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class Topography(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class Season(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class HostAffiliation(DomainModelBase):
    id: str
    host_id_id: str
    programme_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id_id": "Host described by this record",
        "programme_id_id": "Observing programme that this host is affiliated with",
        "valid_from": "Date from which the details for this record are valid",
        "valid_to": "Date after which the details for this record are no longer valid",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Which programs this host is affiliated with"


@dataclass
class Programme(DomainModelBase):
    id: Optional[int]
    name: Optional[str]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": ""
    }
    _comment = "placeholder"


@dataclass
class HostAlias(DomainModelBase):
    id: str
    host_id_id: str
    alternative_id: Optional[str]
    alternative_name: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id_id": "Primary ID by which the host is known",
        "alternative_id": "Alternative ID by which the host is known",
        "alternative_name": "Alternative name by which the host is known",
        "valid_from": "Date the alternative id/name was used from",
        "valid_to": "Date the alternative id/name was used to",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "table to track known aliases for hosts"


@dataclass
class HostResponsibleParty(DomainModelBase):
    id: Optional[int]
    user_id_id: Optional[int]
    description: str
    _comments = {
        "id": "",
        "user_id_id": "",
        "description": "Description of role with this association. Note: this will be changed to a code table"
    }
    _comment = "placeholder"


@dataclass
class HostMedia(DomainModelBase):
    id: str
    host_id_id: Optional[str]
    media_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "host_id_id": "",
        "media_id_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"


@dataclass
class Observer(DomainModelBase):
    id: str
    name: str
    description: str
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
    manufacturer: Optional[str]
    model: Optional[str]
    serial_number: Optional[str]
    firmware_version: Optional[str]
    control_schedule_id_id: Optional[int]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of sensor",
        "description": "Description of sensor",
        "links": "Link(s) to further information",
        "location": "Location of observer",
        "elevation": "Elevation of observer above mean sea level",
        "manufacturer": "Make, or manufacturer, of sensor",
        "model": "Model of sensor",
        "serial_number": "Serial number of sensor",
        "firmware_version": "Firmware version of software installed in sensor",
        "control_schedule_id_id": "Link to information on calibration schedule and details",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "wmdr.equipment"


@dataclass
class ControlSchedule(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of control schedule"
    }
    _comment = "placeholder"


@dataclass
class ObserverCharacteristics(DomainModelBase):
    id: str
    observer_id_id: str
    observed_property_id_id: Optional[int]
    observing_method_id_id: Optional[str]
    measurement_units: Optional[int]
    drift_per_unit_time: Optional[float]
    unit_time: Optional[int]
    valid_min: Optional[float]
    valid_max: Optional[float]
    measurement_uncertainty: Optional[float]
    measurement_accuracy: Optional[float]
    measurement_repeatability: Optional[float]
    measurement_resolution: Optional[float]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "observer_id_id": "The observer to which this record applies",
        "observed_property_id_id": "The observed parameter to which this record applies",
        "observing_method_id_id": "Primary method/principles by which the sensor makes measurements",
        "measurement_units": "The units used in this record",
        "drift_per_unit_time": "Sensor drift per unit time, units specified by measurement units, unit time by unit time",
        "unit_time": "Unit time for drift per unit time (seconds)",
        "valid_min": "Minimum observable value by sensor, in units specificed by measurement units",
        "valid_max": "Maximum observable value by sensor, in units specificed by measurement units",
        "measurement_uncertainty": "Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_accuracy": "Measurement accuracy (trueness) for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_repeatability": "Measurement repeatability (precision) for measurements from this sensor, 2 sigma. Units as per measuremenet units",
        "measurement_resolution": "Minimum change detectable for measurements from this sensor. Units as per measurement units",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Table to record sensor specifications"


@dataclass
class ObservingMethod(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of observing method"
    }
    _comment = "placeholder"


@dataclass
class ObserverResponsibleParty(DomainModelBase):
    id: Optional[int]
    user_id_id: Optional[int]
    description: str
    _comments = {
        "id": "",
        "user_id_id": "",
        "description": "Description of role with this association. Note: this will be changed to a code table"
    }
    _comment = "placeholder"


@dataclass
class ObserverMedia(DomainModelBase):
    id: str
    observer_id_id: Optional[str]
    media_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "observer_id_id": "",
        "media_id_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"


@dataclass
class Collection(DomainModelBase):
    id: str
    name: str
    links: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of collection",
        "links": "Link(s) to further information on collection",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Feature(DomainModelBase):
    id: str
    name: Optional[str]
    description: Optional[str]
    links: Optional[dict]
    feature_type_id_id: int
    geometry: Geography
    elevation: Optional[float]
    parent_id_id: Optional[str]
    properties: Optional[dict]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of feature",
        "description": "Description of feature",
        "links": "Link(s) to further information on feature",
        "feature_type_id_id": "enumerated feature type",
        "geometry": "",
        "elevation": "Meam elevation of feature above mean sea level",
        "parent_id_id": "Parent feature for this feature if nested",
        "properties": "Array of named values consistent with that defined for the feature type",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "table to contain definition of different geographic features"


@dataclass
class Source(DomainModelBase):
    id: str
    name: str
    description: str
    source_type_id_id: int
    links: Optional[dict]
    processor: Optional[str]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of source",
        "description": "Description of source type, e.g. file etc",
        "source_type_id_id": "The type of source",
        "links": "Link(s) to further information on source",
        "processor": "Name of processor used to ingest the data",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "placeholder"


@dataclass
class Observation(DomainModelBase):
    id: str
    location: Geography
    elevation: Optional[float]
    observation_type_id_id: Optional[int]
    phenomenon_start: Optional[datetime]
    phenomenon_end: datetime
    result_value: float
    result_uom: Optional[str]
    result_description: Optional[str]
    result_quality: Optional[dict]
    result_time: Optional[datetime]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    host_id_id: str
    observer_id_id: Optional[str]
    observed_property_id_id: int
    observing_procedure_id_id: Optional[int]
    collection_id_id: Optional[str]
    parameter: Optional[dict]
    feature_id_id: Optional[str]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _source_id_id: int
    _source_identifier: int
    _comments = {
        "id": "ID / primary key",
        "location": "Location of observation",
        "elevation": "Elevation of observation above mean sea level (in meters)",
        "observation_type_id_id": "Type of observation",
        "phenomenon_start": "Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end",
        "phenomenon_end": "End time of the phenomenon being observed or observing period",
        "result_value": "The value of the result in float representation",
        "result_uom": "Units used to represent the value being observed",
        "result_description": "str representation of the result if applicable",
        "result_quality": "JSON representation of the result quality, key / value pairs",
        "result_time": "Time that the result became available",
        "valid_from": "Time that the result starts to be valid",
        "valid_to": "Time after which the result is no longer valid",
        "host_id_id": "Host associated with making the observation, equivalent to OGC OMS 'host'",
        "observer_id_id": "Observer associated with making the observation, equivalent to OGC OMS 'observer'",
        "observed_property_id_id": "The phenomenon, or thing, being observed",
        "observing_procedure_id_id": "Procedure used to make the observation",
        "collection_id_id": "Primary collection or dataset that this observation belongs to. Note: this is different to the OGC OMS collection concept.",
        "parameter": "List of key/ value pairs in dict",
        "feature_id_id": "Feature of interest that this observation is associated with",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc",
        "_source_id_id": "The source of this record",
        "_source_identifier": "The original identifier for the record from the data source"
    }
    _comment = "table to store observations"


@dataclass
class Deployment(DomainModelBase):
    id: str
    host_id_id: Optional[str]
    observer_id_id: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    installation_height: Optional[float]
    reference_surface_id: Optional[int]
    exposure_id: Optional[int]
    configuration: Optional[str]
    maintenance_schedule_id_id: Optional[int]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Unique ID / primary key for deployment",
        "host_id_id": "",
        "observer_id_id": "",
        "valid_from": "",
        "valid_to": "",
        "installation_height": "Installation height above reference surface (in meters)",
        "reference_surface_id": "",
        "exposure_id": "",
        "configuration": "Textual description of sensor installation and configuration",
        "maintenance_schedule_id_id": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Table to track deployments of an observer to a host"


@dataclass
class MaintenanceSchedule(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of maintenance schedule"
    }
    _comment = "placeholder"


@dataclass
class Exposure(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of sensor exposure according to WMO-No. 8"
    }
    _comment = "placeholder"


@dataclass
class ReferenceSurface(DomainModelBase):
    id: Optional[int]
    name: Optional[int]
    description: str
    _comments = {
        "id": "",
        "name": "",
        "description": "Description of reference surface"
    }
    _comment = "placeholder"


@dataclass
class DeploymentMedia(DomainModelBase):
    id: str
    deployment_id_id: Optional[str]
    media_id_id: Optional[int]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    _version: int
    _change_date: datetime
    _user_id_id: int
    _status_id_id: int
    comments: str
    _comments = {
        "id": "Primary key for this record",
        "deployment_id_id": "",
        "media_id_id": "",
        "valid_from": "",
        "valid_to": "",
        "_version": "Version number of this record",
        "_change_date": "Date this record was changed",
        "_user_id_id": "Which user/agent last modified this record",
        "_status_id_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc"
    }
    _comment = "Link table between hosts and media"



