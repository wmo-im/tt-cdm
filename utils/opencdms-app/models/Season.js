import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Season extends Model {
  static entity = 'season';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

