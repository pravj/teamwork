function addFields(){
	var months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", 
	"Oct", "Nov", "Dec"]
	current_month = new Date().getMonth() + 1,
	extraDay = 5, url = "/calender";

	/*All varialbes*/
	var longest_streak_range,
	current_streak_range,
	total_streak_range,
	longest_streak_range_from,
	longest_streak_range_to,
	current_streak_range_from,
	current_streak_range_to,
	total_streak_range_from,
	total_streak_range_to,
	total_commits,
	longest_streak,
	current_streak,
	max_commit=0;

	/*HTML variables*/
	var contrib_day,
	longest_streak_div,
	date_range_for_longest_streak,
	current_streak_div,
	date_range_for_current_streak,
	date_range_for_total_streak;

	$.ajax({url: url}).done(function(res){
		res = JSON.parse(res)[0];
		longest_streak_range = res.longest_streak_range.split(" - ");
		longest_streak_range_from = months[parseInt(longest_streak_range[0].split("-")[1])]+'-'+longest_streak_range[0].split("-")[2]+'-'+longest_streak_range[0].split("-")[0];
		longest_streak_range_to = months[parseInt(longest_streak_range[1].split("-")[1])]+'-'+longest_streak_range[1].split("-")[2]+'-'+longest_streak_range[1].split("-")[0];
		current_streak_range = res.current_streak_range.split(" - ");
		current_streak_range_from = months[parseInt(current_streak_range[0].split("-")[1])]+'-'+current_streak_range[0].split("-")[2]+'-'+current_streak_range[0].split("-")[0];
		current_streak_range_to = months[parseInt(current_streak_range[1].split("-")[1])]+'-'+current_streak_range[1].split("-")[2]+'-'+current_streak_range[1].split("-")[0];
		total_streak_range = res.total_streak_range.split(" - ");
		total_streak_range_from = months[parseInt(total_streak_range[1].split("-")[1])]+'-'+total_streak_range[1].split("-")[2]+'-'+total_streak_range[1].split("-")[0];
		total_streak_range_to = months[parseInt(total_streak_range[1].split("-")[1])]+'-'+total_streak_range[1].split("-")[2]+'-'+total_streak_range[1].split("-")[0];
		total_commits = res.total;
		longest_streak = res.longest_streak;
		current_streak = res.current_streak;

		for(var i=0;i<366;i++){
			if(max_commit < res.contributions[i][1])
				max_commit = res.contributions[i][1];
		}

		/*Months on top*/
		for(var i=current_month;i<current_month+12;i++){
		var monthField = document.createElement("div");
		monthField.setAttribute("class", "month");
		monthField.setAttribute("style", "transform: translate("+67*(i - current_month)+"px,"+(-15)*(i - current_month)+"px);");
		if(i>=12)
		monthField.innerHTML = months[i-12];
		else
		monthField.innerHTML = months[i];
		$(".months").append(monthField);}

		/*Contribution details.*/

		/*setting total commits*/
		contrib_day = document.createElement("div");
		contrib_day.setAttribute("class", "lbl1");
		contrib_day.innerHTML = total_commits+ " total";
		$(".contrib-day").append(contrib_day);
		/*total commits set*/

		date_range_for_total_streak = document.createElement("div");
		date_range_for_total_streak.innerHTML = total_streak_range_from+" - "+total_streak_range_to;
		date_range_for_total_streak.setAttribute("class", "lbl1");
		$(".contrib-day").append(date_range_for_total_streak);

		longest_streak_div = document.createElement("div");
		longest_streak_div.setAttribute("class", "lbl1");
		longest_streak_div.innerHTML = longest_streak+" days";
		$(".longest-streak").append(longest_streak_div);

		date_range_for_longest_streak = document.createElement("div");
		date_range_for_longest_streak.innerHTML = longest_streak_range_from+" - "+longest_streak_range_to;
		date_range_for_longest_streak.setAttribute("class", "lbl1");
		$(".longest-streak").append(date_range_for_longest_streak);

		current_streak_div = document.createElement("div");
		current_streak_div.setAttribute("class", "lbl1");
		current_streak_div.innerHTML = current_streak+" days";
		$(".current-streak").append(current_streak_div);

		date_range_for_current_streak = document.createElement("div");
		date_range_for_current_streak.innerHTML = current_streak_range_from+" - "+current_streak_range_to;
		date_range_for_current_streak.setAttribute("class", "lbl1");
		$(".current-streak").append(date_range_for_current_streak);

		for(var i=0;i<7;i++){
		var subField = document.createElement("div");
		subField.setAttribute("id", "square");
		if(i< extraDay){
		subField.setAttribute("style", "visibility:hidden;");}
		else{
		subField.setAttribute("class", "hint--left");
		subField.setAttribute("data-hint", res.contributions[i-5][1]+" Contributions on "+res.contributions[i-5][0]);
		subField.setAttribute("style", "background:"+get_color(res.contributions[i-5][1], max_commit));}
		document.getElementById("vert").appendChild(subField);}

		/*Remaining days*/
		for(var i=1; i<53;i++){
		var field = document.createElement("div");
		field.setAttribute("id", "vert"+i);
		var y_ = (-105)*(i);
		field.setAttribute("style", "transform : translate("+15*(i)+"px, "+y_+"px); width: 13px; ");
		$(".contrib").append(field);
		for(var j=1; j<=7;j++){
		if((7*i)+j >= 366)
		break;
		var subField = document.createElement("div");
		subField.setAttribute("id", "square");
		subField.setAttribute("class", "hint--left");
		subField.setAttribute("data-hint", res.contributions[(7*i)+j][1]+" Contributions on "+res.contributions[(7*i)+j][0]);
		subField.setAttribute("style", "background:"+get_color(res.contributions[(7*i)+j][1], max_commit));
		document.getElementById("vert"+i).appendChild(subField);}}
	});
}

function get_color(commit, max_commit){
	var colors = ["#eee", "#d6e685", "#8cc665", "#44a340", "#1e6823"];
	if(commit == 0)
		return colors[0];
	else if(commit < max_commit/4)
		return colors[1];
	else if(commit < max_commit/2)
		return colors[2];
	else if(commit < (3*max_commit)/4)
		return colors[3];
	else
		return colors[4];
}
