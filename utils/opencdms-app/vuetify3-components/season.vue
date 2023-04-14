<template>
  <v-card>
    <v-card-title>Create new 'Season'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="season.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="season.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="season.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSeason">Create Season</v-btn>
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
import Season from '@/models/Season';

export default defineComponent({
  name: 'SeasonForm',
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
      season.value.links = updatedLinks;
    }

    // set up repos

    const seasonRepo = useRepo(Season);
    const season = ref(seasonRepo.make());

    // function to create new object and to add to store
    const createSeason = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,season.value);
        await seasonRepo.save(valueToSave);
        resetSeason();
    };

    const resetSeason = () => {
        Object.assign(season.value, seasonRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        season,
        createSeason,
        resetSeason,
        links,
        updateLinks
    }
  }
});
</script>
