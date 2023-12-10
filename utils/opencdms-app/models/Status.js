import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';

export default class Status extends Model {
  static entity = 'status';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string(''),
      _version: this.number(null),
      _change_date: this.string(''),
      _user_id: this.string(''),
      _user: this.belongsTo(User,'_user_id'),
      _comments: this.string('')
    };
  };
};

