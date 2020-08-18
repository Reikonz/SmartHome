function toggle_outlet(){
	$.ajax({
			type: 'GET',
			url: "toggle_outlet/",
			data: {"data": 1},
			success: function(response){				
			},
			error: function(response){
			}
		})
}
