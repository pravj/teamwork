function addFields(){
	var months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", 
	"Oct", "Nov", "Dec"],
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
	colors = ["#eee", "#d6e685", "#8cc665", "#44a340", "#1e6823"],
	current_month = new Date().getMonth() + 1, today = Date.parse(new Date()),
	extraDay = 5, url = "/calender/details", org = document.title, data = {org: org},
	total_commit = 0, longest_streak = 0, temp_long_streak = 0, current_streak = 0,
	temp_ = new Date(), temp_date = temp_.getDate(), temp_month = temp_.getMonth()+1,
	temp_year = temp_.getFullYear() - 1, long_from, long_to, temp_long_from, temp_long_to;

	long_from = temp_date+" "+months[temp_month - 1]+" "+temp_year;
	long_to = temp_date+" "+months[temp_month - 1]+" "+temp_year;

	$.post(url, data, function(res){
		var color_to_assign = new Array(366), sizeof_res = Object.keys(res).length;
		for(var _t=0;_t<366;_t++) color_to_assign[_t] = 0;
		for(var temp=0; temp<sizeof_res; temp++){
			var date_from_now = parseInt((today - Date.parse(res[temp].repository_pushed_at))/86400000);
			if(date_from_now < 366){
				color_to_assign[date_from_now]++;
				total_commit++;
			}
		}
		var j=0;

		/*Months on top*/
		for(var i=current_month;i<current_month+12;i++){
			var monthField = document.createElement("div");
			monthField.setAttribute("class", "month");
			monthField.setAttribute("style", "transform: translate("+67*(i - current_month)+"px,"+(-15)*(i - current_month)+"px);");
			if(i>=12)
				monthField.innerHTML = months[i-12];
			else
				monthField.innerHTML = months[i];
			$(".months").append(monthField);
		}

		var field = document.createElement("div");
		field.setAttribute("id", "vert");
		field.setAttribute("style", "transform : translate(0px, 0px); width:13px");
		$(".contrib").append(field);

		/*First two days*/
		for(var i=0;i<7;i++){
			var subField = document.createElement("div");
			subField.setAttribute("id", "square");
			if(i< extraDay){
				subField.setAttribute("style", "visibility:hidden;");
			}
			else{
				if(temp_date > days[temp_month - 1]){
					temp_date = 1;
					temp_month++;
				}
				var col, commits_of_day = color_to_assign[370-i];
				if(commits_of_day != 0){
					temp_long_streak += 1;
				}
				else{
					temp_long_from = temp_date+" "+months[temp_month - 1]+" "+temp_year;
					temp_long_streak = 0;
				}
				if(longest_streak < temp_long_streak){
					longest_streak = temp_long_streak;
					long_from = temp_long_from;
					long_to = temp_date+" "+months[temp_month - 1]+" "+temp_year;
				}
				temp_long_streak = 0;
				if(commits_of_day == 0)
					col = colors[0];
				else if (commits_of_day < 5)
					col = colors[1];
				else if(commits_of_day < 15)
					col = colors[2];
				else
					col = colors[3];
				subField.setAttribute("class", "hint--left");
				subField.setAttribute("data-hint", commits_of_day+" Contributions on "+temp_date+" "+months[temp_month - 1]+" "+temp_year);
				subField.setAttribute("style", "background:"+col);
				temp_date++;
			}
			document.getElementById("vert").appendChild(subField);
		}

		/*Remaining days*/
		for(var i=0; i<52;i++){
			var field = document.createElement("div");
			field.setAttribute("id", "vert"+i);
			var y_ = (-105)*(i+1);
			field.setAttribute("style", "transform : translate("+15*(i+1)+"px, "+y_+"px); width: 13px; ");
			$(".contrib").append(field);
			for(var j=0; j<7;j++){
				var subField = document.createElement("div");
				subField.setAttribute("id", "square");
				var _d_ = (i*7) + j;
				if(_d_ >= 0){
					if(temp_date > days[temp_month - 1]){
						temp_date = 1;
						temp_month++;
						if(temp_month > 12){
							temp_month = 1;
							temp_year++;
						}
					}
					// subField.setAttribute("date", temp_date+" "+months[temp_month - 1]+" "+temp_year);
					commits_of_day = color_to_assign[363 - _d_ ];
					if(commits_of_day != 0){
						temp_long_streak += 1;
					}
					else{
						temp_long_from = temp_date+" "+months[temp_month - 1]+" "+temp_year;
						temp_long_streak = 0;
						col = colors[0];
					}

					if(longest_streak < temp_long_streak){
						longest_streak = temp_long_streak;
						long_from = temp_long_from;
						long_to = temp_date+" "+months[temp_month - 1]+" "+temp_year;
					}
					if(commits_of_day != 0)
					if(commits_of_day <= 5) col = colors[1];
					else if(commits_of_day <= 15) col = colors[2];
					else col = colors[3];
					// subField.setAttribute("count", commits_of_day);
					subField.setAttribute("class", "hint--left");
					subField.setAttribute("data-hint", commits_of_day+" Contributions on "+temp_date+" "+months[temp_month - 1]+" "+temp_year);
					subField.setAttribute("style", "background:"+col);
					temp_date++;
				}
				else {
					if(temp_date > days[temp_month - 1]){
						temp_date = 1;
						temp_month++;
						if(temp_month > 12){
							temp_month = 1;
							temp_year++;
						}
					}
					subField.setAttribute("date", temp_date+" "+months[temp_month - 1]+" "+temp_year);
					subField.setAttribute("style", "background:"+colors[3]);
					temp_date++;
					// subField.setAttribute("count", commits_of_day);
					// subField.setAttribute("onmouseover", "hover("+this+")");
				}
				document.getElementById("vert"+i).appendChild(subField);
			}
		}
		if(longest_streak < temp_long_streak){
			longest_streak = temp_long_streak;
			long_from = temp_long_from;
			long_to = temp_date+" "+months[temp_month - 1]+" "+temp_year;
		}
		current_streak = temp_long_streak;
		temp_long_streak = 0;

		console.log(long_from);
		console.log(long_to);
		/*Contribution details.*/
		var contrib_day = document.createElement("div");
		contrib_day.setAttribute("class", "lbl1");
		contrib_day.innerHTML = total_commit+ " total";
		$(".contrib-day").append(contrib_day);
		var longest_streak_div = document.createElement("div");
		var date_range = document.createElement("div");
		date_range.innerHTML = long_from+" - "+long_to;
		date_range.setAttribute("class", "lbl1");
		longest_streak_div.setAttribute("class", "lbl1");
		longest_streak_div.innerHTML = longest_streak+" days";
		$(".longest-streak").append(longest_streak_div);
		$(".longest-streak").append(date_range);
		var current_streak_div = document.createElement("div");
		current_streak_div.setAttribute("class", "lbl1");
		current_streak_div.innerHTML = current_streak+" days";
		$(".current-streak").append(current_streak_div);
		// load_graph(color_to_assign);
		console.log(window.innerHeight);
		console.log(window.innerWidth);
		load_org_detail();
	});
}

function load_org_detail(){
	var org = document.title, url = "/api/org";

	$.ajax({url: url}).done(function(res) {
		res = JSON.parse(res);
		var img = document.createElement("img");
		img.setAttribute("src", res.avatar_url);
		$(".org-detail").append(img);
		var h1 = document.createElement("hi");
		h1.setAttribute("class", "org-name");
		$(".org-detail").append(h1);
		var h1_div = document.createElement("longest_streak_div");
		h1_div.innerHTML = res.login;
		$(".org-name").append(h1_div);
		// var h1_span_span = document.createElement("span");
		// h1_span_span.innerHTML = org;
		// $(".org-name").append(h1_span_span);
		var line = document.createElement("div");
		line.setAttribute("class", "line");
		$(".org-detail").append(line);
		/*
		var location = document.createElement("div"), email = document.createElement("div"), created_at = document.createElement("div");
		location.setAttribute("class", "loc-em-cr");
		location.innerHTML = res.location;
		email.innerHTML = res.email;
		email.setAttribute("class", "loc-em-cr");
		var created_at_ = new Date(res.created_at).toString().split(" ");
		created_at.innerHTML = "created on "+created_at_[1]+" "+created_at_[2]+", "+created_at_[3];
		created_at.setAttribute("class", "loc-em-cr");
		$(".org-detail").append(location);
		$(".org-detail").append(email);
		$(".org-detail").append(created_at);
		var line = document.createElement("div");
		line.setAttribute("class", "line");
		$(".org-detail").append(line);
		*/
	});
}