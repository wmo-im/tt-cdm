import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Exposure extends Model {
  static entity = 'exposure';
  static fields() {
    return {
      id: this.number(null),
      name: this.number(null),
      description: this.string('')
    };
  };
};

