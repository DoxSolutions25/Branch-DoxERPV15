frappe.ui.form.on('Branch', {
    onload: function(frm) {
        set_account_filters(frm);
    },
    refresh: function(frm) {
        set_account_filters(frm);
    }
});

function set_account_filters(frm) {
    
    frm.fields_dict['branch_bank_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Bank'
            }
        };
    };

    
    frm.fields_dict['branch_tax_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Tax'
            }
        };
    };

    
    frm.fields_dict['branch_cogs_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Cost of Goods Sold'
            }
        };
    };

    
    frm.fields_dict['branch_cash_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Cash'
            }
        };
    };
    
    frm.fields_dict['branch_income_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Direct Income'
            }
        };
    };
    
    frm.fields_dict['branch_direct_expense_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Direct Expenses'
            }
        };
    };
    
    frm.fields_dict['branch_indirect_income_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Indirect Income'
            }
        };
    };
    
    
    frm.fields_dict['branch_indirect_expense_account'].grid.get_field('account').get_query = function(doc, cdt, cdn) {
        return {
            filters: {
                'account_type': 'Indirect Expenses'
            }
        };
    };
    
}