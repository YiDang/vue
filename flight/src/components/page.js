export const page= {
	data () {
		return {
        currentPage:1,
        pageSize:10,
      }
    },
    methods: {
    },
    computed:{
    	existData: function () {
    		return this.listw84page.length==0
    	},
    	paged:function(){
    		var start = this.pageSize*(this.currentPage-1)
    		var end = this.pageSize*this.currentPage
    		var travels = []
            console.log('listw84page length',this.listw84page.length)
    		for(var i=start; i<end && i < this.listw84page.length; i++){
    			travels.push(this.listw84page[i])
    		}
            console.log('paged length',travels.length)
    		return travels
    	}
    }
}
