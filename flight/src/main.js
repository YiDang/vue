// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en'
import VueSessionStorage from 'vue-sessionstorage'

Vue.config.productionTip = false
Vue.use(ElementUI, { locale })
Vue.use(VueSessionStorage)
/* eslint-disable no-new */

router.beforeEach((to, from, next) => {
  console.log("log")
  if(to.path == "/login") {
  	next()
  }
  console.log(this)
  // if(this.$session.exists('login')) {
  // 	next()
  // }
  // else {
  // 	next({ path: '/' })
  // }
  next()
  

})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
  components: { App },
  template: '<App/>'
})

