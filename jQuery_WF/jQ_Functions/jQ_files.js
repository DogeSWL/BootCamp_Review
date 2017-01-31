$(document).ready(function() {
  $('#addClassB').click(function() {
    $('#redP').addClass('turnRed');
  })

  $('#slideTogB').click(function() {
    $('#sTogHere').slideToggle('slow');
  })

  $('#appendB').click(function() {
    $('#appendSection').append('<p>A new paragraph</p>');
  })
})
