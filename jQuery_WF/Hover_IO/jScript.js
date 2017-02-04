$(document).ready(function() {

  $('img').hover(function() {
    $(this).attr('src', $(this).attr('alt-src'));
    }, function() {
    $(this).attr('src', $(this).attr('default-src')) ;
    }
  );

});
