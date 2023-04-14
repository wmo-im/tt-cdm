<template>
  <v-card>
    <v-card-title>Create new 'MediaType'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="mediaType.id" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="name" v-model="mediaType.name" type="number" hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="description" v-model="mediaType.description"  hint="Type of media uploaded" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createMediaType">Create MediaType</v-btn>
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
import MediaType from '@/models/MediaType';

export default defineComponent({
  name: 'MediaTypeForm',
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
      mediaType.value.links = updatedLinks;
    }

    // set up repos

    const mediaTypeRepo = useRepo(MediaType);
    const mediaType = ref(mediaTypeRepo.make());

    // function to create new object and to add to store
    const createMediaType = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,mediaType.value);
        await mediaTypeRepo.save(valueToSave);
        resetMediaType();
    };

    const resetMediaType = () => {
        Object.assign(mediaType.value, mediaTypeRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
    });

    return {
        mediaType,
        createMediaType,
        resetMediaType,
        links,
        updateLinks
    }
  }
});
</script>
