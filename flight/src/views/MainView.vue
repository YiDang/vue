<template>
	<div id = "main-view">
		<el-container>
			<el-header>
				<header-bar></header-bar>
			</el-header>
			<el-main>
				<router-view/>
			</el-main>
		</el-container>
		<!-- <book-view></book-view> -->
    
  </div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'
// import BookView from './BookView'

export default {
  name: 'main-view',
  components: { HeaderBar },

}
</script>