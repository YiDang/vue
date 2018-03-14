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
		<router-view/>
	</div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'

export default {
  name: 'book-view',
  components: { HeaderBar },
  data () {
    return {
    	form:{
    		depart:'',
    		destination:'',
    		date1:'',
    		date2:'',
    	}
    }
  },
  methods: {
  	onSubmit: function () {
  		this.$router.push({name: 'ListView'})
  	}

  }
}
</script>