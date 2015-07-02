var search = {
	initBackground : function(){
		$(".searchResult li:odd").css("background", "rgb(234, 250, 234)");
		$(".searchResult li:even").css("background", "rgb(228, 245, 246)");
	},
	
	init : function(){
		search.initBackground();
	}
}

$(document).ready(search.init);
