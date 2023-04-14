import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';

export default class MaintenanceSchedule extends Model {
  static entity = 'maintenance_schedule';
  static fields() {
    return {
      id: this.number(null),
      name: this.number(null),
      description: this.string('')
    };
  };
};

