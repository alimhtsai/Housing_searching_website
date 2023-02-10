$(document).ready(function(){
  
  $(".buy a").click(function(){
    $(this).addClass("active");
    $(".rent a").removeClass("active");
  });

  $(".rent a").click(function(){
    $(this).addClass("active");
    $(".buy a").removeClass("active");
  });

  $("#filter-1").click(function(){
    $("#filter-2.active").toggleClass("active");
    $("#filter-3.active").toggleClass("active");
    $(".sort.active").removeClass("active");
    $(this).toggleClass("active");
  });

  $("#filter-2").click(function(){
    $("#filter-1.active").toggleClass("active");
    $("#filter-3.active").toggleClass("active");
    $(".sort.active").removeClass("active");
    $(this).toggleClass("active");
  });

  $("#filter-3").click(function(){
    $("#filter-1.active").toggleClass("active");
    $("#filter-2.active").toggleClass("active");
    $(".sort.active").removeClass("active");
    $(this).toggleClass("active");
  });

  $(".sort").click(function(){
    $(".condition.active").removeClass("active");
    $(this).toggleClass("active");
  });

  $(".save").click(function(){
    $(this).toggleClass("active");
  });

  $(".select a").click(function(){
    $(".select a.active").removeClass("active");
    $(this).toggleClass("active");
    $(".condition").removeClass("active");
    $(".sort").removeClass("active");
  });

  $(".delete a").click(function(){
    $(".select a").removeClass("active");
  });

});

function goBack() {
  window.history.back();
}