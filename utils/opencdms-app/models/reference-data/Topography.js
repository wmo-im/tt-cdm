import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class Topography extends Model {
  static entity = 'topography';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

