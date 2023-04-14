<template>
  <v-card>
    <v-card-title>Create new 'Exposure'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="exposure.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="exposure.name" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="exposure.description"  hint="Description of sensor exposure according to WMO-No. 8" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createExposure">Create Exposure</v-btn>
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
import Exposure from '@/models/Exposure';

export default defineComponent({
  name: 'ExposureForm',
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
      exposure.value.links = updatedLinks;
    }

    // set up repos

    const exposureRepo = useRepo(Exposure);
    const exposure = ref(exposureRepo.make());

    // function to create new object and to add to store
    const createExposure = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,exposure.value);
        await exposureRepo.save(valueToSave);
        resetExposure();
    };

    const resetExposure = () => {
        Object.assign(exposure.value, exposureRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        exposure,
        createExposure,
        resetExposure,
        links,
        updateLinks
    }
  }
});
</script>
