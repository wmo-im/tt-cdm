import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class SurfaceCover extends Model {
  static entity = 'surface_cover';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

