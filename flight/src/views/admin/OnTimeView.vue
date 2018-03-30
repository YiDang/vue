<template>
  <div id = "on-time-view">
    <!-- <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.flight" placeholder='flight'></el-input>
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
      v-show='show'
      :data="paged"
      style="width: 100%">
      <el-table-column
        prop="airline_code"
        label="airline code"
        width="120">
      </el-table-column>
      <el-table-column
        prop="flight_no"
        label="flight no"
        width="100">
      </el-table-column>
      <el-table-column
        prop="departure_airport"
        label="departure airport"
        width="140">
      </el-table-column>
      <el-table-column
        prop="departure_date"
        label="departure date"
        width="140">
      </el-table-column>
      <el-table-column
        prop="departure_time"
        label="departure time"
        width="140">
      </el-table-column>
      <el-table-column
        prop="departure_time"
        label="scheduled departure time"
        width="200">
      </el-table-column>
      <el-table-column
        prop="delay"
        label="delayed time(mins)"
        width="150">
      </el-table-column>
      <el-table-column
        prop="isdelay"
        label=""
        width="150">
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

export default {

  name: 'on-time-view',
  mixins:[page],
  // components: { HeaderBar },
  data () {
    return {
     form:{
        airport:''
      },
      show:true,
      flights:[{
        flight:'ua350',
        type:'delayed',
        time:'',
        scheduletime:''
      },{
        flight:'ua350',
        type:'delayed',
        time:'',
        scheduletime:''
      }],
      listw84page:[]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("register submit")
    },

  },
  created: function() {
    console.log("created")
    this.listw84page = []
    
    this.$axios({
        method: 'post',
        url:  '/api/api/manager/delay',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
      }).then(response => {
        console.log(response.data)
        this.listw84page = response.data
        // for(var i =0;i<3;i++){
        //   this.listw84page.push(response.data[i])
        // }
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },
}
</script>