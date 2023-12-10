import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ReferenceSurface extends Model {
  static entity = 'reference_surface';
  static fields() {
    return {
      id: this.number(null),
      name: this.number(null),
      description: this.string('')
    };
  };
};

