import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ObservingMethod extends Model {
  static entity = 'observing_method';
  static fields() {
    return {
      id: this.number(null),
      name: this.number(null),
      description: this.string('')
    };
  };
};

