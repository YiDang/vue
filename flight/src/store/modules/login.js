const state = {
  loginState:false
}

const mutations = {
  login(state){
    state.loginState = true;
  },
  logout(state){
    state.loginState = false; 
  }
}

const actions = {
  login({commit}){
    commit('login')
  },
  logout({commit}){
    commit('logout')
  }
}

export default {
  state,
  mutations,
  actions
}
