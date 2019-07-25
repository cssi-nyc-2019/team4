functobject.onclick = function(){myScript};

function checkBoxLimit() {
	var checkBoxGroup = document.forms['Genres']['check[]'];			
	var limit = 5;
	for (var i = 0; i < checkBoxGroup.length; i++) {
		checkBoxGroup[i].onclick = function() {
			var checkedcount = 0;
			for (var i = 0; i < checkBoxGroup.length; i++) {
				checkedcount += (checkBoxGroup[i].checked) ? 1 : 0;
			}
			if (checkedcount > limit) {
				console.log("Please Select " + limit + " checkboxes.");
				alert("Please Select " + limit + " checkboxes.");						
				this.checked = false;
				
			}else if (checkedcount < limit) {
				console.log("You may only select atleast 5 boxes");
				alert("You may only select atlest 5 boxes")

			}
		}
	}
}