<template>
  <v-card>
    <v-card-title>Create new 'Topography'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="topography.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="topography.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="topography.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createTopography">Create Topography</v-btn>
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
import Topography from '@/models/Topography';

export default defineComponent({
  name: 'TopographyForm',
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
      topography.value.links = updatedLinks;
    }

    // set up repos

    const topographyRepo = useRepo(Topography);
    const topography = ref(topographyRepo.make());

    // function to create new object and to add to store
    const createTopography = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,topography.value);
        await topographyRepo.save(valueToSave);
        resetTopography();
    };

    const resetTopography = () => {
        Object.assign(topography.value, topographyRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        topography,
        createTopography,
        resetTopography,
        links,
        updateLinks
    }
  }
});
</script>
