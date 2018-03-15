<template>
	<div id = "book-view">
		<header-bar></header-bar>
		<h1>Book page</h1>
		<el-form ref="form" :model="form" label-width="80px">
			<el-form-item label="">
				<el-row type="flex" class="row-bg" justify="center">

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
					<el-button type="primary" @click="onSubmit">Search</el-button>
				</el-col>
				</el-row>
			</el-form-item>
		</el-form>
	<ul>
		<search-list-item
		v-for="(travel,index) in travels"
		v-bind:key="travel.id"
		v-bind:id="travel.id"
		v-bind:from="travel.from"
		v-bind:to="travel.to"
		></search-list-item>
		<!-- <li v-for="(travel,index) in travels"
		>{{travel.from}},{{travel.to}}</li> -->

	</ul>
	</div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'
import SearchListItem from '../components/SearchListItem'

export default {
  name: 'book-view',
  components: { HeaderBar,SearchListItem },
  data () {
    return {
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
  		for(var i = 0; i < 10; i++){
  			this.travels.push({
  				id:i,
    			from:'EWR',
    			to:'JFK'
    		})
  		}
  	}

  }
}
</script>