function initialize() {
  $("#change_lang_en").click(() => {
    // frappe.call("frappe.translate.set_preferred_language_cookie", {
    //   preferred_language: "en"
    // }).then(function () { location.reload() })
    document.cookie = `preferred_language=en`;
    window.location.reload();
  });

  $("#change_lang_ar").click(() => {
    // frappe.call("frappe.translate.set_preferred_language_cookie", {
    //   preferred_language: "ar"
    // }).then(function () { location.reload() })
    document.cookie = `preferred_language=ar`;
    window.location.reload();
  });

  var preferred_language = frappe.get_cookie("preferred_language");
  if (preferred_language) {
    if (preferred_language == "ar") {
      $(".language-switcher-image").attr(
        "src",
        "/assets/doxbook_theme/images/ar.png"
      );
      $("#change_lang_ar").hide();
    } else if (preferred_language == "en") {
      $(".language-switcher-image").attr(
        "src",
        "/assets/doxbook_theme/images/en.png"
      );
      $("#change_lang_en").hide();
    } else {
      $(".language-switcher-image").attr(
        "src",
        "/assets/doxbook_theme/images/en.png"
      );
    }
  } else {
    // frappe.call("frappe.translate.set_preferred_language_cookie", {
    //   preferred_language: "en"
    // });
    // $(".language-switcher-image").attr("src", "/assets/doxbook_theme/images/en.png");
    // $('#change_lang_en').hide();
    document.cookie = `preferred_language=ar`;
    window.location.reload();
  }
}

$(window).ready(initialize);

// function initialize() {

//   $('#change_lang_en').click(() => {
//     frappe.call("frappe.translate.set_preferred_language_cookie", {
//       preferred_language: "en"
//     }).then(function () { location.reload() })
//   });

//   $('#change_lang_ar').click(() => {
//     frappe.call("frappe.translate.set_preferred_language_cookie", {
//       preferred_language: "ar"
//     }).then(function () { location.reload() })
//   });

//   var preferred_language = frappe.get_cookie("preferred_language");
//   if (preferred_language) {
//     if (preferred_language == "ar") {
//       $(".language-switcher-image").attr("src", "/assets/doxbook_theme/images/ar.png");
//       $('#change_lang_ar').hide();
//     }
//     else if (preferred_language == "en") {
//       $(".language-switcher-image").attr("src", "/assets/doxbook_theme/images/en.png");
//       $('#change_lang_en').hide();
//     }
//     else {
//       $(".language-switcher-image").attr("src", "/assets/doxbook_theme/images/en.png");
//     }
//   } else {
//     frappe.call("frappe.translate.set_preferred_language_cookie", {
//       preferred_language: "ar"
//     });
//     $(".language-switcher-image").attr("src", "/assets/doxbook_theme/images/ar.png");
//     $('#change_lang_en').hide();
//   }

// }

// $(window).ready(initialize)
