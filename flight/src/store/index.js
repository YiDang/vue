import Vue from 'vue'
import Vuex from 'vuex'
import login from './modules/login'
// 暂时不用了 03/15/2018
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    login:login
  }
})
