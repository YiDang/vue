<template>
	<div id = "book-view">
		<el-form ref="form" :model="form" label-width="0px">
			<el-form-item label="">
				<el-row type="flex" class="row-bg" justify="center" :gutter="20">

				<el-col :span="3">
					<el-input placeholder="From airport" v-model="form.depart"></el-input>
				</el-col>
				<el-col :span="3">
					<el-input placeholder="To airport" v-model="form.destination"></el-input>
				</el-col>

				<el-col :span="5">
					<el-date-picker value-format="MM/dd/yyyy" type="date" placeholder="Departure date" v-model="form.date1" style="width: 100%;"></el-date-picker>
				</el-col>
        <el-col :span="5" v-show="trip == 'roundtrip'">
          <el-date-picker value-format="MM/dd/yyyy" type="date" placeholder="Return date" v-model="form.date2" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col :span="2">
          <el-row type="flex" class="row-bg" justify="center">
            <el-radio v-model="trip" @change="onSwitch" label="oneway">one-way</el-radio>
          </el-row>
          <el-row type="flex" class="row-bg" justify="center">
            <el-radio v-model="trip" @change="onSwitch" label="roundtrip">round</el-radio>
          </el-row>
        </el-col>

				<el-col :span="3">
					<el-button type="primary" @click="onSearch">Search</el-button>
				</el-col>
				</el-row>
			</el-form-item>
		</el-form>
    <el-row >
    {{traveltype}}
    </el-row>
    <el-row :hidden = 'existData1'>
    {{form.depart}} to {{form.destination}}
      <search-list-item
      @rowChange="onRowChange1"
      v-bind:travels="travels1paged"
      >
      </search-list-item>
      <el-pagination layout="prev, pager, next" 
      :total="travels1.length" :page-size="pageSize" :current-page.sync="currentPage1">
      </el-pagination>
    </el-row>
    <!-- {{t1picked}} -->
		<el-row :hidden = 'existData2'>
      {{form.destination}} to {{form.depart}} 
      <search-list-item
      @rowChange="onRowChange2"
      v-bind:travels="travels2paged"
      >
      </search-list-item>
      <el-pagination layout="prev, pager, next" 
      :total="travels2.length" :page-size="pageSize" :current-page.sync="currentPage2">
      </el-pagination>
    </el-row>

    <el-row :hidden = 'existData3'>
      Result
      <search-list-item
      v-bind:travels="travelspicked">
      </search-list-item>
    </el-row>
    <el-row>Passenger list
      <el-table
      :data="passengers"
      style="width: 80%; margin: auto">
        <el-table-column
        prop="ssn"
        label="ssn"
        width="180">
        </el-table-column>
        <el-table-column
        prop="name"
        label="name"
        width="180">
        </el-table-column>
        <el-table-column
        prop="reserved"
        label="reserved"
        width="180">
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">reserve a seat</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <el-row>
      <el-form :inline="true" :model="newPsg">
        <el-form-item label="SSN">
          <el-input v-model="newPsg.ssn" placeholder="SSN"></el-input>
        </el-form-item>
        <el-form-item label="Name">
          <el-input v-model="newPsg.name" placeholder="Name"></el-input>
        </el-form-item>
          <el-button type="primary" @click="addPassenger">AddPassenger</el-button>
        </el-form-item>
        </el-form-item>
          <el-button type="primary" @click="emptyPassenger">Empty list</el-button>
        </el-form-item>
        {{addMsg}}
      </el-form>
    </el-row>
    <el-row>
      <el-button v-show='submitable' type='submit' @click='onSubmit'>
        submit
      </el-button>
    </el-row>
	</div>
</template>



<script>

import SearchListItem from '../components/SearchListItem'
import store from 'store'

export default {
  name: 'book-view',

  components: {SearchListItem },

  data () {
    return {
      trip : 'oneway',
    	form:{
    		depart:'EWR',
    		destination:'ORD',
    		date1:'',
    		date2:''
    	},
      newPsg:{
        ssn:'',
        name:'',
        reserved:'N'
      },
      addMsg:'',
      currentPage1:1,
      currentPage2:1,
      pageSize:5,
    	travels1:[],
      travels2:[],
      passengers:[],
      t1picked:{},
      t2picked:{},
      traveltype:''
    }
  },
  methods: {
  	onSearch: function () {
      // console.log(this.form.date1)
  		this.travels1 = []
      this.travels2 = []

      var params = new URLSearchParams(this.form);
      params.set('trip', this.trip=='oneway'?0:1)
      this.$axios({
        method: 'post',
        url:  '/api/api/customer/searchFlight',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
        this.travels1 = this.nullfilter(response.data[0])
        this.travels2 = this.nullfilter(response.data[1])
      })

      //request for that if it is domestic
      params = new URLSearchParams(this.form);
      this.$axios({
        method: 'post',
        url:  '/api/api/manager/getDomestic',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log('international?',response.data)
        if(response.data[0].domestic=='true') this.traveltype='You are looking for a DOMESTIC trip'
          else this.traveltype='You are looking for an INTERNATIONAL trip'
      })

      // this.travels1.push({departure:1,arrival:1})
      // this.travels1.push({departure:1,arrival:2})
      // this.travels2.push({departure:1,arrival:1})
      // this.travels2.push({departure:1,arrival:3})
  	},

    nullfilter: function (list) {
      var tmp=[]
      if(list == null && list == undefined) return tmp
      console.log('list',list.length)
      var x = list.length
      for(var i = 0;i < x; i++){
        if(list[i] != null){
          tmp.push(list[i])
        }
        
      }
      return tmp
    },
    onRowChange1: function (data) {
      this.t1picked=data
    },
    onRowChange2: function (data) {
      this.t2picked=data
    },

    onSwitch:function(){
      this.travels1=this.travels2=[]
      this.t1picked=this.t2picked=null
    },
    onSubmit:function(){
      var params = new URLSearchParams();
      params.set('go',JSON.stringify(this.t1picked))
      params.set('back',JSON.stringify(this.t2picked))
      params.set('account_no',store.get('token').no)
      params.set('passengers', JSON.stringify(this.passengers))
      if(this.trip == 'oneway') params.set('type',1)
      else params.set('type',2)
      this.$axios({
        method: 'post',
        url:  '/api/api/customer/bookFlight',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log(response.data)
      })
    },
    addPassenger:function(){
      if(this.newPsg.ssn=='' || this.newPsg.name==''){
        this.addMsg='ssn or name cannot be empty'
      }
      else{
        this.addMsg=''
        this.passengers.push(this.newPsg)
        this.newPsg={
         ssn:'',
         name:''
       }
      }
    },
    emptyPassenger:function(){
      this.passengers = []
    },
    handleClick:function(row){
      row.reserved='Y'
    }
  },
  computed: {

  	existData1: function () {
      // console.log(this.travels.length)
      return this.travels1.length==0
    },
    existData2: function () {
      // console.log(this.travels.length)
      return this.travels2.length==0
    },
    existData3: function () {
      // console.log(this.travels.length)
      return this.travelspicked.length!=0
    },
    travels1paged:function(){
      var start = this.pageSize*(this.currentPage1-1)
      var end = this.pageSize*this.currentPage1
      var travels = []
      for(var i=start; i<end && i < this.travels1.length; i++){
        travels.push(this.travels1[i])
      }
      // console.log(this.currentPage1)
      return travels
    },
    travels2paged:function(){
      var start = this.pageSize*(this.currentPage2-1)
      var end = this.pageSize*this.currentPage2
      var travels = []
      for(var i=start; i<end && i < this.travels2.length; i++){
        travels.push(this.travels2[i])
      }
      // console.log(this.currentPage1)
      return travels
    },
    travelspicked:function(){
      console.log(this.trip)
      switch(this.trip)
      {
        case 'oneway':
        return [this.t1picked]
        break;
        case 'roundtrip':
        return [this.t1picked,this.t2picked]
        break;
      }
    },
    submitable:function(){
      var b= true
      switch(this.trip)
      {
        case 'oneway':
        b=b&& this.t1picked!={}
        break;
        case 'roundtrip':
        b=b&& this.t1picked!={}&&this.t2picked!={}
        break;
      }
      b=b&&this.passengers.length!=0
      return b
    }
  }
}
</script>