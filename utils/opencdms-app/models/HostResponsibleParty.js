import { Model } from 'pinia-orm'
import LinksType from '@/models/LinksType';
import User from '@/models/User';

export default class HostResponsibleParty extends Model {
  static entity = 'host_responsible_party';
  static fields() {
    return {
      id: this.number(null),
      user_id: this.number(null),
      user: this.belongsTo(User,'user_id'),
      description: this.string('')
    };
  };
};

