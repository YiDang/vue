<template>
	<div id = "main-view">
		<header-bar></header-bar>
    <router-view/>
  </div>
</template>



<script>
import HeaderBar from '../components/HeaderBar'


export default {
  name: 'main-view',
  components: { HeaderBar },

}
</script>