$(document).ready(function() {

  //generates random numbers to choose which pictures to return
  function genPic() {
    var ranNum1 = Math.floor(Math.random() * 2)+1;
    var ranNum2 = Math.floor(Math.random() * 5);

    if(ranNum1 == 2) {
      return "<img src='img/cat"+ranNum2+".png'>";
    }else {
      return "<img src='img/ninja"+ranNum2+".png'>";
    }
  };

  //creates 5 div boxes and append it to container div
  //genPic function adds img into div box as it is created
  for(var i=0; i<5; i++) {
    var aDiv = document.createElement('div');
    aDiv.className = 'aBlock';
    container.appendChild(aDiv);
    aDiv.innerHTML = genPic();
  };

  //on click changes img *problem: only able to change once*
  $('img').click(function() {
    $(this).replaceWith(genPic());
  });
});
