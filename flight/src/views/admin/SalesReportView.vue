<template>
  <div id = "sales-report-view">
    <el-row :gutter="10">
      <el-form :model="month" ref="month" label-width="100px">
        <el-col :span="4">
          <el-input v-model="month.year" placeholder="year"></el-input>
        </el-col>
        <el-col :span="4">
            <el-select v-model="month.month" placeholder="Month">
              <el-option
              v-for="item in monthEum"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="4">
          <el-button type = "submit" @click="onMonthSelected">search</el-button>
        </el-col>
      </el-form>
    </el-row>
    <el-table
      :data="listw84page"
      style="width: 100%"
      v-show='showTable'>
      <el-table-column
        prop="name"
        label="Company"
        width="180">
      </el-table-column>
      <el-table-column
        prop="value"
        label="Revenue">
      </el-table-column>
      <el-table-column
        prop="# of flight"
        label="number of tickets">
      </el-table-column>
    </el-table>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'sales-report-view',
  // components: { HeaderBar },
  data () {
    return {
      month:{
        year:'',
        month:'',
      },
      showTable:false,
      saledate:[],
      listw84page:[],
      monthEum: [{
          value: 1,
          label: 'Jan'
        },{
          value: 2,
          label: 'Feb'
        },{
          value: 3,
          label: 'Mar'
        },{
          value: 4,
          label: 'Apr'
        },{
          value: 5,
          label: 'May'
        },{
          value: 6,
          label: 'Jun'
        },{
          value: 7,
          label: 'Jul'
        },{
          value: 8,
          label: 'Aug'
        },{
          value: 9,
          label: 'Sep'
        },{
          value: 10,
          label: 'Oct'
        },{
          value: 11,
          label: 'Nov'
        },{
          value: 12,
          label: 'Dec'
        }],
    }
  },
  methods: {
    onMonthSelected:function(){
      console.log("month selected")
      this.showTable=true
      var params = new URLSearchParams(this.month);
      this.$axios({
        method: 'post',
        url:  '/api/api/manager/getSalesReport',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.listw84page   = response.data
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },

  }
}
</script>