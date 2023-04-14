<template>
  <v-card>
    <v-card-title>Create new 'SurfaceRoughness'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="surfaceRoughness.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="surfaceRoughness.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="surfaceRoughness.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSurfaceRoughness">Create SurfaceRoughness</v-btn>
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
import SurfaceRoughness from '@/models/SurfaceRoughness';

export default defineComponent({
  name: 'SurfaceRoughnessForm',
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
      surfaceRoughness.value.links = updatedLinks;
    }

    // set up repos

    const surfaceRoughnessRepo = useRepo(SurfaceRoughness);
    const surfaceRoughness = ref(surfaceRoughnessRepo.make());

    // function to create new object and to add to store
    const createSurfaceRoughness = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,surfaceRoughness.value);
        await surfaceRoughnessRepo.save(valueToSave);
        resetSurfaceRoughness();
    };

    const resetSurfaceRoughness = () => {
        Object.assign(surfaceRoughness.value, surfaceRoughnessRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        surfaceRoughness,
        createSurfaceRoughness,
        resetSurfaceRoughness,
        links,
        updateLinks
    }
  }
});
</script>
