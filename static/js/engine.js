$('#category-search-form').hide();
$('#name-search-form').hide();
$('#person_search').hide();
$('#business_search').hide();
$(".results").hide();

$('.do_not_hide').show();

$("#person_button").click(function(event) {
  $("#person_search").show();
  $("#business_search").hide();
});

$("#business_button").click(function(event) {
  $("#business_search").show();
  $("#person_search").hide();
  });


$("#name_button").click(function(event) {
  $("#name-search-form").show();
  $("#category-search-form").hide();
  });

$("#category_button").click(function(event) {
  $("#category-search-form").show();
  $("#name-search-form").hide();
  });

function ScrollToPersonSearch() {
var elmnt = document.getElementById("person_search");
elmnt.scrollIntoView();
}

function ScrollToBusinessSearch() {
var elmnt = document.getElementById("business_search");
elmnt.scrollIntoView();
}


$(".move-area").mousemove(function(event) {
  var eye = $(".eye");
  var x = (eye.offset().left) + (eye.width() / 2);
  var y = (eye.offset().top) + (eye.height() / 2);
  var rad = Math.atan2(event.pageX - x, event.pageY - y);
  var rot = (rad * (180 / Math.PI) * -1) + 180;
  eye.css({
    '-webkit-transform': 'rotate(' + rot + 'deg)',
    '-moz-transform': 'rotate(' + rot + 'deg)',
    '-ms-transform': 'rotate(' + rot + 'deg)',
    'transform': 'rotate(' + rot + 'deg)'
  });
});

function SearchSummaryReveal() {
  $(".results").show();
}

object.onsubmit = function(){SearchSummaryReveal};
