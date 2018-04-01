<template>
  <div id = "active-flights-view">
  <h1>Most active flights</h1>
  <div style="margin: 0 15%">
    <el-table
      :data="paged"
      style="width: 100%">
      <el-table-column
        prop="airlineCode"
        label="airlineCode"
        width="180">
      </el-table-column>
      <el-table-column
        prop="flight_no"
        label="flight_no"
        width="180">
      </el-table-column>
      <el-table-column
        prop="active_number"
        label="active point"
        width="180">
      </el-table-column>
    </el-table>
    </div>
    <el-pagination :hidden = 'existData' layout="prev, pager, 
    next" :total="listw84page.length" :page-size="pageSize" :current-page.sync="currentPage">
    </el-pagination>
    <el-button @click="onTest"></el-button>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import { page } from '../../components/page.js'
import {prefix} from '../../components/prefix'
export default {

  name: 'active-flights-view',
  mixins:[page],
  // components: { HeaderBar },
  data () {
    return {
      listw84page:[]
    }
  },
  methods: {
    onRegister:function(){
      console.log("register submit")
    },
    onTest:function(){
      this.$router.push({
        target:"_blank"
      })
    },

  },
  created: function() {
    console.log("created")
    this.listw84page = []
    
    this.$axios({
        method: 'post',
        url:  '/api/api/manager/mostActiveFlight',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
      }).then(response => {
        console.log(response.data)
        this.listw84page = response.data
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },

}
</script>