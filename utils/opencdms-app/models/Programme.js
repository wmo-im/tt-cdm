import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Programme extends Model {
  static entity = 'programme';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

