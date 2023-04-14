<template>
  <v-card>
    <v-card-title>Create new 'ObserverResponsibleParty'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="observerResponsibleParty.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="observerResponsibleParty.user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="description" v-model="observerResponsibleParty.description"  hint="Description of role with this association. Note: this will be changed to a code table" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createObserverResponsibleParty">Create ObserverResponsibleParty</v-btn>
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

// import model
import ObserverResponsibleParty from '@/models/ObserverResponsibleParty';

export default defineComponent({
  name: 'ObserverResponsiblePartyForm',
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
      observerResponsibleParty.value.links = updatedLinks;
    }

    // set up repos
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( observerResponsibleParty.value.user !== null ){
        if ( 'description' in observerResponsibleParty.value.user ){
          return observerResponsibleParty.value.user.description;
        }else{
          return "";
        }
      }else{
        return "Select user";
      }
    } );

    const observerResponsiblePartyRepo = useRepo(ObserverResponsibleParty);
    const observerResponsibleParty = ref(observerResponsiblePartyRepo.make());

    // function to create new object and to add to store
    const createObserverResponsibleParty = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,observerResponsibleParty.value);
        await observerResponsiblePartyRepo.save(valueToSave);
        resetObserverResponsibleParty();
    };

    const resetObserverResponsibleParty = () => {
        Object.assign(observerResponsibleParty.value, observerResponsiblePartyRepo.make() );
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
    });

    return {
        observerResponsibleParty,
        createObserverResponsibleParty,
        resetObserverResponsibleParty,
        links,
        updateLinks,
        userOptions, userOptionsHint
    }
  }
});
</script>
