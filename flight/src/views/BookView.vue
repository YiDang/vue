<template>
	<div id = "book-view">
		<!-- <h1>Book page</h1> -->
		<el-form ref="form" :model="form" label-width="80px">
			<el-form-item label="">
				<el-row type="flex" class="row-bg" justify="center" :gutter="20">

				<el-col :span="4">
					<el-input placeholder="From airport" v-model="form.depart"></el-input>
				</el-col>
				<el-col :span="4">
					<el-input placeholder="To airport" v-model="form.destination"></el-input>
				</el-col>

				<el-col :span="4">
					<el-date-picker type="date" placeholder="Departure time" v-model="form.date1" style="width: 100%;"></el-date-picker>
				</el-col>
        <el-col :span="4">
          <el-row type="flex" class="row-bg" justify="center">
            <el-radio v-model="trip" label="oneway">one-way</el-radio>
          </el-row>
          <el-row type="flex" class="row-bg" justify="center">
            <el-radio v-model="trip" label="roundtrip">round</el-radio>
          </el-row>
        </el-col>

				<el-col :span="4">
					<el-button type="primary" @click="onSubmit">Search</el-button>
				</el-col>
				</el-row>
			</el-form-item>
		</el-form>
		<search-list-item
			:hidden = 'existData'
			v-bind:travels="travels">
		</search-list-item>
		<el-pagination :hidden = 'existData' layout="prev, pager, next" :total="50" :page-size="10">
		</el-pagination>
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
    		depart:'',
    		destination:'',
    		date1:'',
    		date2:'',
    	},
    	travels:[

    	]
    }
  },
  methods: {
  	onSubmit: function () {

  		this.travels = []

  		for(var i = 0; i < 10; i++){
  			this.travels.push({
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
  	}

  },
  computed: {
  	existData: function () {
      // console.log(this.travels.length)
      return this.travels.length==0
    },
  },
}
</script>