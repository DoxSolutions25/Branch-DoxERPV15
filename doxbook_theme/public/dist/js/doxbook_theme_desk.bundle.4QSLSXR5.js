(()=>{frappe.templates.navbar=`<header class="navbar navbar-expand sticky-top dox-theme" role="navigation">
	<div class="container">
		<a href="javascript:history.back()" class="back-button"></a>
		<a class="navbar-brand navbar-home" href="/app">
			<img class="app-logo" style="width: {{ navbar_settings.logo_width || 24 }} px"
				src="{{ frappe.boot.app_logo_url }}">
		</a>
		<ul class="nav navbar-nav d-none d-sm-flex" id="navbar-breadcrumbs"></ul>
		<div class="collapse navbar-collapse justify-content-end">
			<form class="form-inline fill-width justify-content-end" role="search" onsubmit="return false;">
				{% if (frappe.boot.read_only) { %}
				<span class="indicator-pill yellow no-indicator-dot" title="{%= __(" Your site is getting upgraded.")
					%}">
					{%= __("Read Only Mode") %}
				</span>
				{% } %}
				<div class="input-group search-bar text-muted hidden">
					<input id="navbar-search" type="text" class="form-control" placeholder="{%= __(" Search or type a
						command (Ctrl + G)") %}" aria-haspopup="true">
					<span class="search-icon">
						<svg class="icon icon-sm">
							<use href="#icon-search"></use>
						</svg>
					</span>
				</div>
			</form>
			<ul class="navbar-nav">
				<li class="nav-item dropdown dropdown-language dropdown-mobile ness_lang">
					<a class="nav-link lang-icon" data-toggle="dropdown" href="#" onclick="return false;">
						<!-- <i class="fa fa-globe lang-icon"></i> -->
						<span id="current_lang"></span>
					</a>
					<div class="dropdown-menu dropdown-menu-right" id="toolbar-user" role="menu">
						<a class="dropdown-item" id="change_lang_en" href="#">
							English
						</a>
						<div class="dropdown-divider"></div>
						<a class="dropdown-item" href="#" id="change_lang_ar">
							<!-- onclick="return frappe.ui.toolbar.change_lang_ar()" -->
							Arabic
						</a>
					</div>
				</li>
				<li class="nav-item dropdown dropdown-notifications dropdown-mobile hidden">
					<a class="nav-link notifications-icon text-muted" data-toggle="dropdown" aria-haspopup="true"
						aria-expanded="true" href="#" onclick="return false;">
						<span class="notifications-seen">
							<svg class="icon icon-md">
								<use href="#icon-notification"></use>
							</svg>
						</span>
						<span class="notifications-unseen">
							<svg class="icon icon-md">
								<use href="#icon-notification-with-indicator"></use>
							</svg>
						</span>
					</a>
					<div class="dropdown-menu notifications-list dropdown-menu-right" role="menu">
						<div class="notification-list-header">
							<div class="header-items"></div>
							<div class="header-actions"></div>
						</div>
						<div class="notification-list-body">
							<div class="panel-notifications"></div>
							<div class="panel-events"></div>
						</div>
					</div>
				</li>
				<li class="nav-item dropdown dropdown-message dropdown-mobile hidden">
					<a class="nav-link notifications-icon text-muted" data-toggle="dropdown" aria-haspopup="true"
						aria-expanded="true" href="#" onclick="return false;">
						<span>
							<svg class="icon icon-md">
								<use href="#icon-small-message"></use>
							</svg>
						</span>
					</a>
				</li>
				<li class="vertical-bar d-none d-sm-block"></li>
				<li class="nav-item dropdown dropdown-help dropdown-mobile d-none d-lg-block">
					<a class="nav-link" data-toggle="dropdown" href="#" onclick="return false;">
						{{ __("Help") }}
						<span>
							<svg class="icon icon-xs">
								<use href="#icon-small-down"></use>
							</svg>
						</span>
					</a>
					<div class="dropdown-menu dropdown-menu-right" id="toolbar-help" role="menu">
						<div id="help-links"></div>
						<div class="dropdown-divider documentation-links"></div>
						{% for item in navbar_settings.help_dropdown %}
						{% if (!item.hidden) { %}
						{% if (item.route) { %}
						<a class="dropdown-item" href="{{ item.route }}">
							{%= __(item.item_label) %}
						</a>
						{% } else if (item.action) { %}
						<a class="dropdown-item" onclick="return {{ item.action }}">
							{%= __(item.item_label) %}
						</a>
						{% } else { %}
						<div class="dropdown-divider"></div>
						{% } %}
						{% } %}
						{% endfor %}
					</div>
				</li>
				<li class="nav-item dropdown dropdown-navbar-user dropdown-mobile">
					<a class="nav-link" data-toggle="dropdown" href="#" onclick="return false;">
						{{ avatar }}
					</a>
					<div class="dropdown-menu dropdown-menu-right" id="toolbar-user" role="menu">
						{% for item in navbar_settings.settings_dropdown %}
						{% if (!item.hidden) { %}
						{% if (item.route) { %}
						<a class="dropdown-item" href="{{ item.route }}">
							{%= __(item.item_label) %}
						</a>
						{% } else if (item.action) { %}
						<a class="dropdown-item" onclick="return {{ item.action }}">
							{%= __(item.item_label) %}
						</a>
						{% } else { %}
						<div class="dropdown-divider"></div>
						{% } %}
						{% } %}
						{% endfor %}
					</div>
				</li>
				<li class="nav-item" class="hidden-xs">
					<button type="button" id="change-branch-id" class="change-branch btn btn-info"
						data-toggle="dropdown">
						Change Branch
					</button>
				</li>
			</ul>
		</div>
	</div>
</header>`;frappe.standard_pages.Workspaces=function(){var a=frappe.container.add_page("Workspaces");frappe.ui.make_app_page({parent:a,name:"Workspaces",title:__("Workspace")}),frappe.workspace=new i(a),$(a).bind("show",function(){frappe.workspace.show()})};var i=class extends frappe.views.Workspace{sidebar_item_container(e){return $(`
			<div
				class="sidebar-item-container ${e.is_editable?"is-draggable":""}"
				item-parent="${e.parent_page}"
				item-name="${e.title}"
				item-public="${e.public||0}"
				item-is-hidden="${e.is_hidden||0}"
			>
				<div class="desk-sidebar-item standard-sidebar-item ${e.selected?"selected":""}">
					<a
						href="/app/${e.public?frappe.router.slug(e.title):"private/"+frappe.router.slug(e.title)}"
						class="item-anchor ${e.is_editable?"":"block-click"}" title="${__(e.title)}"
					>
                    
						<span class="sidebar-item-icon" item-icon=${e.icon||"folder-normal"}>
                        ${e.svg?'<img class="icon-md mr-2" src='+e.svg+" />":frappe.utils.icon(e.icon||"folder-normal","md")}
                        
                        
        </span>
						<span class="sidebar-item-label">${__(e.title)}<span>
					</a>
					<div class="sidebar-item-control"></div>
				</div>
				<div class="sidebar-child-item nested-container"></div>
			</div>
		`)}};function s(){let a=localStorage.getItem("set_session");parseInt(a)===1&&(n.show(),localStorage.setItem("set_session",0)),$(".change-branch").click(function(){n.show(),localStorage.setItem("set_session",0)});let e=document.getElementById("change-branch-id");frappe.defaults.get_default("branch")?e.innerText=frappe.defaults.get_default("branch"):e.innerText="Select Branch"}$(window).ready(s);var n=new frappe.ui.Dialog({title:"Please select your Current Branch",fields:[{label:"Branch",fieldname:"branch",fieldtype:"Link",options:"Branch"}],size:"small",primary_action_label:"Submit",primary_action(a){console.log(a.branch),o(a.branch),n.hide()}});function o(a){frappe.call({method:"frappe.core.doctype.session_default_settings.session_default_settings.set_session_default_values",args:{default_values:{branch:a}},callback:function(e){e.message=="success"?(frappe.show_alert({message:__("Current Branch Updated"),indicator:"green"}),frappe.ui.toolbar.clear_cache()):frappe.show_alert({message:__("An error occurred while setting your current branch"),indicator:"red"})}})}})();
//# sourceMappingURL=doxbook_theme_desk.bundle.4QSLSXR5.js.map
