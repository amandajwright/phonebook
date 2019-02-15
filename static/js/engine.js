$("#person_search").hide();
$("#business_search_btns").hide();
$("#business_name_search").hide();
$("#business_category_search").hide();
$(".results").hide();

$(".do_not_hide").show();

function scrollToPersonSearch() {
var elmnt = document.getElementById("person_search");
elmnt.scrollIntoView();
}

function scrollToBusinessSearchBtns() {
var elmnt = document.getElementById("business_search_btns");
elmnt.scrollIntoView();
}

function scrollToBusinessNameSearch() {
var elmnt = document.getElementById("business_name_search");
elmnt.scrollIntoView();
}

function scrollToBusinessCategorySearch() {
var elmnt = document.getElementById("business_category_search");
elmnt.scrollIntoView();
}

$("#search_by_person_btn").click(function(event) {
  $("#person_search").show();
  $("#business_search_btns").hide();
  $("#business_name_search").hide();
  $("#business_category_search").hide();
  scrollToPersonSearch()
});

$("#search_by_business_btn").click(function(event) {
  $("#business_search_btns").show();
  $("#person_search").hide();
  scrollToBusinessSearchBtns()
  });

$("#search_by_biz_name_btn").click(function(event) {
  $("#business_name_search").show();
  $("#business_category_search").hide();
  scrollToBusinessNameSearch();
  });

$("#search_by_biz_category_btn").click(function(event) {
  $("#business_category_search").show();
  $("#business_name_search").hide();
  scrollToBusinessCategorySearch();
  });

$("#switch_to_biz_category_search").click(function(event) {
  $("#business_category_search").show();
  $("#business_name_search").hide();
  $("#business_name_search_results").hide();
  scrollToBusinessCategorySearch();
  });

$("#switch_to_biz_name_search").click(function(event) {
  $("#business_name_search").show();
  $("#business_category_search").hide();
  $("#business_category_search_results").hide();
  scrollToBusinessNameSearch();
  });

// function ScrollToPersonResults() {
// var elmnt = document.getElementById("person_search_results");
// elmnt.scrollIntoView();
// }
//
// function SearchSummaryReveal() {
//   $(".results").show();
//   ScrollToPersonResults();
// }
//
// object.onsubmit = function(){SearchSummaryReveal};
