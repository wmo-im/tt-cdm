import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class TimeZone extends Model {
  static entity = 'time_zone';
  static fields() {
    return {
      id: this.number(null),
      abbreviation: this.string(''),
      name: this.string(''),
      offset: this.number(null),
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

