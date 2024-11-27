import frappe
from frappe import _

@frappe.whitelist()
def get_workspace_sidebar_items():
    from frappe.desk.desktop import Workspace

    """Get list of sidebar items for the desk."""
    has_access = "Workspace Manager" in frappe.get_roles()

    # Don't get domain-restricted pages
    blocked_modules = frappe.get_doc("User", frappe.session.user).get_blocked_modules()
    blocked_modules.append("Dummy Module")

    filters = {
        "restrict_to_domain": ["in", frappe.get_active_domains()],
        "module": ["not in", blocked_modules],
    }

    if has_access:
        filters = []  # If the user has access, ignore domain restrictions

    # Pages sorted based on sequence id
    order_by = "sequence_id asc"
    fields = [
        "name",
        "title",
        "for_user",
        "parent_page",
        "content",
        "public",
        "module",
        "icon",
        "is_hidden",
    ]
    all_pages = frappe.get_all(
        "Workspace",
        fields=fields,
        filters=filters,
        order_by=order_by,
        ignore_permissions=True,
    )

    pages = []
    private_pages = []

    # Filter pages based on permission
    for page in all_pages:
        try:
            workspace = Workspace(page)  # Initialize without 'load_content'
            if has_access or workspace.is_permitted():
                if page.public and (has_access or not page.is_hidden):
                    pages.append(page)
                elif page.for_user == frappe.session.user:
                    private_pages.append(page)
                page["label"] = _(page.get("name"))
        except frappe.PermissionError:
            pass

    if private_pages:
        pages.extend(private_pages)

    return {"pages": pages, "has_access": has_access}

@frappe.whitelist()
def get_lang():
    """Return the current language setting for the user."""
    return frappe.local.lang  # Return the current language
