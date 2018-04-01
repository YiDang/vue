<template>
  <div id = "admin-view">
  <el-container>
    <el-aside width="200px">
      <admin-menu></admin-menu>
    </el-aside>
    <el-main>
      <router-view/>
    </el-main>
  </el-container>
  </div>
</template>



<script>
import AdminMenu from '../components/AdminMenu'
import {prefix} from '../components/prefix'
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