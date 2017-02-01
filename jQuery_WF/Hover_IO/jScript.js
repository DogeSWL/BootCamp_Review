function numCheck(num) {
  if(num==1) {
    return "<img src='img/git4.jpg'>";
  }
  if(num==2) {
    return "<img src='img/git5.jpg'>";
  }
  if(num==3) {
    return "<img src='img/git6.png'>";
  }
  if(num==4) {
    return "<img src='img/git1.png'>";
  }
  if(num==5) {
    return "<img src='img/git2.png'>";
  }
  if(num==6) {
    return "<img src='img/git3.png'>";
  }
};

$(document).ready(function() {

  $('img').hover(function() {
    $(this).replaceWith(numCheck($(this).attr('data-alt-src')));
  }, function() {
    $(this).replaceWith(numCheck($(this).attr('data-alt-src')));
  });

});
