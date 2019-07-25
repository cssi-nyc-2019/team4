var limit = 5;
$('input.single-checkbox').on('change', function(evt) {
   if($(this).genres(':checked').length >= limit) {
       this.checked = false;
   }
});