import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import FacilityType from '@/models/FacilityType';
import WmoRegion from '@/models/WmoRegion';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Host extends Model {
  static entity = 'host';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      links: this.attr(new LinksType([])),
      location: this.string(''),
      elevation: this.number(null),
      wigos_station_identifier: this.string(''),
      facility_type_id: this.string(''),
      facility_type: this.belongsTo(FacilityType,'facility_type_id'),
      date_established: this.string(''),
      date_closed: this.string(''),
      wmo_region_id: this.string(''),
      wmo_region: this.belongsTo(WmoRegion,'wmo_region_id'),
      territory_id: this.string(''),
      territory: this.belongsTo(Territory,'territory_id'),
      time_zone_id: this.string(''),
      time_zone: this.belongsTo(TimeZone,'time_zone_id'),
      valid_from: this.string(''),
      valid_to: this.string(''),
      _version: this.number(null),
      _change_date: this.string(''),
      _user_id: this.string(''),
      _user: this.belongsTo(User,'_user_id'),
      _status_id: this.string(''),
      _status: this.belongsTo(Status,'_status_id'),
      comments: this.string('')
    };
  };
};

