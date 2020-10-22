import Vue from 'vue'
import La from '@/components/La.vue'
//import router from './router'
import store from './store'

if (Vue.config.devtools) {
  let recaptchaScript = document.createElement("script");
  recaptchaScript.setAttribute("src", "http://localhost:8098");
  document.head.appendChild(recaptchaScript);
}

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

new Vue({
  //router,
  store,
  render: h => h(La)
}).$mount('#la')
