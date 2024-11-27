from __future__ import unicode_literals
import frappe
import json
from frappe.utils import floor, flt, today, cint
from frappe import _


@frappe.whitelist()
def dox_patch():
    # delete erpnext welcome page
    frappe.delete_doc_if_exists("Page", "welcome-to-erpnext", force=1)
    # update Welcome Blog Post
    if frappe.db.exists("Blog Post", "Welcome"):
        frappe.db.set_value("Blog Post", "Welcome", "content", "")
    create_custom_field_doxerp()
    remove_onboard_module()
    # update_app_logo()


def remove_onboard_module():
    frappe.db.sql("""update `tabModule Onboarding` set documentation_url=null""")
    frappe.db.sql("""update `tabModule Onboarding` set is_complete=1""")

    frappe.db.sql(
        """update `tabOnboarding Step` set intro_video_url=null,description=null"""
    )
    frappe.db.sql(
        """update `tabOnboarding Step` set intro_video_url=null,description=null"""
    )


def update_app_logo():
    web_doc = frappe.get_doc("Website Settings")
    # update homepage to login page
    web_doc.home_page = "login"
    # hide footer email subscribe form
    web_doc.hide_footer_signup = 1
    # rename login form app name
    web_doc.app_name = "DOXERP"
    web_doc.app_logo = "/assets/doxbook_theme/images/dox_logo.png"
    web_doc.splash_image = "/assets/doxbook_theme/images/dox business logo_ 3.png"
    web_doc.flags.ignore_mandatory = True
    web_doc.save(ignore_permissions=True)
    nav_doc = frappe.get_doc("Navbar Settings")
    nav_doc.app_logo = "/assets/doxbook_theme/images/dox_logo.png"
    nav_doc.flags.ignore_mandatory = True
    nav_doc.save(ignore_permissions=True)


def create_custom_field_doxerp():
    from frappe.custom.doctype.custom_field.custom_field import create_custom_field

    custom_fields = [
        {
            "fieldname": "svg",
            "label": "SVG",
            "fieldtype": "Attach",
        }
    ]
    for df in custom_fields:
        if not frappe.db.exists(
            "Custom Field", {"fieldname": df.get("fieldname"), "dt": "Workspace"}
        ):
            create_custom_field("Workspace", df=df)
