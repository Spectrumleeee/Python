var analyzer = {
	init : function(){
		analyzer.initAreaSelector();
		analyzer.initXY();
	},
	
	initAreaSelector : function(){
		$('.city_selector').CitySelector();
	},
	
	initXY : function(){
		var vData1 = [[3, 28], [4, 83], [5, 103], [6, 115], [7, 128], [8, 116], [9, 96], [10, 116], [11, 93], [12, 86], [13, 104], [14, 114], [15, 84], [16, 100], [17, 103], [18, 129], [19, 112], [20, 119], [21, 92], [22, 118], [23, 106], [24, 141], [25, 87], [26, 136], [27, 123], [28, 113], [29, 139], [30, 97], [31, 107]];
/*		
		vData1 = []; vData2 = []; vData3 = [];
		for( var i = 1; i < 13; i+=1 ){
			vData1.push([i, 30*i])
			vData2.push([i, Math.random()*400])
			vData3.push([i, Math.random()*200])
		}
*/				
		plot = $.plot($("#placeholder"), [{ label: "Apple = 000.00", data: vData1}],{
			crosshair: {mode: "x"},
			grid: {hoverable: true, autoHighlight: false},
			series: { lines: { show: true }, points: { show: true} },
			xaxis: { ticks: [[1, "20150510"], [7, "20150516"], [13, "20150522"], [19, "20150529"], [25, "20150604"], [31, "20150610"]], min: 1, max: 31 },
			yaxis: { ticks: 10, min: 0 }
		});

		var legends = $("#placeholder .legendLabel");

		legends.each(function () {
			// fix the widths so they don't jump around
			$(this).css('width', $(this).width());
		});

		var updateLegendTimeout = null;
		var latestPosition = null;

		function updateLegend() {

			updateLegendTimeout = null;

			var pos = latestPosition;

			var axes = plot.getAxes();
			if (pos.x < axes.xaxis.min || pos.x > axes.xaxis.max ||
				pos.y < axes.yaxis.min || pos.y > axes.yaxis.max) {
				return;
			}

			var i, j, dataset = plot.getData();
			for (i = 0; i < dataset.length; ++i) {

				var series = dataset[i];

				// Find the nearest points, x-wise

				for (j = 0; j < series.data.length; ++j) {
					if (series.data[j][0] > pos.x) {
						break;
					}
				}

				// Now Interpolate

				var y,
					p1 = series.data[j - 1],
					p2 = series.data[j];

				if (p1 == null) {
					y = p2[1];
				} else if (p2 == null) {
					y = p1[1];
				} else {
					y = p1[1] + (p2[1] - p1[1]) * (pos.x - p1[0]) / (p2[0] - p1[0]);
				}

				legends.eq(i).text(series.label.replace(/=.*/, "= " + y.toFixed(2)));
			}
		}

		$("#placeholder").bind("plothover",  function (event, pos, item) {
			latestPosition = pos;
			if (!updateLegendTimeout) {
				updateLegendTimeout = setTimeout(updateLegend, 50);
			}
		});
	}
}

$(document).ready(analyzer.init);