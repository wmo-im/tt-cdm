import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class MediaType extends Model {
  static entity = 'media_type';
  static fields() {
    return {
      id: this.number(null),
      name: this.number(null),
      description: this.string('')
    };
  };
};

