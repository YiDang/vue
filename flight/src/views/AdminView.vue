<template>
  <div id = "admin-view">
  <el-container>
    <el-aside width="200px">
      <admin-menu></admin-menu>
    </el-aside>
    <el-main>Main</el-main>
  </el-container>
  
  </div>
</template>



<script>
import AdminMenu from '../components/AdminMenu'

export default {

  name: 'admin-view',
  components: {AdminMenu},
  data () {
    return {

    }
  },
  methods: {

  }
}
</script>