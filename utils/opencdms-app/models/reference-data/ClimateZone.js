import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class ClimateZone extends Model {
  static entity = 'climate_zone';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      links: this.string(''),
      _version: this.number(null),
      _change_date: this.string(''),
      _user_id: this.number(null),
      _user: this.belongsTo(User,'_user_id'),
      _status_id: this.number(null),
      _status: this.belongsTo(Status,'_status_id'),
      comments: this.string('')
    };
  };
};
