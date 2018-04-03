<template>
  <div id = "reservation-view">
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.input" :placeholder='form.ph'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=6>
            <el-select v-model="groupby" placeholder="search by">
              <el-option
              v-for="item in form.typeEnum"
              :key="item.label"
              :label="item.label"
              :value="item.label">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span=3>
            <el-form-item>
              <el-button type="submit" @click="onSearch">Search</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-row>
<!--     <el-table
      v-show='show'
      :data="reservations"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="name"
        v-if="'name' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="flight"
        label="flight"
        v-if="'flight' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="stat1"
        label="stat1"
        width="180">
      </el-table-column>
    </el-table> -->
    <el-table
      :hidden='!show'
      border
      :data="paged"
      style="width: 80%; margin: auto">
      <el-table-column
        prop="reservation_no"
        label="reservation_no">
      </el-table-column>
      <el-table-column
        prop="departure"
        label="from">
      </el-table-column>
      <el-table-column
        prop="arrival"
        label="to">
      </el-table-column>
      <el-table-column
        prop="date"
        label="date">
      </el-table-column>
      <el-table-column
        label='stops'>
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
          <el-table :data="scope.row.stops.go" >
            <el-table-column property="departure_airport" label="departure_airport"></el-table-column>
            <el-table-column property="arrival_airport" label="arrival_airport"></el-table-column>
            <el-table-column property="departure_time" label="departure_time"></el-table-column>
            <el-table-column property="arrival_time" label="arrival_time"></el-table-column>
          </el-table>
          <el-table :data="scope.row.stops.back" v-show='scope.row.stops.back.length!=0'>
            <el-table-column property="departure_airport" label="departure_airport"></el-table-column>
            <el-table-column property="arrival_airport" label="arrival_airport"></el-table-column>
            <el-table-column property="departure_time" label="departure_time"></el-table-column>
            <el-table-column property="arrival_time" label="arrival_time"></el-table-column>
          </el-table>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">details</el-tag>
          </div>
          </el-popover>
        </template>    
      </el-table-column>
      <el-table-column
        prop="price"
        label="$price">
      </el-table-column>
      
      <el-table-column
        label='passengers'>
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
          <el-table :data="scope.row.passenger_info">
            <el-table-column property="name" label="name" width='150px'></el-table-column>
          </el-table>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">details</el-tag>
          </div>
          </el-popover>
        </template>    
      </el-table-column>
    </el-table>
    <el-pagination :hidden = 'existData' layout="prev, pager, 
    next" :total="listw84page.length" :page-size="pageSize" :current-page.sync="currentPage">
    </el-pagination>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import RecordListItem from '../../components/RecordListItem'
import { page } from '../../components/page.js'
import {prefix} from '../../components/prefix'
export default {

  name: 'reservation-view',
  mixins:[page],
  components: { RecordListItem },
  data () {
    return {
      form:{
        input:'',
        ph:'',
        flight:'',
        name:'',
        typeEnum:[{
          label:'name'
        },{
          label:'flight'
        }],
      },
      show:false,
      groupby:'',
      listw84page:[]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("register submit")
      // this.travels = []

      var params = new URLSearchParams();
      params.append('input', this.form.input);
      params.append('type', this.groupby);

      this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/listReservation',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log("respose",response.data)
        this.listw84page = response.data
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },

  },
  watch:{
    groupby: function(){
        this.listw84page=[]
        if(this.groupby=='name'){
            // this.form.name = this.form.input
            this.form.ph = 'customer name'
            this.show = false
        }
        if(this.groupby=='flight'){
            // this.form.flight = this.form.input
            this.form.ph = 'flight'
            this.show = false
        }
    }
  },
}
</script>
<!-- [ { "arrival": "SNA, Orange County", "date": "03/21/2018", "departure": "MIA, Miami", "isCurrent": false, "passenger_info": [ "Judy Durrant" ], "price": 404.58, "reservation_no": 1, "stops": { "back": [], "go": [ { "arrival_airport": "MSP", "arrival_time": "5:00pm", "departure_airport": "MIA", "departure_time": "2:02pm" }, { "arrival_airport": "SNA", "arrival_time": "9:42pm", "departure_airport": "MSP", "departure_time": "7:45pm" } ] } }, { "arrival": "ATL, Atlanta", "date": "03/19/2018", "departure": "PHX, Phoenix", "isCurrent": false, "passenger_info": [ "Judy Durrant" ], "price": 603.24, "reservation_no": 301, "stops": { "back": [ { "arrival_airport": "PHX", "arrival_time": "9:01pm", "departure_airport": "ATL", "departure_time": "7:51pm" } ], "go": [ { "arrival_airport": "ATL", "arrival_time": "6:46am", "departure_airport": "PHX", "departure_time": "12:15am" } ] } } ] -->