var stocks = {
	updateTimes : 1,
	updateIntervalMils : 60000,
	fiveMinutesMils : 300000,
	quarterHourMils : 900000,
	halfHourMils : 1800000,
	
	init : function(){
		setInterval("stocks.update()", stocks.updateIntervalMils);
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
	
	preShow : function(){
		var fiveMins = (stocks.updateIntervalMils * stocks.updateTimes) % stocks.fiveMinutesMils;
		var quarterHour = (stocks.updateIntervalMils * stocks.updateTimes) % stocks.quarterHourMils;
		var halfHourMils = (stocks.updateIntervalMils * stocks.updateTimes) % stocks.halfHourMils;
		
		if(halfHourMils == 0){
			var str = "<li style='background-color: rgb(236, 123, 141);'> 30# ";
			stocks.updateTimes = 1;
		}else if(quarterHour == 0){
			var str = "<li style='background-color: rgb(61, 192, 61);'> 15# ";
		}else if(fiveMins == 0){
			var str = "<li style='background-color: rgb(172, 165, 255);'> 5## ";
		}else{
			var str = "<li style='background-color: rgb(234,250,234);'> 1## ";
		}
		
		stocks.updateTimes++;
		
		return str;
	},
	
	showData : function(data){
		var str = stocks.preShow();
		
		str += data.stocks_sh_sz[0][1] + ' - ' + data.stocks_sh_sz[1][1] + " - ";
		for (index in data.stocks){
			str += data.stocks[index][0] + ":" + data.stocks[index][3] + " - " + data.stocks[index][4] + " - " + data.stocks[index][5] + " "
		}
		str += "</li>"
		$(".stocks-view").prepend(str);
	},
	
	currentTime : function(){
		now = new Date();
		var prefix = "3535 ";
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