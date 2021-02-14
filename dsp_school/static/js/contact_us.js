(function($) {
  "use strict"; // Start of use strict

  // Detect when form-control inputs are not empty
  $(".cool-b4-form .form-control").on("input", function() {
    if ($(this).val()) {
      $(this).addClass("hasValue");
    } else {
      $(this).removeClass("hasValue");
    }
  });
})(jQuery); // End of use strict