<template>
  <v-card>
    <v-card-title>Create new 'DeploymentMedia'</v-card-title>
    <v-card-text>
        <v-form>
            <v-card-item><v-text-field label="id" v-model="deploymentMedia.id"  hint="Primary key for this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="deploymentOptions" item-title="name" item-value="id" label="deployment" v-model="deploymentMedia.deployment" :hint="deploymentOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="mediaOptions" item-title="name" item-value="id" label="media" v-model="deploymentMedia.media" :hint="mediaOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="valid_from" v-model="deploymentMedia.valid_from"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="valid_to" v-model="deploymentMedia.valid_to"  hint="" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_version" v-model="deploymentMedia._version" type="number" hint="Version number of this record" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-text-field label="_change_date" v-model="deploymentMedia._change_date"  hint="Date this record was changed" persistent-hint></v-text-field></v-card-item>
            <v-card-item><v-select :items="userOptions" item-title="name" item-value="id" label="user" v-model="deploymentMedia._user" :hint="userOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-select :items="statusOptions" item-title="name" item-value="id" label="status" v-model="deploymentMedia._status" :hint="statusOptionsHint" return-object persistent-hint></v-select></v-card-item>
            <v-card-item><v-text-field label="comments" v-model="deploymentMedia.comments"  hint="Free text comments on this record, for example description of changes made etc" persistent-hint></v-text-field></v-card-item>
        </v-form>
        <v-btn @click="createDeploymentMedia">Create DeploymentMedia</v-btn>
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


import Deployment from '@/models/Deployment';
import Media from '@/models/Media';
import User from '@/models/User';
import Status from '@/models/Status';

// import model
import DeploymentMedia from '@/models/DeploymentMedia';

export default defineComponent({
  name: 'DeploymentMediaForm',
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
      deploymentMedia.value.links = updatedLinks;
    }

    // set up repos
    const deploymentRepo = useRepo(Deployment);
    const deploymentOptions = computed(() => { return deploymentRepo.all() });
    const deploymentOptionsHint = computed(() => {
      if( deploymentMedia.value.deployment !== null ){
        if ( 'description' in deploymentMedia.value.deployment ){
          return deploymentMedia.value.deployment.description;
        }else{
          return "";
        }
      }else{
        return "Select deployment";
      }
    } );
    const mediaRepo = useRepo(Media);
    const mediaOptions = computed(() => { return mediaRepo.all() });
    const mediaOptionsHint = computed(() => {
      if( deploymentMedia.value.media !== null ){
        if ( 'description' in deploymentMedia.value.media ){
          return deploymentMedia.value.media.description;
        }else{
          return "";
        }
      }else{
        return "Select media";
      }
    } );
    const userRepo = useRepo(User);
    const userOptions = computed(() => { return userRepo.all() });
    const userOptionsHint = computed(() => {
      if( deploymentMedia.value._user !== null ){
        if ( 'description' in deploymentMedia.value._user ){
          return deploymentMedia.value._user.description;
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
      if( deploymentMedia.value._status !== null ){
        if ( 'description' in deploymentMedia.value._status ){
          return deploymentMedia.value._status.description;
        }else{
          return "";
        }
      }else{
        return "Select status";
      }
    } );

    const deploymentMediaRepo = useRepo(DeploymentMedia);
    const deploymentMedia = ref(deploymentMediaRepo.make());

    // function to create new object and to add to store
    const createDeploymentMedia = async () => {
        let valueToSave = {};
        Object.assign(valueToSave,deploymentMedia.value);
        await deploymentMediaRepo.save(valueToSave);
        resetDeploymentMedia();
    };

    const resetDeploymentMedia = () => {
        Object.assign(deploymentMedia.value, deploymentMediaRepo.make() );
    };


    onBeforeMount( async() => {
      // load reference data so this is available to the form
      if( deploymentRepo.all().length === 0){
          // load reference data
          loadCSV('/data/deployment.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            deploymentRepo.save(data.value);
          });
      }
      if( mediaRepo.all().length === 0){
          // load reference data
          loadCSV('/data/media.psv').then( (result) => {
            const data = ref(null);
            data.value = result.csvData;
            mediaRepo.save(data.value);
          });
      }
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
        deploymentMedia,
        createDeploymentMedia,
        resetDeploymentMedia,
        links,
        updateLinks,
        deploymentOptions, deploymentOptionsHint,
        mediaOptions, mediaOptionsHint,
        userOptions, userOptionsHint,
        statusOptions, statusOptionsHint
    }
  }
});
</script>
