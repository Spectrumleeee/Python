var stocks = {
	init : function(){
		setInterval("stocks.update()", 30000);
		//stocks.getFreshStocksData();
		setInterval("stocks.currentTime()", 1000);
	},
	
	update : function(){
		$.ajax({
		type: "POST",
		url: "stocks",
		contentType : "application/x-www-form-urlencoded",
		data: {
			username : "liguangpu",
			password : "123456"
		},
		success: function(data){
			stocks.showData(data);
		}});
	},
	
	showData : function(data){
		var str = "<li>";
		str += data.stocks_sh_sz[0][1] + ' - ' + data.stocks_sh_sz[1][1] + " - ";
		for (index in data.stocks){
			str += data.stocks[index][0] + ":" + data.stocks[index][3] + " - " + data.stocks[index][4] + " - " + data.stocks[index][5] + " "
		}
		str += "</li>"
		$(".stocks-view").prepend(str);
	},
	
	currentTime : function(){
		now = new Date();
		var prefix = "4620 16.32 ";
		var year = now.getFullYear();
		var month = now.getMonth();
		var day = now.getDay();
		var hours = now.getHours();
		var minutes = now.getMinutes();
		var seconds = now.getSeconds();
		var currentTime = prefix + year + "/" + month + "/" + day + " " + hours + ":" + minutes + ":" + seconds;
		$(".current-time").text(currentTime);
		return currentTime;
	}
}

$(document).ready(stocks.init)