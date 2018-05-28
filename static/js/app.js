$(function() {

  if (localStorage.menuState=="0"){
    $(".app-container").addClass("expanded");
  } else {
    $(".app-container").removeClass("expanded");
  }
  $(".navbar-expand-toggle").click(function() {
    if (localStorage.menuState=="0"){
      localStorage.menuState = "1";
    } else {
      localStorage.menuState = "0";
    }
    $(".app-container").toggleClass("expanded");
    return $(".navbar-expand-toggle").toggleClass("fa-rotate-90");
  });
  return $(".navbar-right-expand-toggle").click(function() {
    $(".navbar-right").toggleClass("expanded");
    return $(".navbar-right-expand-toggle").toggleClass("fa-rotate-90");
  });
});

$(function() {
  return $('.toggle-checkbox').bootstrapSwitch({
    size: "small"
  });
});

$(function() {
  return $('.match-height').matchHeight();
});

$(function() {
  return $(".side-menu .nav .dropdown").on('show.bs.collapse', function() {
    return $(".side-menu .nav .dropdown .collapse").collapse('hide');
  });
});
