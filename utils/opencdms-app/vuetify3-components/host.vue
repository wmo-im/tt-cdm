<template>
  <v-card>
    <v-card-title>Create new 'Host'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="host.id"  hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="host.name"  hint="Preferred name of host" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="host.description"  hint="Description of host" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="location" v-model="host.location"  hint="Location of station" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="elevation" v-model="host.elevation" type="number" hint="Elevation of station above mean sea level in meters" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="wigos_station_identifier" v-model="host.wigos_station_identifier"  hint="WIGOS station identifier" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="facilityTypeOptions" item-title="name" item-value="id" label="facility_type" v-model="host.facility_type" :hint="facilityTypeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="date_established" v-model="host.date_established"  hint="Date host was first established" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="date_closed" v-model="host.date_closed"  hint="Date host was first established" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="wmoRegionOptions" item-title="name" item-value="id" label="wmo_region" v-model="host.wmo_region" :hint="wmoRegionOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="territoryOptions" item-title="name" item-value="id" label="territory" v-model="host.territory" :hint="territoryOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="timeZoneOptions" item-title="name" item-value="id" label="time_zone" v-model="host.time_zone" :hint="timeZoneOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="valid_from" v-model="host.valid_from"  hint="Date from which the details for this record are valid" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="valid_to" v-model="host.valid_to"  hint="Date after which the details for this record are no longer valid" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="host._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_change_date" v-model="host._change_date"  hint="Date this record was changed" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="host._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="host._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="host.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHost">Create Host</v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
import * as d3 from 'd3';
import { defineComponent, ref, computed } from 'vue';
import { VCard, VCardTitle, VCardText, VCardItem, VForm, VTextField, VSelect, VBtn } from 'vuetify/lib/components';
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onErrorCaptured} from 'vue';
import {useStore} from 'pinia';
import {useRepo} from 'pinia-orm';

import LinkForm from '@/web-components/forms/links';


import FacilityType from '@/models/FacilityType';
import WmoRegion from '@/models/WmoRegion';
import Territory from '@/models/Territory';
import TimeZone from '@/models/TimeZone';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import Host from '@/models/Host';

export default defineComponent({
  name: 'HostForm',
  props: {
  },
  components: {
    VCard,
    VCardTitle,
    VCardText,
    VCardItem,
    VTextField,
    VSelect,
    VForm,
    VBtn,
    LinkForm
  },
  setup() {

    const loadCSV = async (path) => {
      let csvData;
      csvData = await d3.dsv('|',path, d3.autoType);
      return {csvData};
    };

    // set up links object
    const links = ref([]);
    const updateLinks = (updatedLinks) => {
      console.log("updating links");
      host.value.links = updatedLinks;
    }

    // set up repos
    const facilityTypeRepo = useRepo(FacilityType);
    const facilityTypeOptions = computed(() => { return facilityTypeRepo.all() });
    const facilityTypeOptionsHint = computed(() => {
      if( host.value.facility_type !== null ){
        if ( 'description' in host.value.facility_type ){
          return host.value.facility_type.description;
        }else{
          return "";
        }
      }else{
        return "Select facility_type";
      }
    } );
    const wmoRegionRepo = useRepo(WmoRegion);
    const wmoRegionOptions = computed(() => { return wmoRegionRepo.all() });
    const wmoRegionOptionsHint = computed(() => {
      if( host.value.wmo_region !== null ){
        if ( 'description' in host.value.wmo_region ){
          return host.value.wmo_region.description;
        }else{
          return "";
        }
      }else{
        return "Select wmo_region";
      }
    } );
    const territoryRepo = useRepo(Territory);
    const territoryOptions = computed(() => { return territoryRepo.all() });
    const territoryOptionsHint = computed(() => {
      if( host.value.territory !== null ){
        if ( 'description' in host.value.territory ){
          return host.value.territory.description;
        }else{
          return "";
        }
      }else{
        return "Select territory";
      }
    } );
    const timeZoneRepo = useRepo(TimeZone);
    const timeZoneOptions = computed(() => { return timeZoneRepo.all() });
    const timeZoneOptionsHint = computed(() => {
      if( host.value.time_zone !== null ){
        if ( 'description' in host.value.time_zone ){
          return host.value.time_zone.description;
        }else{
          return "";
        }
      }else{
        return "Select time_zone";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( host.value._user !== null ){
        if ( 'description' in host.value._user ){
          return host.value._user.description;
        }else{
          return "";
        }
      }else{
        return "Select user";
      }
    } );
    const statusRepo = useRepo(Status);
    const statusOptions = computed(() => { return statusRepo.all() });
    const statusOptionsHint = computed(() => {
      if( host.value._status !== null ){
        if ( 'description' in host.value._status ){
          return host.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostRepo = useRepo(Host);
    const host = ref(hostRepo.make());

    // function to create new object and to add to store
    const createHost = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,host.value);
        await hostRepo.save(valueToSave);
        resetHost();
    };

    const resetHost = () => {
        Object.assign(host.value, hostRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
      if( facilityTypeRepo.all().length === 0){
          // load reference data
          loadCSV('/data/facility_type.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            facilityTypeRepo.save(data.value);
          });
      }
      if( wmoRegionRepo.all().length === 0){
          // load reference data
          loadCSV('/data/wmo_region.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            wmoRegionRepo.save(data.value);
          });
      }
      if( territoryRepo.all().length === 0){
          // load reference data
          loadCSV('/data/territory.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            territoryRepo.save(data.value);
          });
      }
      if( timeZoneRepo.all().length === 0){
          // load reference data
          loadCSV('/data/time_zone.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            timeZoneRepo.save(data.value);
          });
      }
      if( userRepo.all().length === 0){
          // load reference data
          loadCSV('/data/user.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            userRepo.save(data.value);
          });
      }
      if( statusRepo.all().length === 0){
          // load reference data
          loadCSV('/data/status.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            statusRepo.save(data.value);
          });
      }
    });

    return {
        host,
        createHost,
        resetHost,
        links,
        updateLinks,
        facilityTypeOptions, facilityTypeOptionsHint,
        wmoRegionOptions, wmoRegionOptionsHint,
        territoryOptions, territoryOptionsHint,
        timeZoneOptions, timeZoneOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
