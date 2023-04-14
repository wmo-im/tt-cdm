import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';

export default class Status extends Model {
  static entity = 'status';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string(''),
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

