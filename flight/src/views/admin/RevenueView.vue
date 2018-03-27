<template>
  <div id = "revenue-view">
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
    </el-table>

    <el-table
      v-show='showvip'
      :data="revenuevip"
      style="width: 100%">
      <el-table-column
        prop="customer"
        label="most valuable customer"
        width="180">
      </el-table-column>
      <el-table-column
        prop="revenue"
        label="revenue"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>



<script>
// import HeaderBar from '../components/HeaderBar'

export default {

  name: 'revenue-view',
  // components: { HeaderBar },
  data () {
    return {
      form:{
        input:'',
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
      revenue:[{
        flight:'ua123',
        city:'NY',
        customer:'9527'
      }],
      revenuevip:[{
        customer:'9527',
        revenue:'10000'
      }],
    }
  },
  methods: {
    onSearch:function(){
      this.show=true
      if(this.groupby=='customer'){
        this.showvip = true
      }
      else this.showvip = false
      console.log("register submit")
    },
  },
  watch:{
    groupby: function(){
        if(this.groupby=='flight'){
            this.form.flight = this.form.input
            this.form.ph = 'flight'
            this.show = this.showvip = false
        }
        if(this.groupby=='city'){
            this.form.city = this.form.input
            this.form.ph = 'city'
            this.show = this.showvip = false
        }
        if(this.groupby=='customer'){
            this.form.customer = this.form.input
            this.form.ph = 'customer'
            this.show = false
            this.showvip = false
        }
    }
}
}
</script>