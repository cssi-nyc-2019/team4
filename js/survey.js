$("input:checkbox").click(function() {
var bol = $("input:checkbox:checked").length >= 2;     
$("input:checkbox").not(":checked").attr("disabled",bol);
});