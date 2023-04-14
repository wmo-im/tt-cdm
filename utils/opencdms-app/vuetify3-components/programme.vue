<template>
  <v-card>
    <v-card-title>Create new 'Programme'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="programme.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="programme.name"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="programme.description"  hint="" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createProgramme">Create Programme</v-btn>
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
import Programme from '@/models/Programme';

export default defineComponent({
  name: 'ProgrammeForm',
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
      programme.value.links = updatedLinks;
    }

    // set up repos

    const programmeRepo = useRepo(Programme);
    const programme = ref(programmeRepo.make());

    // function to create new object and to add to store
    const createProgramme = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,programme.value);
        await programmeRepo.save(valueToSave);
        resetProgramme();
    };

    const resetProgramme = () => {
        Object.assign(programme.value, programmeRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        programme,
        createProgramme,
        resetProgramme,
        links,
        updateLinks
    }
  }
});
</script>
