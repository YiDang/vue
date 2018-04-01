<template>
  <div id = "best-seller-view">
  <h1>BestSeller</h1>
  <div style="margin: 0 15%">
    <el-table
      :data="listw84page"
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
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import { page } from '../components/page.js'

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
        var tmp = response.data
        for(var i = 0; i<tmp.length&&i<10;i++){
          this.listw84page.push(tmp[i])
        }
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },

}
</script>