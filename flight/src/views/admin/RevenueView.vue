<template>
  <div id = "revenue-view">
      <el-row>
      <el-form ref="form" :model="form" label-width="0px">
        <el-row :gutter=10>
          <el-col :span=8>
            <el-form-item >
              <el-input v-model="input" :placeholder='form.ph'></el-input>
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

    <el-table
      v-show='show'
      :data="revenue"
      style="width: 100%">
      <el-table-column
        prop="flight"
        label="flight"
        v-if="'flight' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="city"
        label="city"
        v-if="'city' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="customer"
        label="customer"
        v-if="'customer' == groupby"
        width="180">
      </el-table-column>
      <el-table-column
        prop="revenue"
        label="revenue"
        width="180">
      </el-table-column>
    </el-table>
<!-- {{revenue}}revenue<br/> -->
<!-- {{revenue[0].mostCustomerRev}}customer<br/> -->
<!-- {{form.flight}}-flight<br/> -->
<!-- {{form.city}}-city<br/> -->
<!-- {{form.customer}}-customer<br/> -->
    <el-row v-show='showvip'>
      <el-table
      :data="vip"
      style="width: 100%">
        <el-table-column
        prop="account_no"
        label="account_no"
        width="180">
        </el-table-column>
        <el-table-column
        prop="first_name"
        label="first_name"
        width="180">
        </el-table-column>
        <el-table-column
        prop="last_name"
        label="last_name"
        width="180">
        </el-table-column>
        <el-table-column
        prop="revenue"
        label="revenue"
        width="180">
        </el-table-column>
      </el-table>
      Customer who generate most interest
    </el-row>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'
import {prefix} from '../../components/prefix'
export default {

  name: 'revenue-view',
  // components: { HeaderBar },
  data () {
    return {
      input:'',
      form:{
        ph:'',
        flight:'',
        city:'',
        customer:'',
        typeEnum:[{
          label:'flight',          
        },{
          label:'city',          
        },{
          label:'customer',          
        }]
      },
      groupby:'flight',
      show:false,
      showvip:false,
      revenue:[],
      vip:[]

    }
  },
  methods: {
    onSearch:function(){
      this.revenue=[]
      this.input=''
      this.vip=[]
      this.show=true
      if(this.groupby=='customer'){
        this.showvip = true
      }
      else this.showvip = false
      console.log("register submit")

      var params = new URLSearchParams();
      params.append('flight', this.form.flight);
      params.append('city', this.form.city);
      params.append('customer', this.form.customer);
      params.append('groupby', this.groupby);
      // console.log("input:",this.form.input)
      // console.log("groupby:",this.groupby)
      this.$axios({
        method: 'post',
        url:  prefix + '/api/manager/getRevList',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.revenue = response.data
        if(this.revenue.length>0) {
          this.vip.push(this.revenue[0].mostCustomerRev)
          console.log('vip',this.vip)
        }
        // console.log(response.status)
        // console.log(response.statusText)
        // console.log(response.headers)
        // console.log(response.config)
      })
    },
  },
  watch:{
    groupby: function(){
        this.revenue=[]
        this.input=''
        this.vip=[]
        if(this.groupby=='flight'){
            this.form.ph = 'flight'
            this.show = this.showvip = false
        }
        if(this.groupby=='city'){
            this.form.ph = 'city'
            this.show = this.showvip = false
        }
        if(this.groupby=='customer'){
            this.form.ph = 'customer'
            this.show = false
            this.showvip = false
        }
    },
    input:function(){
        this.revenue=[]
        this.input=''
        this.vip=[]
      if(this.groupby=='flight'){
            this.form.flight = this.input
        }
        if(this.groupby=='city'){
            this.form.city = this.input
        }
        if(this.groupby=='customer'){
            this.form.customer = this.input
        }
    }
}
}
</script>