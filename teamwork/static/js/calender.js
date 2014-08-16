function addFields(){
	var months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", 
	"Oct", "Nov", "Dec"];
	var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	var colors = ["#eee", "#d6e685", "#8cc665", "#44a340", "#1e6823"];
	var current_month = new Date().getMonth() + 1;
	// var current_date = new Date().getDate() % 7;
	var extraDay = 5;

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
			subField.setAttribute("style", "background:"+colors[Math.floor(Math.random()*4)]);
			document.getElementById("vert"+i).appendChild(subField);
		}
	}
}

function loadXMLDoc(org){
	var xmlhttp;
	if(window.XMLHttpRequest){
	// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
	else{// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function(){
		if(xmlhttp.readyState==4 && xmlhttp.status==200){
			return xmlhttp.responseText;
		}
	}
	xmlhttp.open("POST","orgDesc",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("org="+org);
}