import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '@/components/LandingPage.vue';
import AmplifierPage from '@/components/AmplifierPage.vue';
import DJMixerPage from '@/components/DJMixerPage.vue';
import SpeakersPage from '@/components/SpeakersPage.vue';
import MicroPhone from '@/components/MicroPhone.vue';
import AmplifierItemDetails from '@/components/AmplifierItemDetails.vue';
import AmplifierList from '@/components/Admin Components/AmplifierList.vue';
import EditAmplifier from '@/components/Admin Components/EditAmplifier.vue';
import AdminHomePage from '@/components/Admin Components/AdminHomePage.vue';
import UserHomePage from '@/components/UserHomePage.vue';
import AddSpeaker from '@/components/Admin Components/AddSpeaker.vue';
import EditSpeaker from '@/components/Admin Components/EditSpeaker.vue';
import SpeakerList from '@/components/Admin Components/SpeakerList.vue';
import AmplifierDetails from '@/components/AmplifierDetails.vue';

const routes = [
    {
        path: "/",
        name: "landingpage",
        component: LandingPage,
    },
    {
        path: "/amplifier",
        name: "amplifier",
        component: AmplifierPage,
    },
    {
        path: "/djmixer",
        name: "djmixer",
        component: DJMixerPage
    

    },
    {
        path: "/speaker",
        name: "speaker",
        component: SpeakersPage

    },
    {
        path: "/microphone",
        name: "microphone",
        component: MicroPhone

    },
    {
        path: "/amplifieritemdetails",
        name: 'amplifieritemdetails',
        component: AmplifierItemDetails
    },


    // router.js
    {
        path: '/admin/amplifierslist',
        component: AmplifierList
    },
    {
        path: '/amplifiers/edit/:id',
        component: EditAmplifier,
        props: true
    },
    {
        path: '/admin',
        name: 'adminhomepage',
        component: AdminHomePage,

    },
    {
        path: '/user',
        name: 'userhomepage',
        component: UserHomePage
    },
    {
        path: '/admin/speakerslist',
        name: 'speakers-list',
        component: SpeakerList
      },
      {
        path: '/admin/add-speaker',
        name: 'add-speaker',
        component: AddSpeaker
      },
      {
        path: '/admin/edit-speaker/:id',
        name: 'edit-speaker',
        component: EditSpeaker
      },
      {
        path: '/amplifier/:id',
        name: 'AmplifierDetails',
        // component: () => import('@/views/AmplifierDetails.vue'),
        component: AmplifierDetails,
        props: true
      }
      
    
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  // eslint-disable-next-line no-unused-vars
  scrollBehavior(to, from, savedPosition) {
    // Always scroll to top
    return { top: 0 };
  }

});

export default router;
