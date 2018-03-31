<template>
	<div id = "record-view">
    <el-row :gutter=20>
      <el-checkbox-group v-model="checkList">
        <el-col :span="3" :offset="3">
          <el-checkbox label="current">current</el-checkbox>
        </el-col>
        <el-col :span="3">
          <el-checkbox label="history">history</el-checkbox>
        </el-col>
      </el-checkbox-group>
    </el-row>
		<record-list-item
    :hidden = 'existData'
    v-bind:travels="paged"
		></record-list-item>
    <el-pagination :hidden = 'existData' layout="prev, pager, 
    next" :total="listw84page.length" :page-size="pageSize" :current-page.sync="currentPage">
    </el-pagination>
	</div>
</template>



<script>

import RecordListItem from '../components/RecordListItem'
import { page } from '../components/page.js'
import store from 'store'
<<<<<<< HEAD
=======

>>>>>>> 19232e1a47f46234c4e7be129b4543788489e16b
export default {
  name: 'record-view',

  components: {RecordListItem },

  mixins:[page],
  data () {
    return {
      checkList:['current'],
    	form:{
    		depart:'',
    		destination:'',
    		date1:'',
    		date2:'',
    	},
    	travels:[],
    }
  },
  computed: {
    listw84page:function(){
      var travels=[]
      var current=this.checkList.indexOf('current')>=0
      var history=this.checkList.indexOf('history')>=0
      this.travels.forEach(function(element) {
        if((element.isFuture && current)||(!element.isFuture && history))
          travels.push(element)
      });
      console.log('filtered',travels.length)
      return travels
    }
  },
  methods: {
  },

  created: function() {
    console.log("created")
    this.travels = []
    
    var params = new URLSearchParams();
<<<<<<< HEAD
    var no = store.get('token').no
    params.append('account_no', no);
=======
    params.append('account_no', store.get('token').no);
>>>>>>> 19232e1a47f46234c4e7be129b4543788489e16b
    this.$axios({
        method: 'post',
        url:  '/api/api/customer/getReserv',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded'
        },
        data: params
      }).then(response => {
        console.log("data",response.data)
        this.travels = response.data
      })
    },

}
</script>
