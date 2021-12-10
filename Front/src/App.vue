<template>
  <div id="app">
    <RegPopup
        style="z-index: 10005"
        v-if="regPopupHashes.includes($route.hash)"
    />
    <router-view
        v-if="!loading"
        :is_auth="getAuth.is_auth"
    />
  </div>
</template>

<script>

import RegPopup from "@/components/common/RegPopup";
import {mapActions, mapGetters} from "vuex";
import {HTTP} from "@/api/common";


export default {
  name: 'App',
  components: {
    RegPopup
  },
  data() {
    return {
      loading: true,
      is_portfolio_emit: false,
      is_waiting_started: false,
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
    ...mapActions(['verifyToken', 'activation', 'authorization', 'logout', 'setUser', 'createUser','setFiles']),
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
        try {
          await this.setUser()
          await this.setFiles('?ordering=created_at')
        } catch (e) {
          // statements to handle any exceptions
          localStorage.setItem('token', '')
          console.log(e); // pass exception object to error handler
        }
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

