import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import MainView from '@/views/MainView'
import LoginView from '@/views/LoginView'
import BookView from '@/views/BookView'
import BestSellerView from '@/views/BestSellerView'
import RecordView from '@/views/RecordView'
import UserInfoView from '@/views/UserInfoView'
import AdminView from '@/views/AdminView'

import ActiveFlightsView from '@/views/admin/ActiveFlightsView'
import AllFlightsView from '@/views/admin/AllFlightsView'
import FlightsOfAirportView from '@/views/admin/FlightsOfAirportView'
import OnTimeView from '@/views/admin/OnTimeView'
import ReservationView from '@/views/admin/ReservationView'
import RevenueView from '@/views/admin/RevenueView'
import SalesReportView from '@/views/admin/SalesReportView'
import SeatReserveView from '@/views/admin/SeatReserveView'
import UserManageView from '@/views/admin/UserManageView'

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
          path: 'record',
          name: 'RecordView',
          component: RecordView
        },
        {
          path: 'bestseller',
          name: 'BestSellerView',
          component: BestSellerView
        },
        {
          path: 'user',
          name: 'UserInfoView',
          component: UserInfoView
        },
        {
          path: 'admin',
          name: 'AdminView',
          component: AdminView,
          children: [
              {
                path: '/activeflights',
                name: 'ActiveFlightsView',
                component: ActiveFlightsView
              },
              {
                path: '/allflights',
                name: 'AllFlightsView',
                component: AllFlightsView
              },
              {
                path: '/flightsofairport',
                name: 'FlightsOfAirportView',
                component: FlightsOfAirportView
              },
              {
                path: '/ontime',
                name: 'OnTimeView',
                component: OnTimeView
              },
              {
                path: '/reservation',
                name: 'ReservationView',
                component: ReservationView
              },
              {
                path: '/revenue',
                name: 'RevenueView',
                component: RevenueView
              },
              {
                path: '/salesreport',
                name: 'SalesReportView',
                component: SalesReportView
              },
              {
                path: '/seatreserve',
                name: 'SeatReserveView',
                component: SeatReserveView
              },
              {
                path: '/usermanage',
                name: 'UserManageView',
                component: UserManageView
              },

          ]
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
  // console.log(to)
  // console.log(store.get('token'))
  if(to.path.indexOf('admin')>=0) console.log('admin')
  if(to.path != '/login' && !store.get('token')){
    // console.log('redirect')
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
