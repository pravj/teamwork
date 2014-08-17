function addFields(){
	var months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", 
	"Oct", "Nov", "Dec"];
	var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	var colors = ["#eee", "#d6e685", "#8cc665", "#44a340", "#1e6823"];
	var current_month = new Date().getMonth() + 1;
	var extraDay = 5;
	var org = document.title;
	var url = "/calender/details";
	var data = {org: org};
	var today = Date.parse(new Date());

	$.post(url, data, function(res){
	
		var color_to_assign = new Array(365);
		var sizeof_res = Object.keys(res).length;
		// Array.apply(null, color_to_assign).map(Number.prototype.valueOf,0);
		for(var _t=0;_t<365;_t++)
			color_to_assign[_t] = 0;
		console.log(color_to_assign[0]);
		for(var temp=0; temp<sizeof_res; temp++){
			var date_from_now = parseInt((today - Date.parse(res[temp].repository_pushed_at))/86400000);
			if(date_from_now < 365){
				color_to_assign[date_from_now]++;
			}
		}
		var j=0;
		for(var i=current_month;i<current_month+12;i++){
			var monthField = document.createElement("div");
			monthField.setAttribute("class", "month");
			monthField.setAttribute("style", "transform: translate("+67*(i - current_month)+"px,"+(-15)*(i - current_month)+"px);");
			if(i>=12)
				monthField.innerHTML = months[i-12];
			else
				monthField.innerHTML = months[i];
			$(".calender-graph").append(monthField);
		}

		var field = document.createElement("div");
		field.setAttribute("id", "vert");
		field.setAttribute("style", "transform : translate(0px, -160px); width:13px");
		$(".calender-graph").append(field);
		for(var i=0;i<7;i++){
			var subField = document.createElement("div");
			subField.setAttribute("id", "square");
			if(i< extraDay)
				subField.setAttribute("style", "visibility:hidden;");
				
			else
				subField.setAttribute("style", "background:"+colors[0]);
			document.getElementById("vert").appendChild(subField);
		}

		for(var i=0; i<53;i++){
			var field = document.createElement("div");
			field.setAttribute("id", "vert"+i);
			var y_ = (-105)*(i+1)-160;
			field.setAttribute("style", "transform : translate("+15*(i+1)+"px, "+y_+"px); width: 13px; ");
			$(".calender-graph").append(field);
			for(var j=0; j<7;j++){
				var subField = document.createElement("div");
				subField.setAttribute("id", "square");
				var _d_ = (i*7) + j - 2;
				if(_d_ > 0){
					if(color_to_assign[365 - _d_] == 0){
						subField.setAttribute("style", "background:"+colors[0]);
					}
					else if(color_to_assign[365 - _d_] > 0 && color_to_assign[365 - _d_] <= 5){
						subField.setAttribute("style", "background:"+colors[1]);
					}
					else if(color_to_assign[365 - _d_] > 5 && color_to_assign[365 - _d_] <= 15){
						subField.setAttribute("style", "background:"+colors[2]);
					}
					else if(color_to_assign[365 - _d_] > 15){
						subField.setAttribute("style", "background:"+colors[3]);
					}
				}
				else{
					subField.setAttribute("style", "background:"+colors[3]);
				}
				document.getElementById("vert"+i).appendChild(subField);
			}
		}
	});
}

function compare_dates(date1, date2){
	if(date1 == date2)
		return 1;
	return 0;
}