import "./ui/toolbar/navbar.html";
// TaxesAndTotalsExtend is just variable name
// erpnext.taxes_and_totals is function contain function you want to override

// const TaxesAndTotalsExtend = frappe.workspace.extend({
// });
// console.log("hello from dox")
// frappe.provide("frappe.view.Workspace");
// frappe.views.Workspace.extend({
//     sidebar_item_container(item) {
//         console.log('Hello from extend taxes and total extend !!');
//     }
// });

frappe.standard_pages["Workspaces"] = function () {
  var wrapper = frappe.container.add_page("Workspaces");

  frappe.ui.make_app_page({
    parent: wrapper,
    name: "Workspaces",
    title: __("Workspace"),
  });

  frappe.workspace = new Custom_Workspace(wrapper);
  $(wrapper).bind("show", function () {
    frappe.workspace.show();
  });




};

class Custom_Workspace extends frappe.views.Workspace {
  
  sidebar_item_container(item) {
    
    return $(`
			<div
				class="sidebar-item-container ${item.is_editable ? "is-draggable" : ""}"
				item-parent="${item.parent_page}"
				item-name="${item.title}"
				item-public="${item.public || 0}"
				item-is-hidden="${item.is_hidden || 0}"
			>
				<div class="desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""
      }">
					<a
						href="/app/${item.public
        ? frappe.router.slug(item.title)
        : "private/" + frappe.router.slug(item.title)
      }"
						class="item-anchor ${item.is_editable ? "" : "block-click"}" title="${__(
        item.title
      )}"
					>
                    
						<span class="sidebar-item-icon" item-icon=${item.icon || "folder-normal"}>
                        ${item.svg
        ? '<img class="icon-md mr-2" src=' +
        item.svg +
        " />"
        : frappe.utils.icon(
          item.icon || "folder-normal",
          "md"
        )
      }
                        
                        
        </span>
						<span class="sidebar-item-label">${__(item.title)}<span>
					</a>
					<div class="sidebar-item-control"></div>
				</div>
				<div class="sidebar-child-item nested-container"></div>
			</div>
		`);
  }

  // constructor(wrapper) {
  //   // this.wrapper = $(wrapper);
  //   this.prepare_container();
  // }

}


function initialize() {

  let set_session = localStorage.getItem("set_session");
  if (parseInt(set_session) === 1) {
      d.show();
      localStorage.setItem("set_session", 0);
  }   

  $(".change-branch").click(function(){
      d.show();
      localStorage.setItem("set_session", 0);  
  })
  
  const btn = document.getElementById("change-branch-id");
  if (frappe.defaults.get_default("branch")) {
      btn.innerText = frappe.defaults.get_default("branch")
  }else{
      btn.innerText = "Select Branch"
  }
  
}

$(window).ready(initialize)

let d = new frappe.ui.Dialog({
  title: 'Please select your Current Branch',
  fields: [
      {
          label: 'Branch',
          fieldname: 'branch',
          fieldtype: 'Link',
          options:"Branch"
      },
  ],
  size: 'small', // small, large, extra-large 
  primary_action_label: 'Submit',
  primary_action(values) {
      console.log(values.branch);
      update_session_default(values.branch)
      d.hide();
  }
});


function update_session_default(branch) {
  frappe.call({
    method: "frappe.core.doctype.session_default_settings.session_default_settings.set_session_default_values",
    args: {
      default_values: {"branch": branch},
    },
    callback: function (data) {
      if (data.message == "success") {
        frappe.show_alert({
          message: __("Current Branch Updated"),
          indicator: "green",
        });
        frappe.ui.toolbar.clear_cache();
      } else {
        frappe.show_alert({
          message: __(
            "An error occurred while setting your current branch"
          ),
          indicator: "red",
        });
      }
    },
  });
}
