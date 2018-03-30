<template>
  <div id = "seat-reserve-view">
    <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="form.flight" placeholder='flight'></el-input>
            </el-form-item>
          </el-col>
          <el-col :span=8>
            <el-form-item >
              <el-date-picker value-format="MM/dd/yyyy" type="date" placeholder="date" v-model="form.date2" style="width: 100%;"></el-date-picker>
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
      :data="reservation"
      style="width: 100%">
      <el-table-column
        prop="flight"
        label="flight"
        width="180">
      </el-table-column>
      <el-table-column
        prop="stat1"
        label="stat1"
        width="180">
      </el-table-column>
    </el-table>
    {{reservation}}
    <h1>Seat Reservation</h1>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'seat-reserve-view',
  // components: { HeaderBar },
  data () {
    return {
      form:{
        flight:'',
      },
      show:false,
      reservation:[]
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      console.log("register submit")

      var params = new URLSearchParams();
      params.append('flight', this.form.flight);
      console.log(this.form.flight)
      this.$axios({
        method: 'post',
        url:  '/api/api/manager/customerSeated',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.reservation = response.data
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },

  },
}
</script>