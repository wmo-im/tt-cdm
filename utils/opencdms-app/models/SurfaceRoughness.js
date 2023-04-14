import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class SurfaceRoughness extends Model {
  static entity = 'surface_roughness';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

