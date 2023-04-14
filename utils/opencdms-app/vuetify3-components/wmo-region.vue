<template>
  <v-card>
    <v-card-title>Create new 'WmoRegion'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="wmoRegion.id" type="number" hint="ID / primary key" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="wmoRegion.name"  hint="Short name for feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="wmoRegion.description"  hint="Description of feature type" persistent-hint></v-text-field></v-card-item>
            <v-card-item><LinkForm :links="links" @updateLinks="updateLinks" ></LinkForm></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="wmoRegion._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_change_date" v-model="wmoRegion._change_date"  hint="Date this record was changed" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="wmoRegion._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="wmoRegion._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="wmoRegion.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createWmoRegion">Create WmoRegion</v-btn>
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


import User from '@/models/User';
import Status from '@/models/Status';

// import model
import WmoRegion from '@/models/WmoRegion';

export default defineComponent({
  name: 'WmoRegionForm',
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
      wmoRegion.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( wmoRegion.value._user !== null ){
        if ( 'description' in wmoRegion.value._user ){
          return wmoRegion.value._user.description;
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
      if( wmoRegion.value._status !== null ){
        if ( 'description' in wmoRegion.value._status ){
          return wmoRegion.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const wmoRegionRepo = useRepo(WmoRegion);
    const wmoRegion = ref(wmoRegionRepo.make());

    // function to create new object and to add to store
    const createWmoRegion = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,wmoRegion.value);
        await wmoRegionRepo.save(valueToSave);
        resetWmoRegion();
    };

    const resetWmoRegion = () => {
        Object.assign(wmoRegion.value, wmoRegionRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
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
        wmoRegion,
        createWmoRegion,
        resetWmoRegion,
        links,
        updateLinks,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
