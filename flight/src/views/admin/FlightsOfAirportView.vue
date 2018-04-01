<template>
  <div id = "flights-of-airport-view">
    <h1>Flight of given airport</h1>
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.airport" placeholder='airport'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=3>
            <el-form-item>
              <el-button type="submit" @click="onSearch">Search</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-row>
    <el-table
      v-show='show'
      :data="paged"
      style="width: 100%">
      <el-table-column
        prop="airlineName"
        label="airlineName">
      </el-table-column>
      <el-table-column
        prop="flight_no"
        label="flight_no">
      </el-table-column>
      <el-table-column
        prop="plane"
        label="plane">
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
        prop="departure_weekday"
        label="departure_weekday">
      </el-table-column>
      <el-table-column
        prop="departure_time"
        label="departure_time">
      </el-table-column>
      <el-table-column
        prop="arrival_weekday"
        label="arrival_weekday">
      </el-table-column>
      <el-table-column
        prop="arrival_time"
        label="arrival_time">
      </el-table-column>
      <el-table-column
        prop="distance"
        label="distance">
      </el-table-column>
      <el-table-column
        prop="duration"
        label="duration">
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

  name: 'flights-of-airport-view',
  mixins:[page],
  // components: { HeaderBar },
  data () {
    return {
      form:{
        airport:''
      },
      show:false,
      listw84page:[]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("search submit")

      var params = new URLSearchParams();
      params.append('airportCode', this.form.airport);
      // console.log("input:",this.form.input)
      // console.log("groupby:",this.groupby)
      this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/listForAirport',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
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
}
</script>