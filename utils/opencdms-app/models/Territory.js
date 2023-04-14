import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import WmoRegion from '@/models/WmoRegion';
import User from '@/models/User';
import Status from '@/models/Status';

export default class Territory extends Model {
  static entity = 'territory';
  static fields() {
    return {
      id: this.number(null),
      ISO3c: this.string(''),
      name: this.string(''),
      description: this.string(''),
      wmo_region_id: this.number(null),
      wmo_region: this.belongsTo(WmoRegion,'wmo_region_id'),
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

