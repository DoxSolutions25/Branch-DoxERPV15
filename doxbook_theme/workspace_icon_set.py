import frappe


@frappe.whitelist()
def update_workspace_images():
    data = [
      # {"Sr": 1, "ID": "Settings", "SVG": ""},
      #   {"Sr": 2, "ID": "Build", "SVG": ""},
      #   {"Sr": 3, "ID": "Integrations", "SVG": ""},
      #   {"Sr": 4, "ID": "Retail", "SVG": "/assets/doxbook_theme/images/retails.svg"},
      #   {
      #       "Sr": 5,
      #       "ID": "ERPNext Settings",
      #       "SVG": "/assets/doxbook_theme/images/Setting.svg",
      #   },
      #   {
      #       "Sr": 6,
      #       "ID": "Salespeople",
      #       "SVG": "/assets/doxbook_theme/images/salespeopleandbranches.svg",
      #   },
      #   {"Sr": 7, "ID": "Website", "SVG": "/assets/doxbook_theme/images/website.svg"},
      #   {
      #       "Sr": 8,
      #       "ID": "ERPNext Integrations",
      #       "SVG": "/assets/doxbook_theme/images/Integration.svg",
      #   },
      #   {
      #       "Sr": 9,
      #       "ID": "Customization",
      #       "SVG": "/assets/doxbook_theme/images/customization.svg",
      #   },
      #   {"Sr": 10, "ID": "Utilities", "SVG": ""},
      #   {"Sr": 11, "ID": "Users", "SVG": "/assets/doxbook_theme/images/User.svg"},
      #   {"Sr": 12, "ID": "Tools", "SVG": "/assets/doxbook_theme/images/Tools.svg"},
      #   {"Sr": 13, "ID": "Support", "SVG": "/assets/doxbook_theme/images/Support.svg"},
      #   {
      #       "Sr": 14,
      #       "ID": "Manufacturing",
      #       "SVG": "/assets/doxbook_theme/images/manufacturer.svg",
      #   },
      #   {"Sr": 15, "ID": "Quality", "SVG": "/assets/doxbook_theme/images/Quality.svg"},
      #   {"Sr": 16, "ID": "Projects", "SVG": "/assets/doxbook_theme/images/Project.svg"},
      #   {"Sr": 17, "ID": "Loans", "SVG": "/assets/doxbook_theme/images/Loan.svg"},
      #   {"Sr": 18, "ID": "Tax & Benefits", "SVG": ""},
      #   {"Sr": 19, "ID": "Salary Payout", "SVG": ""},
      #   {"Sr": 20, "ID": "Payroll", "SVG": "/assets/doxbook_theme/images/Payroll.svg"},
      #   {"Sr": 21, "ID": "Performance", "SVG": ""},
      #   {"Sr": 22, "ID": "Leaves", "SVG": ""},
      #   {"Sr": 23, "ID": "Recruitment", "SVG": ""},
      #   {"Sr": 24, "ID": "Expense Claims", "SVG": ""},
      #   {"Sr": 25, "ID": "Shift & Attendance", "SVG": ""},
      #   {"Sr": 26, "ID": "Employee Lifecycle", "SVG": ""},
      #   {"Sr": 27, "ID": "HR", "SVG": "/assets/doxbook_theme/images/HrWhiteRed.svg"},
      #   {
      #       "Sr": 28,
      #       "ID": "Buying",
      #       "SVG": "/assets/doxbook_theme/images/BuyingWhiteRed.svg",
      #   },
      #   {"Sr": 29, "ID": "Stock", "SVG": "/assets/doxbook_theme/images/stock.svg"},
      #   {
      #       "Sr": 30,
      #       "ID": "Selling",
      #       "SVG": "/assets/doxbook_theme/images/SalesRedWhite.svg",
      #   },
      #   {"Sr": 31, "ID": "CRM", "SVG": "/assets/doxbook_theme/images/CrmWhiteRed.svg"},
      #   {
      #       "Sr": 32,
      #       "ID": "Expenses",
      #       "SVG": "/assets/doxbook_theme/images/ExpensesRedWhite.svg",
      #   },
      #   {"Sr": 33, "ID": "Assets", "SVG": "/assets/doxbook_theme/images/Assets.svg"},
      #   {
      #       "Sr": 34,
      #       "ID": "Accounting",
      #       "SVG": "/assets/doxbook_theme/images/AccountingRedWhite.svg",
      #   },
      #   {"Sr": 35, "ID": "Home", "SVG": "/assets/doxbook_theme/images/homepage08b992.svg"},
      #   {"Sr": 36, "ID": "Accounts", "SVG": ""},
      #   {"Sr": 37, "ID": "Fixed Assets", "SVG": ""},
      #   {"Sr": 38, "ID": "Inventory", "SVG": ""},
      #   {
      #       "Sr": 39,
      #       "ID": "Branch Sales",
      #       "SVG": "/assets/doxbook_theme/images/BranchDox.svg",
      #   },
      #   {
      #       "Sr": 40,
      #       "ID": "Sales",
      #       "SVG": "/assets/doxbook_theme/images/BranchDox.svg",
      #   },
      
      #updated script as per required workspace
        {
            "Sr": 32,
            "ID": "Sales",
            "SVG": "/assets/doxbook_theme/images/SalesWS.svg",
        },
        {
            "Sr": 33,
            "ID": "Leads",
            "SVG": "/assets/doxbook_theme/images/leads.svg",
        },
        {
            "Sr": 34,
            "ID": "Customers",
            "SVG": "/assets/doxbook_theme/images/Customer.svg",
        },
        {
            "Sr": 35,
            "ID": "Quotations",
            "SVG": "/assets/doxbook_theme/images/Qutation.svg",
        },
        {
            "Sr": 36,
            "ID": "Sales Orders",
            "SVG": "/assets/doxbook_theme/images/SalesOrder.svg",
        },
        {
            "Sr": 37,
            "ID": "Sales Invoices",
            "SVG": "/assets/doxbook_theme/images/SalesInvoices.svg",
        },
        {
            "Sr": 38,
            "ID": "Customer Payment",
            "SVG": "/assets/doxbook_theme/images/CustomerPayment.svg",
        },
         {
            "Sr": 39,
            "ID": "Purchases",
            "SVG": "/assets/doxbook_theme/images/PurchasesWS.svg",
        },
         {
            "Sr": 40,
            "ID": "Suppliers",
            "SVG": "/assets/doxbook_theme/images/Supplier.svg",
        },
          {
            "Sr": 41,
            "ID": "Purchases Orders",
            "SVG": "/assets/doxbook_theme/images/PurchasesOrder.svg",
        },
          {
            "Sr": 42,
            "ID": "Purchases Invoices",
            "SVG": "/assets/doxbook_theme/images/PurchasesInvoice.svg",
        },
          {
            "Sr": 43,
            "ID": "Landed Vouchers",
            "SVG": "/assets/doxbook_theme/images/LandedCost.svg",
        },
          {
            "Sr": 44,
            "ID": "Suppliers Payments",
            "SVG": "/assets/doxbook_theme/images/SupplierPayment.svg",
        },
          {
            "Sr": 45,
            "ID": "Inventory",
            "SVG": "/assets/doxbook_theme/images/InventoryWS.svg",
        },
          {
            "Sr": 46,
            "ID": "Items",
            "SVG": "/assets/doxbook_theme/images/Item.svg",
        },
          {
            "Sr": 47,
            "ID": "Warehouses",
            "SVG": "/assets/doxbook_theme/images/Warehouses.svg",
        },
          {
            "Sr": 48,
            "ID": "Stock transfers",
            "SVG": "/assets/doxbook_theme/images/StockTransfer.svg",
        },
          {
            "Sr": 49,
            "ID": "Stock Adjustments",
            "SVG": "/assets/doxbook_theme/images/StockAdjustment.svg",
        },
          {
            "Sr": 50,
            "ID": "Accountant",
            "SVG": "/assets/doxbook_theme/images/AccountantWS.svg",
        },
          {
            "Sr": 51,
            "ID": "Project Management",
            "SVG": "/assets/doxbook_theme/images/icons8-project-48.png",
        },
          {
            "Sr": 52,
            "ID": "Chart Of Accounts",
            "SVG": "/assets/doxbook_theme/images/ChartOfAccounts.svg",
        },
          {
            "Sr": 53,
            "ID": "Journal Entries",
            "SVG": "/assets/doxbook_theme/images/JournalEntryWS.svg",
        },
          {
            "Sr": 54,
            "ID": "Expense Entries",
            "SVG": "/assets/doxbook_theme/images/ExpensesEntriesWS.svg",
        },
          {
            "Sr": 55,
            "ID": "Salary Entries",
            "SVG": "/assets/doxbook_theme/images/SalaryEntryWS.svg",
        },
          {
            "Sr": 56,
            "ID": "Cash Transfer",
            "SVG": "/assets/doxbook_theme/images/CashTransferWS.svg",
        },
          {
            "Sr": 57,
            "ID": "Employees",
            "SVG": "/assets/doxbook_theme/images/EmployeesWS.svg",
        },
          {
            "Sr": 58,
            "ID": "Setting",
            "SVG": "/assets/doxbook_theme/images/SettingsWS.svg",
        },
          {
            "Sr": 59,
            "ID": "Reports",
            "SVG": "/assets/doxbook_theme/images/ReportsWS.svg",
        },
    ]

