$(document).ready(function() {
  for(var i=0; i<8; i++) {
    var innerDiv = document.createElement('div');
    innerDiv.className = 'aBlock';

    permGrids.appendChild(innerDiv);
    innerDiv.innerHTML = "<img src='octobiwan.jpg'>";
  }
  
  $('img').click(function() {
    $(this).hide();
  });

  $('#restoreBtn').click(function() {
    $('img').show();
  });
})
