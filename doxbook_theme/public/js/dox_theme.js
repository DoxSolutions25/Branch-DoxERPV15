function initialize() {
  $("#change_lang_en").click(() => {
    frappe.call({
      method: "doxbook_theme.utils.change_lang",
      args: {
        language: "en",
      },
      callback: function (result) {
        if (result.message === true) {
          frappe.msgprint(__("Switching Language..."));
          frappe.ui.toolbar.clear_cache();
        }
      },
    });
  });

  $("#change_lang_ar").click(() => {
    frappe.call({
      method: "doxbook_theme.utils.change_lang",
      args: {
        language: "ar",
      },
      callback: function (result) {
        if (result.message === true) {
          frappe.msgprint(__("Switching Language..."));
          frappe.ui.toolbar.clear_cache();
        }
      },
    });
  });

  frappe.call({
    method: "doxbook_theme.utils.get_lang",
    callback: function (result) {
      if (result.status_code === 200) {
        if (result.data == "en") $("#current_lang").html("English");
        else if (result.data == "ar") $("#current_lang").html("Arabic");
      }
    },
  });

  // frappe.provide("frappe.view.Workspace");
  // frappe.views.Workspace = frappe.views.Workspace.extend({
  //   sidebar_item_container(item) {
  //     console.log('Hello from extend taxes and total extend !!');
  //   }
  // });
  // $.extend(frappe.view.workspace, {
  //   sidebar_item_container(item) {
  //     console.log('Hello from extend taxes and total extend !!');
  //     return $(`
  //         <div class="sidebar-item-container ${item.is_editable ? "is-draggable" : ""}" item-parent="${item.parent_page
  //       }" item-name="${item.title}" item-public="${item.public || 0}">
  //           <div class="desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""}">
  //             <a
  //               href="/app/${item.public
  //         ? frappe.router.slug(item.title)
  //         : "private/" + frappe.router.slug(item.title)
  //       }"
  //               class="item-anchor ${item.is_editable ? "" : "block-click"}" title="${__(item.title)}"
  //             >
  //               <span class="sidebar-item-icon" item-icon=${item.icon || "folder-normal"}>${frappe.utils.icon(
  //         item.icon || "folder-normal",
  //         "md"
  //       )}</span>
  //               <span class="sidebar-item-label">${__(item.title)}<span>
  //             </a>
  //             <div class="sidebar-item-control"></div>
  //           </div>
  //           <div class="sidebar-child-item nested-container"></div>
  //         </div>
  //       `);
  //   }
  // });
}

$(window).ready(initialize);