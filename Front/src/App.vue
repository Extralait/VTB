<template>
  <div id="app">
    <Navbar
        :is_auth="getAuth.is_auth"
    />
    <RegPopup
        style="z-index: 10005"
        v-if="regPopupHashes.includes($route.hash)"
    />
    <router-view
        v-if="!loading"
        :user="getAuth.user"
    />
  </div>
</template>

<script>

import RegPopup from "@/components/common/RegPopup";
import {mapActions, mapGetters} from "vuex";
import Navbar from "@/components/common/Navbar";
import {HTTP} from "@/api/common";


export default {
  name: 'App',
  components: {
    RegPopup, Navbar
  },
  data() {
    return {
      loading: true,
      is_portfolio_emit: false,
      is_waiting_started:false,
      regPopupHashes: [
        '#sign_in',
        '#sign_up',
        '#reset_password',
        '#reset_password_confirmation',
        '#log_out',
        '#account_activation',
        '#api_key_change'
      ],
      reloadDataCounter: 0
    }
  },
  methods: {
    ...mapActions(['verifyToken', 'activation', 'authorization', 'logout', 'setUser', 'createUser']),
  },
  computed: {
    ...mapGetters(['getAuth']),
    is_auth: function () {
      return this.getAuth.is_auth
    },
  },
  async mounted() {
    let localStorageToken = localStorage.getItem('token')
    if (localStorageToken) {
      await this.verifyToken({"token": localStorageToken})
      if (!this.getAuth.errors.verifyError) {
        HTTP.defaults.headers.common['Authorization'] = 'JWT ' + localStorageToken
        await this.setUser()
      }
    }
    this.loading = false
  },
}

</script>

<style>
#app {
  position: relative;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

* {
  margin: 0;
  padding: 0;
}

#app {
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  position: relative;
}

.t-vue-title:first-child {
  display: none;
}

.no-scroll {
  overflow-y: hidden;
  overflow-x: hidden;
  display: block;
}

::-webkit-scrollbar {
  width: 0;
}

body {
  overflow-x: hidden;
}

</style>

<style scoped>
@import '../public/css/lib/bootstrap/bootstrap.min.css';
@import '../public/css/lib/calendar2/semantic.ui.min.css';
/*@import '../public/css/lib/calendar2/pignose.calendar.min.css';*/
@import '../public/css/lib/owl.carousel.min.css';
@import '../public/css/lib/owl.theme.default.min.css';
@import '../public/css/helper.css';
@import '../public/css/style.css';
@import '../public/css/lib/bootstrap/bootstrap.min.css';
@import '../public/css/lib/bootstrap/bootstrap.min.css';

    /*<link href="css/lib/calendar2/semantic.ui.min.css" rel="stylesheet">*/
    /*<link href="" rel="stylesheet">*/
    /*<link href="" rel="stylesheet" />*/
    /*<link href="" rel="stylesheet" />*/
    /*<link href="" rel="stylesheet">*/
    /*<link href="" rel="stylesheet">*/
    /*<script src="https:**oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>*/
    /*<script src="https:**oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>*/

</style>