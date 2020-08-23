function toggle_outlet(){
	var outlet = document.getElementById("office");
	var class_list = outlet.classList.toString();	
	if (class_list.includes("on")){
		outlet.classList.remove("on");
		$.ajax({
			type: 'GET',
			url: "toggle_outlet/",
			data: {"command": "off"},
			success: function(response){				
			},
			error: function(response){
			}
		})
	}else{	
		outlet.classList.add("on");
		$.ajax({
			type: 'GET',
			url: "toggle_outlet/",
			data: {"command": "on"},
			success: function(response){				
			},
			error: function(response){
			}
		})
	}
}
