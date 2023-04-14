<template>
  <v-card>
    <v-card-title>Create new 'ClimateZone'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="climateZone.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="climateZone.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="climateZone.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createClimateZone">Create ClimateZone</v-btn>
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



// import model
import ClimateZone from '@/models/ClimateZone';

export default defineComponent({
  name: 'ClimateZoneForm',
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
      climateZone.value.links = updatedLinks;
    }

    // set up repos

    const climateZoneRepo = useRepo(ClimateZone);
    const climateZone = ref(climateZoneRepo.make());

    // function to create new object and to add to store
    const createClimateZone = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,climateZone.value);
        await climateZoneRepo.save(valueToSave);
        resetClimateZone();
    };

    const resetClimateZone = () => {
        Object.assign(climateZone.value, climateZoneRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        climateZone,
        createClimateZone,
        resetClimateZone,
        links,
        updateLinks
    }
  }
});
</script>
