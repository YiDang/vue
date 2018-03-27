export const page= {
	data () {
		return {
        currentPage:1,
        pageSize:5,
      }
    },
    methods: {
    	// onPageChange: function (list) {
    	// 	console.log('page')
    	// 	var start = this.pageSize*(this.currentPage-1)
    	// 	var end = this.pageSize*this.currentPage
    	// 	var travels = []
    	// 	for(var i=start; i<end && i < this.filtered.length; i++){
    	// 		travels.push(this.filtered[i])
    	// 	}      
    	// 	this.paged=travels
    	// }
    },
    computed:{
    	existData: function () {
    		return this.listw84page.length==0
    	},
    	paged:function(){
    		var start = this.pageSize*(this.currentPage-1)
    		var end = this.pageSize*this.currentPage
    		var travels = []
    		for(var i=start; i<end && i < this.listw84page.length; i++){
    			travels.push(this.listw84page[i])
    		}

    		return travels
    	}
    }
}
