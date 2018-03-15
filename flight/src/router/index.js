import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LoginView from '@/views/LoginView'
import BookView from '@/views/BookView'
import UserInfoView from '@/views/UserInfoView'
import ListView from '@/views/ListView'
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
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },

    {
      path: '/book',
      name: 'BookView',
      component: BookView,
      children: [
      	{
      		path:'list',
      		name:'ListView',
      		component:ListView
      		
      	}
      ]
    },
    {
      path: '/user',
      name: 'UserInfoView',
      component: UserInfoView
    }
  ]
})

router.beforeEach((to, from, next) => {
  console.log("log")
  if(to.path == "/login") {
    next()
  }
  console.log(this)
  // if(this.$session.exists('login')) {
   // next()
  // }
  // else {
  //  next({ path: '/' })
  // }
  next()
  

})

export default router
