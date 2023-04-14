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
from geoalchemy2 import Geography
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import registry, relationship

from opencdms.models import cdm


mapper_registry = registry()


observation_type = Table(
    "observation_type",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for observation type", index=False),
    Column("description", String, comment="Description of observation type", index=False),
    Column("links", JSONB, comment="Link(s) to definition of observation type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


facility_type = Table(
    "facility_type",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for feature type", index=False),
    Column("description", String, comment="Description of feature type", index=False),
    Column("links", JSONB, comment="Link(s) to definition of feature type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


feature_type = Table(
    "feature_type",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for feature type", index=False),
    Column("description", String, comment="Description of feature type", index=False),
    Column("links", JSONB, comment="Link(s) to definition of feature type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


wmo_region = Table(
    "wmo_region",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for feature type", index=False),
    Column("description", String, comment="Description of feature type", index=False),
    Column("links", JSONB, comment="Link(s) to definition of feature type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


territory = Table(
    "territory",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("ISO3c", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for feature type", index=False),
    Column("description", String, comment="Description of feature type", index=False),
    Column("wmo_region_id_id",ForeignKey("cdm.wmo_region.id"), comment="WMO region that represents the territory", index=False),
    Column("links", JSONB, comment="Link(s) to definition of feature type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


observed_property = Table(
    "observed_property",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("short_name", String, comment="Short name representation of observed property, e.g. 'at'", index=False),
    Column("standard_name", String, comment="CF standard name (if applicable), e.g. 'air_temperature'", index=False),
    Column("units", String, comment="Canonical units, e.g. 'Kelvin'", index=False),
    Column("description", String, comment="Description of observed property", index=False),
    Column("links", JSONB, comment="Link(s) to definition / source of observed property", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


observing_procedure = Table(
    "observing_procedure",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of observing procedure", index=False),
    Column("description", String, comment="Description of observing procedure", index=False),
    Column("links", JSONB, comment="Link(s) to further information", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


status = Table(
    "status",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Short name for status", index=False),
    Column("description", String, comment="Description of the status", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


time_zone = Table(
    "time_zone",
    mapper_registry.metadata,
    Column("id", Integer, comment="ID / primary key", primary_key=True, index=False),
    Column("abbreviation", String, comment="Abbreviation for time zone", index=False),
    Column("name", String, comment="Name / description of timezone", index=False),
    Column("offset", Numeric, comment="Offset from UTC (hours)", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


source_type = Table(
    "source_type",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of source type", index=False),
    Column("description", String, comment="Description of source type, e.g. file etc", index=False),
    Column("scheme", String, comment="IANA scheme (if applicable)", index=False),
    Column("links", String, comment="Links proviing further definition of source type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


user = Table(
    "user",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of user/agent", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


media = Table(
    "media",
    mapper_registry.metadata,
    Column("id", String, comment="", primary_key=True, index=False),
    Column("media_type_id_id",ForeignKey("cdm.media_type.id"), comment="", index=False),
    Column("description", String, comment="", index=False),
    Column("created", DateTime(timezone=True), comment="", index=False),
    Column("creator", String, comment="", index=False),
    Column("rights", Integer, comment="", index=False),
    Column("source", String, comment="", index=False),
    Column("data", blob, comment="", index=False),
    schema="cdm"
)


media_type = Table(
    "media_type",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Type of media uploaded", index=False),
    schema="cdm"
)


host = Table(
    "host",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Preferred name of host", index=False),
    Column("description", String, comment="Description of host", index=False),
    Column("links", JSONB, comment="URI to host, e.g. to OSCAR/Surface", index=False),
    Column("location", Geography, comment="Location of station", index=False),
    Column("elevation", Numeric, comment="Elevation of station above mean sea level in meters", index=False),
    Column("wigos_station_identifier", String, comment="WIGOS station identifier", index=False),
    Column("facility_type_id_id",ForeignKey("cdm.facility_type.id"), comment="Type of observing facility, fixed land, mobile sea, etc", index=False),
    Column("date_established", DateTime(timezone=True), comment="Date host was first established", index=False),
    Column("date_closed", DateTime(timezone=True), comment="Date host was first established", index=False),
    Column("wmo_region_id_id",ForeignKey("cdm.wmo_region.id"), comment="WMO region in which the host is located", index=False),
    Column("territory_id_id",ForeignKey("cdm.territory.id"), comment="Territory the host is located in", index=False),
    Column("time_zone_id_id",ForeignKey("cdm.time_zone.id"), comment="Time zone the host is located in", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


host_environment = Table(
    "host_environment",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("host_id", String, comment="Host associated with this record", index=False),
    Column("climate_zone_id_id",ForeignKey("cdm.climate_zone.id"), comment="Climate zone that the associated host is located in", index=False),
    Column("surface_cover_id_id",ForeignKey("cdm.surface_cover.id"), comment="Type of sueface cover", index=False),
    Column("surface_roughness_id_id",ForeignKey("cdm.surface_roughness.id"), comment="Typical surface roughness of the site surrounding the host", index=False),
    Column("topography_id_id",ForeignKey("cdm.topography.id"), comment="Topography of the environment surrounding the host", index=False),
    Column("season_id_id",ForeignKey("cdm.season.id"), comment="Season that is applicable to this record (e.g. all, winter, spring, summer, autumn)", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date the this record is valid from", index=False),
    Column("valid_to", DateTime(timezone=True), comment="date that this record is valid to", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


climate_zone = Table(
    "climate_zone",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


surface_cover = Table(
    "surface_cover",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


surface_roughness = Table(
    "surface_roughness",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


topography = Table(
    "topography",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


season = Table(
    "season",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


host_affiliation = Table(
    "host_affiliation",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("host_id_id",ForeignKey("cdm.host.id"), comment="Host described by this record", index=False),
    Column("programme_id_id",ForeignKey("cdm.programme.id"), comment="Observing programme that this host is affiliated with", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date from which the details for this record are valid", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date after which the details for this record are no longer valid", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


programme = Table(
    "programme",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", String, comment="", index=False),
    Column("description", String, comment="", index=False),
    schema="cdm"
)


host_alias = Table(
    "host_alias",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("host_id_id",ForeignKey("cdm.host.id"), comment="Primary ID by which the host is known", index=False),
    Column("alternative_id", String, comment="Alternative ID by which the host is known", index=False),
    Column("alternative_name", String, comment="Alternative name by which the host is known", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Date the alternative id/name was used from", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Date the alternative id/name was used to", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


host_responsible_party = Table(
    "host_responsible_party",
    mapper_registry.metadata,
    Column("id", Integer, comment="", primary_key=True, index=False),
    Column("user_id_id",ForeignKey("cdm.user.id"), comment="", index=False),
    Column("description", String, comment="Description of role with this association. Note: this will be changed to a code table", index=False),
    schema="cdm"
)


host_media = Table(
    "host_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("host_id_id",ForeignKey("cdm.host.id"), comment="", index=False),
    Column("media_id_id",ForeignKey("cdm.media.id"), comment="", index=False),
    Column("valid_from", DateTime(timezone=True), comment="", index=False),
    Column("valid_to", DateTime(timezone=True), comment="", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


observer = Table(
    "observer",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of sensor", index=False),
    Column("description", String, comment="Description of sensor", index=False),
    Column("links", JSONB, comment="Link(s) to further information", index=False),
    Column("location", Geography, comment="Location of observer", index=False),
    Column("elevation", Numeric, comment="Elevation of observer above mean sea level", index=False),
    Column("manufacturer", String, comment="Make, or manufacturer, of sensor", index=False),
    Column("model", String, comment="Model of sensor", index=False),
    Column("serial_number", String, comment="Serial number of sensor", index=False),
    Column("firmware_version", String, comment="Firmware version of software installed in sensor", index=False),
    Column("control_schedule_id_id",ForeignKey("cdm.control_schedule.id"), comment="Link to information on calibration schedule and details", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


control_schedule = Table(
    "control_schedule",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Description of control schedule", index=False),
    schema="cdm"
)


observer_characteristics = Table(
    "observer_characteristics",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("observer_id_id",ForeignKey("cdm.observer.id"), comment="The observer to which this record applies", index=False),
    Column("observed_property_id_id",ForeignKey("cdm.observed_property.id"), comment="The observed parameter to which this record applies", index=False),
    Column("observing_method_id_id",ForeignKey("cdm.observing_method.id"), comment="Primary method/principles by which the sensor makes measurements", index=False),
    Column("measurement_units", Integer, comment="The units used in this record", index=False),
    Column("drift_per_unit_time", Numeric, comment="Sensor drift per unit time, units specified by measurement units, unit time by unit time", index=False),
    Column("unit_time", Integer, comment="Unit time for drift per unit time (seconds)", index=False),
    Column("valid_min", Numeric, comment="Minimum observable value by sensor, in units specificed by measurement units", index=False),
    Column("valid_max", Numeric, comment="Maximum observable value by sensor, in units specificed by measurement units", index=False),
    Column("measurement_uncertainty", Numeric, comment="Measurement uncertainty for measurements from this sensor, 2 sigma. Units as per measuremenet units", index=False),
    Column("measurement_accuracy", Numeric, comment="Measurement accuracy (trueness) for measurements from this sensor, 2 sigma. Units as per measuremenet units", index=False),
    Column("measurement_repeatability", Numeric, comment="Measurement repeatability (precision) for measurements from this sensor, 2 sigma. Units as per measuremenet units", index=False),
    Column("measurement_resolution", Numeric, comment="Minimum change detectable for measurements from this sensor. Units as per measurement units", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


observing_method = Table(
    "observing_method",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Description of observing method", index=False),
    schema="cdm"
)


observer_responsible_party = Table(
    "observer_responsible_party",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("user_id_id",ForeignKey("cdm.user.id"), comment="", index=False),
    Column("description", String, comment="Description of role with this association. Note: this will be changed to a code table", index=False),
    schema="cdm"
)


observer_media = Table(
    "observer_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("observer_id_id",ForeignKey("cdm.observer.id"), comment="", index=False),
    Column("media_id_id",ForeignKey("cdm.media.id"), comment="", index=False),
    Column("valid_from", DateTime(timezone=True), comment="", index=False),
    Column("valid_to", DateTime(timezone=True), comment="", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


collection = Table(
    "collection",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of collection", index=False),
    Column("links", JSONB, comment="Link(s) to further information on collection", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


feature = Table(
    "feature",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of feature", index=False),
    Column("description", String, comment="Description of feature", index=False),
    Column("links", JSONB, comment="Link(s) to further information on feature", index=False),
    Column("feature_type_id_id",ForeignKey("cdm.feature_type.id"), comment="enumerated feature type", index=False),
    Column("geometry", Geography, comment="", index=False),
    Column("elevation", Numeric, comment="Meam elevation of feature above mean sea level", index=False),
    Column("parent_id_id",ForeignKey("cdm.feature.id"), comment="Parent feature for this feature if nested", index=False),
    Column("properties", JSONB, comment="Array of named values consistent with that defined for the feature type", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


source = Table(
    "source",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("name", String, comment="Name of source", index=False),
    Column("description", String, comment="Description of source type, e.g. file etc", index=False),
    Column("source_type_id_id",ForeignKey("cdm.source_type.id"), comment="The type of source", index=False),
    Column("links", JSONB, comment="Link(s) to further information on source", index=False),
    Column("processor", String, comment="Name of processor used to ingest the data", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


observation = Table(
    "observation",
    mapper_registry.metadata,
    Column("id", String, comment="ID / primary key", primary_key=True, index=False),
    Column("location", Geography, comment="Location of observation", index=True),
    Column("elevation", Numeric, comment="Elevation of observation above mean sea level (in meters)", index=False),
    Column("observation_type_id_id",ForeignKey("cdm.observation_type.id"), comment="Type of observation", index=True),
    Column("phenomenon_start", DateTime(timezone=True), comment="Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end", index=False),
    Column("phenomenon_end", DateTime(timezone=True), comment="End time of the phenomenon being observed or observing period", index=True),
    Column("result_value", Numeric, comment="The value of the result in float representation", index=False),
    Column("result_uom", String, comment="Units used to represent the value being observed", index=False),
    Column("result_description", String, comment="str representation of the result if applicable", index=False),
    Column("result_quality", JSONB, comment="JSON representation of the result quality, key / value pairs", index=False),
    Column("result_time", DateTime(timezone=True), comment="Time that the result became available", index=False),
    Column("valid_from", DateTime(timezone=True), comment="Time that the result starts to be valid", index=False),
    Column("valid_to", DateTime(timezone=True), comment="Time after which the result is no longer valid", index=False),
    Column("host_id_id",ForeignKey("cdm.host.id"), comment="Host associated with making the observation, equivalent to OGC OMS 'host'", index=False),
    Column("observer_id_id",ForeignKey("cdm.observer.id"), comment="Observer associated with making the observation, equivalent to OGC OMS 'observer'", index=False),
    Column("observed_property_id_id",ForeignKey("cdm.observed_property.id"), comment="The phenomenon, or thing, being observed", index=True),
    Column("observing_procedure_id_id",ForeignKey("cdm.observing_procedure.id"), comment="Procedure used to make the observation", index=False),
    Column("collection_id_id",ForeignKey("cdm.collection.id"), comment="Primary collection or dataset that this observation belongs to. Note: this is different to the OGC OMS collection concept.", index=True),
    Column("parameter", JSONB, comment="List of key/ value pairs in dict", index=False),
    Column("feature_id_id",ForeignKey("cdm.feature.id"), comment="Feature of interest that this observation is associated with", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    Column("_source_id_id",ForeignKey("cdm.source.id"), comment="The source of this record", index=True),
    Column("_source_identifier", Integer, comment="The original identifier for the record from the data source", index=True),
    schema="cdm"
)


deployment = Table(
    "deployment",
    mapper_registry.metadata,
    Column("id", String, comment="Unique ID / primary key for deployment", primary_key=True, index=False),
    Column("host_id_id",ForeignKey("cdm.host.id"), comment="", index=False),
    Column("observer_id_id",ForeignKey("cdm.observer.id"), comment="", index=False),
    Column("valid_from", DateTime(timezone=True), comment="", index=False),
    Column("valid_to", DateTime(timezone=True), comment="", index=False),
    Column("installation_height", Numeric, comment="Installation height above reference surface (in meters)", index=False),
    Column("reference_surface_id",ForeignKey("cdm.reference_surface.id"), comment="", index=False),
    Column("exposure_id",ForeignKey("cdm.exposure.id"), comment="", index=False),
    Column("configuration", String, comment="Textual description of sensor installation and configuration", index=False),
    Column("maintenance_schedule_id_id",ForeignKey("cdm.maintenance_schedule.id"), comment="", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


maintenance_schedule = Table(
    "maintenance_schedule",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Description of maintenance schedule", index=False),
    schema="cdm"
)


exposure = Table(
    "exposure",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Description of sensor exposure according to WMO-No. 8", index=False),
    schema="cdm"
)


reference_surface = Table(
    "reference_surface",
    mapper_registry.metadata,
    Column("id", Integer, comment="", index=False),
    Column("name", Integer, comment="", index=False),
    Column("description", String, comment="Description of reference surface", index=False),
    schema="cdm"
)


deployment_media = Table(
    "deployment_media",
    mapper_registry.metadata,
    Column("id", String, comment="Primary key for this record", primary_key=True, index=False),
    Column("deployment_id_id",ForeignKey("cdm.deployment.id"), comment="", index=False),
    Column("media_id_id",ForeignKey("cdm.media.id"), comment="", index=False),
    Column("valid_from", DateTime(timezone=True), comment="", index=False),
    Column("valid_to", DateTime(timezone=True), comment="", index=False),
    Column("_version", Integer, comment="Version number of this record", index=False),
    Column("_change_date", DateTime(timezone=True), comment="Date this record was changed", index=False),
    Column("_user_id_id",ForeignKey("cdm.user.id"), comment="Which user/agent last modified this record", index=False),
    Column("_status_id_id",ForeignKey("cdm.status.id"), comment="Whether this is the latest version or an archived version of the record", index=False),
    Column("comments", String, comment="Free text comments on this record, for example description of changes made etc", index=False),
    schema="cdm"
)


def start_mappers():
    mapper_registry.map_imperatively(cdm.ObservationType, observation_type)
    mapper_registry.map_imperatively(cdm.FacilityType, facility_type)
    mapper_registry.map_imperatively(cdm.FeatureType, feature_type)
    mapper_registry.map_imperatively(cdm.WmoRegion, wmo_region)
    mapper_registry.map_imperatively(cdm.Territory, territory)
    mapper_registry.map_imperatively(cdm.ObservedProperty, observed_property)
    mapper_registry.map_imperatively(cdm.ObservingProcedure, observing_procedure)
    mapper_registry.map_imperatively(cdm.Status, status)
    mapper_registry.map_imperatively(cdm.TimeZone, time_zone)
    mapper_registry.map_imperatively(cdm.SourceType, source_type)
    mapper_registry.map_imperatively(cdm.User, user)
    mapper_registry.map_imperatively(cdm.Media, media)
    mapper_registry.map_imperatively(cdm.MediaType, media_type)
    mapper_registry.map_imperatively(cdm.Host, host)
    mapper_registry.map_imperatively(cdm.HostEnvironment, host_environment)
    mapper_registry.map_imperatively(cdm.ClimateZone, climate_zone)
    mapper_registry.map_imperatively(cdm.SurfaceCover, surface_cover)
    mapper_registry.map_imperatively(cdm.SurfaceRoughness, surface_roughness)
    mapper_registry.map_imperatively(cdm.Topography, topography)
    mapper_registry.map_imperatively(cdm.Season, season)
    mapper_registry.map_imperatively(cdm.HostAffiliation, host_affiliation)
    mapper_registry.map_imperatively(cdm.Programme, programme)
    mapper_registry.map_imperatively(cdm.HostAlias, host_alias)
    mapper_registry.map_imperatively(cdm.HostResponsibleParty, host_responsible_party)
    mapper_registry.map_imperatively(cdm.HostMedia, host_media)
    mapper_registry.map_imperatively(cdm.Observer, observer)
    mapper_registry.map_imperatively(cdm.ControlSchedule, control_schedule)
    mapper_registry.map_imperatively(cdm.ObserverCharacteristics, observer_characteristics)
    mapper_registry.map_imperatively(cdm.ObservingMethod, observing_method)
    mapper_registry.map_imperatively(cdm.ObserverResponsibleParty, observer_responsible_party)
    mapper_registry.map_imperatively(cdm.ObserverMedia, observer_media)
    mapper_registry.map_imperatively(cdm.Collection, collection)
    mapper_registry.map_imperatively(cdm.Feature, feature)
    mapper_registry.map_imperatively(cdm.Source, source)
    mapper_registry.map_imperatively(cdm.Observation, observation)
    mapper_registry.map_imperatively(cdm.Deployment, deployment)
    mapper_registry.map_imperatively(cdm.MaintenanceSchedule, maintenance_schedule)
    mapper_registry.map_imperatively(cdm.Exposure, exposure)
    mapper_registry.map_imperatively(cdm.ReferenceSurface, reference_surface)
    mapper_registry.map_imperatively(cdm.DeploymentMedia, deployment_media)

