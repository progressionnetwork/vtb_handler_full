import Vue from 'vue'
import store from './store'
import App from './App.vue'
import router from "./router";
import Axios from 'axios'

Vue.prototype.$http = Axios;

String.prototype.capitalize = function() {
  return this.charAt(0).toUpperCase() + this.slice(1);
}

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')


