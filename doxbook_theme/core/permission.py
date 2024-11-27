import frappe


def get_permission_query_conditions_account(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return
    filters = [["Branch Users", "user", "=", user],["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not len(branches) >= 1:
        return
    allowed_account = [
        frappe.db.escape(account.get("name"))
        for account in get_allowed_account(branches, user)
    ]
    if not len(allowed_account) >= 1:
        return
    if allowed_account:
        condition = """
            `tabAccount`.`name` in ({allowed_account})
        """.format(
            allowed_account=",".join(allowed_account)
        )
        return condition


def get_permission_query_conditions_warehouse(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return
    filters = [["Branch Users", "user", "=", user],["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not len(branches) >= 1:
        return
    allowed_warehouse = [
        frappe.db.escape(warehouse.get("name"))
        for warehouse in get_allowed_warehouse(branches, user)
    ]
    if not len(allowed_warehouse) >= 1:
        return
    if allowed_warehouse:
        condition = """
            `tabWarehouse`.`name` in ({allowed_warehouse})
        """.format(
            allowed_warehouse=",".join(allowed_warehouse)
        )
        return condition
    else:
        condition = """
            `tabWarehouse`.`name`='{user}'
        """.format(
            user=user
        )

        return condition

def get_permission_query_conditions_branch_customer_group(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return
    
    filters = [["Branch Users", "user", "=", user], ["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not branches:
        print("No branches found for user:", user)  
        return

    allowed_customer_group = [
        frappe.db.escape(customer_group['name'])
        for customer_group in allowed_branch_customer_group(branches, user)
    ]
    
    if not allowed_customer_group:
        print("No allowed customer groups found for user:", user)  
        return

    condition = """
        `tabCustomer Group`.`name` in ({allowed_customer_group})
    """.format(
        allowed_customer_group=",".join(allowed_customer_group)
    )
    
    print("Condition:", condition)  
    return condition

def get_permission_query_conditions_employee_group(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return

    filters = [["Branch Users", "user", "=", user], ["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not branches:
        print("No branches found for user:", user)
        return

    allowed_employee_group = [
        frappe.db.escape(employee_group['name'])
        for employee_group in allowed_branch_employee_group(branches, user)
    ]

    if not allowed_employee_group:
        print("No allowed employee groups found for user:", user)
        return

    condition = """
        `tabEmployee Group`.`name` in ({allowed_employee_group})
    """.format(
        allowed_employee_group=",".join(allowed_employee_group)
    )
    
    print("Condition:", condition)
    return condition


def get_permission_query_conditions_supplier_group(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return

    filters = [["Branch Users", "user", "=", user], ["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not branches:
        print("No branches found for user:", user)
        return

    allowed_supplier_group = [
        frappe.db.escape(supplier_group['name'])
        for supplier_group in allowed_branch_supplier_group(branches, user)
    ]

    if not allowed_supplier_group:
        print("No allowed supplier groups found for user:", user)
        return

    condition = """
        `tabSupplier Group`.`name` in ({allowed_supplier_group})
    """.format(
        allowed_supplier_group=",".join(allowed_supplier_group)
    )
    
    print("Condition:", condition)
    return condition


def get_permission_query_conditions_item_group(user=None):
    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return

    roles = frappe.get_roles(user)
    if "System Manager" in roles:
        return

    filters = [["Branch Users", "user", "=", user], ["Branch", "name", "=", frappe.defaults.get_defaults().branch]]
    branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    if not branches:
        print("No branches found for user:", user)
        return

    allowed_item_group = [
        frappe.db.escape(item_group['name'])
        for item_group in allowed_branch_item_group(branches, user)
    ]

    if not allowed_item_group:
        print("No allowed item groups found for user:", user)
        return

    condition = """
        `tabItem Group`.`name` in ({allowed_item_group})
    """.format(
        allowed_item_group=",".join(allowed_item_group)
    )
    
    print("Condition:", condition)
    return condition


def get_allowed_account(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    # branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    accounts = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)

        default_table_details = [
            {
                "table_field_name": "branch_bank_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_cash_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_tax_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_income_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_cogs_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_direct_expense_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_indirect_income_account",
                "link_field_name": "account",
                "allow": "Account",
            },
            {
                "table_field_name": "branch_indirect_expense_account",
                "link_field_name": "account",
                "allow": "Account",
            },
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")
            # if len(self.get(table_field_name)) == 0:
            # 	clear_user_permissions(self,allow)

            # if len(self.get('user')) == 0:
            # 	clear_user_permissions(self,allow)

            for default_row in branch_doc.get(table_field_name):
                accounts.append(dict(name=default_row.get(link_field_name)))
    return accounts


def get_allowed_warehouse(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    # branches = frappe.get_all("Branch", filters=filters, fields=["name"])
    warehouses = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)

        default_table_details = [
            {
                "table_field_name": "branch_warehouse",
                "link_field_name": "warehouse",
                "allow": "Warehouse",
            }
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")
            # if len(self.get(table_field_name)) == 0:
            # 	clear_user_permissions(self,allow)

            # if len(self.get('user')) == 0:
            # 	clear_user_permissions(self,allow)

            for default_row in branch_doc.get(table_field_name):
                warehouses.append(dict(name=default_row.get(link_field_name)))
    return warehouses

def allowed_branch_customer_group(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    customer_groups = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)
        print(f"Processing branch: {branch.name}")  # Debug statement

        default_table_details = [
            {
                "table_field_name": "branch_customer_group",  # Adjust this to your actual table field name
                "link_field_name": "customer_group",
                "allow": "Customer Group",
            }
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")

            default_rows = branch_doc.get(table_field_name)
            if default_rows:
                for default_row in default_rows:
                    customer_groups.append(dict(name=default_row.get(link_field_name)))
                    print(f"Added customer group: {default_row.get(link_field_name)}")  # Debug statement
            else:
                print(f"No data found in table: {table_field_name} for branch: {branch.name}")  # Debug statement

    return customer_groups 
    
def allowed_branch_employee_group(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    employee_groups = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)
        print(f"Processing branch: {branch.name}")

        default_table_details = [
            {
                "table_field_name": "branch_employee_group",
                "link_field_name": "employee_group",
                "allow": "Employee Group",
            }
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")

            default_rows = branch_doc.get(table_field_name)
            if default_rows:
                for default_row in default_rows:
                    employee_groups.append(dict(name=default_row.get(link_field_name)))
                    print(f"Added employee group: {default_row.get(link_field_name)}")
            else:
                print(f"No data found in table: {table_field_name} for branch: {branch.name}")

    return employee_groups


def allowed_branch_supplier_group(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    supplier_groups = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)
        print(f"Processing branch: {branch.name}")

        default_table_details = [
            {
                "table_field_name": "branch_supplier_group",
                "link_field_name": "supplier_group",
                "allow": "Supplier Group",
            }
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")

            default_rows = branch_doc.get(table_field_name)
            if default_rows:
                for default_row in default_rows:
                    supplier_groups.append(dict(name=default_row.get(link_field_name)))
                    print(f"Added supplier group: {default_row.get(link_field_name)}")
            else:
                print(f"No data found in table: {table_field_name} for branch: {branch.name}")

    return supplier_groups


def allowed_branch_item_group(branches, user):
    filters = [["Branch Users", "user", "=", user]]
    item_groups = []
    for branch in branches:
        branch_doc = frappe.get_doc("Branch", branch.name)
        print(f"Processing branch: {branch.name}")

        default_table_details = [
            {
                "table_field_name": "branch_item_group",
                "link_field_name": "item_group",
                "allow": "Item Group",
            }
        ]
        for default_dict in default_table_details:
            table_field_name = default_dict.get("table_field_name")
            link_field_name = default_dict.get("link_field_name")

            default_rows = branch_doc.get(table_field_name)
            if default_rows:
                for default_row in default_rows:
                    item_groups.append(dict(name=default_row.get(link_field_name)))
                    print(f"Added item group: {default_row.get(link_field_name)}")
            else:
                print(f"No data found in table: {table_field_name} for branch: {branch.name}")

    return item_groups