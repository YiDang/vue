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
					<el-date-picker type="date" placeholder="Departure time" v-model="form.date1" style="width: 100%;"></el-date-picker>
				</el-col>
        <el-col :span="5" v-show="trip == 'roundtrip'">
          <el-date-picker type="date" placeholder="Return time" v-model="form.date2" style="width: 100%;"></el-date-picker>
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
    
    <el-row :hidden = 'existData1'>
    {{form.depart}} to {{form.destination}}
      <search-list-item
      v-bind:direction="1"
      v-bind:travels="travels1"
      v-on:childEvent="onSelection">
      </search-list-item>
      <el-pagination layout="prev, pager, next" :total="50" :page-size="10">
      </el-pagination>
    </el-row>
    <!-- {{t1picked}} -->
		<el-row :hidden = 'existData2'>
      {{form.destination}} to {{form.depart}} 
      <search-list-item
      v-bind:direction="2"
      v-bind:travels="travels2"
      v-on:childEvent="onSelection">
      </search-list-item>
      <el-pagination layout="prev, pager, next" :total="50" :page-size="10">
      </el-pagination>
    </el-row>

    <el-row :hidden = 'existData3'>
      Result
      <search-list-item
      v-bind:direction="0"
      v-bind:travels="travelspicked">
      </search-list-item>
    </el-row>
    <el-row>
      <el-button v-show='submitable' type='submit' @click='onSubmit'>
        submit
      </el-button>
    </el-row>
    <!-- {{t2picked}} -->
	</div>
</template>



<script>

import SearchListItem from '../components/SearchListItem'

export default {
  name: 'book-view',

  components: {SearchListItem },

  data () {
    return {
      trip : 'oneway',
    	form:{
    		depart:'EWR',
    		destination:'JFK',
    		date1:'',
    		date2:'',
    	},
    	travels1:[],
      travels2:[],
      t1picked:'',
      t2picked:''
    }
  },
  methods: {
  	onSearch: function () {

  		this.travels1 = []

  		for(var i = 0; i < 10; i++){
  			this.travels1.push({
  				id:i,
    			from:'EWR',
    			to:'JFK',
    			depart:'00:00',
    			arrive:'00:00',
    			price:100,
    			stops:[
    			{
    				from:'a',
    				to:'b',
    				depart:'00:00',
    				arrive:'00:00',
    			},
    			{
    				from:'a',
    				to:'b',
    				depart:'00:00',
    				arrive:'00:00',
    			}
    			]

    		})
  		}
      if(this.trip=='roundtrip')
        this.travels2=this.travels1
  	},

    onSelection: function (data) {
      // console.log('book view')
      console.log(data.direction)
      switch(data.direction)
      {
        case 1:
        this.t1picked=data.data
        break;
        case 2:
        this.t2picked=data.data
        break;
      }
      // console.log(data.direction)
    },
    onSwitch:function(){
      console.log('clear') 
      this.travels1=this.travels2=[]
      this.t1picked=this.t2picked=''
    },
    onSubmit:function(){

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
      return this.t1picked==''&&this.t2picked==''
    },
    travelspicked:function(){
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
            switch(this.trip)
      {
        case 'oneway':
        return this.t1picked!=''
        break;
        case 'roundtrip':
        return this.t1picked!=''&&this.t2picked!=''
        break;
      }
    }
  }
}
</script>