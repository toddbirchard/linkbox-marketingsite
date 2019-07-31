$(document).ready(function() {
  var response = $('#code code').html();
  if (response) {
    $('#code code').css('display', 'block');
    console.log('response = ' + response);
    console.log('response.length = ' + response.length);
  }
});
