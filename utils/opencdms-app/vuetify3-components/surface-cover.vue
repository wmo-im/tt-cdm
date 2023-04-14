<template>
  <v-card>
    <v-card-title>Create new 'SurfaceCover'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="surfaceCover.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="surfaceCover.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="surfaceCover.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createSurfaceCover">Create SurfaceCover</v-btn>
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
import SurfaceCover from '@/models/SurfaceCover';

export default defineComponent({
  name: 'SurfaceCoverForm',
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
      surfaceCover.value.links = updatedLinks;
    }

    // set up repos

    const surfaceCoverRepo = useRepo(SurfaceCover);
    const surfaceCover = ref(surfaceCoverRepo.make());

    // function to create new object and to add to store
    const createSurfaceCover = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,surfaceCover.value);
        await surfaceCoverRepo.save(valueToSave);
        resetSurfaceCover();
    };

    const resetSurfaceCover = () => {
        Object.assign(surfaceCover.value, surfaceCoverRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        surfaceCover,
        createSurfaceCover,
        resetSurfaceCover,
        links,
        updateLinks
    }
  }
});
</script>
