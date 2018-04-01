<template>
  <div id = "all-flights-view">
<!--     <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.name" placeholder='name'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=3>
            <el-form-item>
              <el-button type="submit" @click="onSearch">Search</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-row> -->
    <el-table
      :data="paged"
      style="width: 100%">
      <el-table-column
        prop="airlineCode"
        label="airlineCode">
      </el-table-column>
      <el-table-column
        prop="flight_no"
        label="flight_no">
      </el-table-column>
      <el-table-column
        prop="departure_airport"
        label="departure_airport">
      </el-table-column>
      <el-table-column
        prop="arrival_airport"
        label="arrival_airport">
      </el-table-column>
      <el-table-column
        prop="departure_time"
        label="departure_time">
      </el-table-column>
      <el-table-column
        prop="arrival_time"
        label="arrival_time">
      </el-table-column>
    </el-table>
    <el-pagination :hidden = 'existData' layout="prev, pager, 
    next" :total="listw84page.length" :page-size="pageSize" :current-page.sync="currentPage">
    </el-pagination>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import { page } from '../../components/page.js'
import {prefix} from '../../components/prefix'
export default {

  name: 'all-flights-view',
  // components: { HeaderBar },
  mixins:[page],
  data () {
    return {
      form:{
        company:''
      },
      listw84page:[]
    }
  },
  methods: {
    onSearch:function(){
      console.log("search submit")
    },

  },

  created: function() {
    console.log("created")
    this.listw84page = []
    
    var params = new URLSearchParams();
    params.append('account_no', 20);
    this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/listAllFlights',
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
    }
}
</script>