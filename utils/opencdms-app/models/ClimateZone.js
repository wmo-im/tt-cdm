import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class ClimateZone extends Model {
  static entity = 'climate_zone';
  static fields() {
    return {
      id: this.number(null),
      name: this.string(''),
      description: this.string('')
    };
  };
};

