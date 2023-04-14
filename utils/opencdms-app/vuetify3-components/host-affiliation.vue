<template>
  <v-card>
    <v-card-title>Create new 'HostAffiliation'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="hostAffiliation.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="hostOptions" item-title="name" item-value="id" label="host" v-model="hostAffiliation.host" :hint="hostOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="programmeOptions" item-title="name" item-value="id" label="programme" v-model="hostAffiliation.programme" :hint="programmeOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="valid_from" v-model="hostAffiliation.valid_from"  hint="Date from which the details for this record are valid" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="valid_to" v-model="hostAffiliation.valid_to"  hint="Date after which the details for this record are no longer valid" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="hostAffiliation._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_change_date" v-model="hostAffiliation._change_date"  hint="Date this record was changed" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="hostAffiliation._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="hostAffiliation._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="hostAffiliation.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createHostAffiliation">Create HostAffiliation</v-btn>
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


import Host from '@/models/Host';
import Programme from '@/models/Programme';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import HostAffiliation from '@/models/HostAffiliation';

export default defineComponent({
  name: 'HostAffiliationForm',
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
      hostAffiliation.value.links = updatedLinks;
    }

    // set up repos
    const hostRepo = useRepo(Host);
    const hostOptions = computed(() => { return hostRepo.all() });
    const hostOptionsHint = computed(() => {
      if( hostAffiliation.value.host !== null ){
        if ( 'description' in hostAffiliation.value.host ){
          return hostAffiliation.value.host.description;
        }else{
          return "";
        }
      }else{
        return "Select host";
      }
    } );
    const programmeRepo = useRepo(Programme);
    const programmeOptions = computed(() => { return programmeRepo.all() });
    const programmeOptionsHint = computed(() => {
      if( hostAffiliation.value.programme !== null ){
        if ( 'description' in hostAffiliation.value.programme ){
          return hostAffiliation.value.programme.description;
        }else{
          return "";
        }
      }else{
        return "Select programme";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( hostAffiliation.value._user !== null ){
        if ( 'description' in hostAffiliation.value._user ){
          return hostAffiliation.value._user.description;
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
      if( hostAffiliation.value._status !== null ){
        if ( 'description' in hostAffiliation.value._status ){
          return hostAffiliation.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const hostAffiliationRepo = useRepo(HostAffiliation);
    const hostAffiliation = ref(hostAffiliationRepo.make());

    // function to create new object and to add to store
    const createHostAffiliation = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,hostAffiliation.value);
        await hostAffiliationRepo.save(valueToSave);
        resetHostAffiliation();
    };

    const resetHostAffiliation = () => {
        Object.assign(hostAffiliation.value, hostAffiliationRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
      if( hostRepo.all().length === 0){
          // load reference data
          loadCSV('/data/host.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            hostRepo.save(data.value);
          });
      }
      if( programmeRepo.all().length === 0){
          // load reference data
          loadCSV('/data/programme.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            programmeRepo.save(data.value);
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
        hostAffiliation,
        createHostAffiliation,
        resetHostAffiliation,
        links,
        updateLinks,
        hostOptions, hostOptionsHint,
        programmeOptions, programmeOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
