import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';
import Status from '@/models/Status';

export default class ObservedProperty extends Model {
  static entity = 'observed_property';
  static fields() {
    return {
      id: this.number(null),
      short_name: this.string(''),
      standard_name: this.string(''),
      units: this.string(''),
      description: this.string(''),
      links: this.attr(new LinksType([])),
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

