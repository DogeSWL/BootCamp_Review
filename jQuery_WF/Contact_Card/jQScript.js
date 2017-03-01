$(document).ready(function() {

  $("form").submit(function() {
    $(".rightContainer").append('<div class=cardBox><h1>'+
    addForm.firstName.value+' '+addForm.lastName.value+'</h1><h4>Click for description!</h4><h3>'+
    addForm.desBox.value+'</h3></div>');

    //adds event listener to element
    $(".cardBox").on("click", function() {
      $(this).children().toggle();;
    });

    //reset the form after submitting
    $("form")[0].reset();

    return false;
  });

  //click on cardBox class will cause element to toggle
  $(".cardBox").click(function() {
    $(this).children().toggle();;
  });

});
