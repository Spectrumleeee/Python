var search = {
	initBackground : function(){
		$(".searchResult li:odd").css("background", "rgb(234, 250, 234)");
		$(".searchResult li:even").css("background", "rgb(191, 239, 241)");
	},
	
	init : function(){
		search.initBackground();
	}
}

$(document).ready(search.init);
