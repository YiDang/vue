<template>
  <div id = "on-timep-view">
    <el-table
      v-show='show'
      :data="listw84page"
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
    <el-pagination :hidden = 'total==0' layout="prev, pager, 
    next" :total="total" :page-size="pageSize" :current-page.sync="currentPage" 
    @current-change="handleCurrentChange">
    </el-pagination>

  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
// import { page } from '../../components/page.js'
import {prefix} from '../../components/prefix'
export default {

  name: 'on-timep-view',
  // mixins:[page],
  // components: { HeaderBar },
  data () {
    return {
      currentPage:1,
      pageSize:10,
      total:0,
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
    handleCurrentChange:function(){
      console.log(this.currentPage)

      this.listw84page = []
      var params = new URLSearchParams();
      var start = (this.currentPage - 1) * this.pageSize

      params.set('start',start)
      params.set('end',this.pageSize)
      this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/delayP',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.total = response.data.count[0][0]
        this.listw84page = response.data.delay

      })
    }

  },
  created: function() {
    console.log("created")
    this.listw84page = []
    var params = new URLSearchParams();
    params.set('start',0)
    params.set('end',this.pageSize)
    this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/delayP',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.total = response.data.count[0][0]
        this.listw84page = response.data.delay
      })
    }

}
</script>