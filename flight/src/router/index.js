import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MainView from '@/views/MainView'
import LoginView from '@/views/LoginView'
import BookView from '@/views/BookView'
import RecordView from '@/views/RecordView'
import UserInfoView from '@/views/UserInfoView'
Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/',
      redirect:'/login'
      // name: 'HelloWorld',
      // component: HelloWorld
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/main',
      name: 'MainView',
      component: MainView,     
      children: [
        {
          path:'book',
          name:'BookView',
          component:BookView
        },
        {
          path: 'user',
          name: 'UserInfoView',
          component: UserInfoView
        },
        {
          path: 'record',
          name: 'RecordView',
          component: RecordView
        } 
      ]
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    }
  ]
})
import store from 'store'
router.beforeEach((to, from, next) => {
  console.log(to)
  console.log(store.get('token'))
  if(to.path != '/login' && !store.get('token')){
    console.log('redirect')
    next({path: '/login'})
  }
  // console.log("log")
  //  var a = store.get('login')
  // console.log('before' , a)

  // store.set('login','xxx')
  // a = store.get('login')
  // console.log('after' , a)
  else next()
  

})

export default router
