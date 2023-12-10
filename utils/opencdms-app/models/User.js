import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class User extends Model {
  static entity = 'user';
  static fields() {
    return {
      id: this.string(''),
      name: this.string(''),
      description: this.string('')
    };
  };
};

