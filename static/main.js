// ----- custom js ----- //

// hide initial
$("#searching").hide();
$("#results-table").hide();
$("#error").hide();

// global
var url = 'http://127.0.0.1:5000/uploads/'
var data ="";

$(function() {

  // sanity check
  console.log( "ready!" );

  // image click
  $(".img").click(function() {

    // empty/hide results
    $("#results").empty();
    $("#results-table").hide();
    $("#error").hide();

    // remove active class
    $(".img").removeClass("active")

    // add active class to clicked picture
    $(this).addClass("active")

    // grab image url
    var image = $(this).attr("src")
    console.log(image)

    // show searching text
    $("#searching").show();
    console.log("searching...")

    // ajax request
    $.ajax({
      type: "POST",
      url: "/search",
      data : { img : image },
      // handle success
      success: function(result) {
        console.log(result.results);
        var data = result.results
        // show table
        $("#results-table").show();
        // loop through results, append to dom
        
        $("#results").append('<tr><th>'+data+'</th></tr>')
        
      },
      // handle error
      error: function(error) {
        
        console.log(error);
        // append to dom
        $("#error").append()
      }
    });

  });

});