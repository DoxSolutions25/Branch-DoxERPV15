frappe.ui.form.on("Item", {
    item_type: function(frm){
        if(frm.doc.item_type == "Stock"){
            frm.set_value({
                is_stock_item: 1,
                is_fixed_asset: 0,
                include_item_in_manufacturing: 0
            })
        }else if(frm.doc.item_type == "Service"){
            frm.set_value({
                is_stock_item: 0,
                is_fixed_asset: 0,
                include_item_in_manufacturing: 0
            })
        }else if(frm.doc.item_type == "Asset"){
            // frm.set_value('is_fixed_asset', 1)
            // frm.set_value('is_stock_item', 0)
            // frm.set_value('include_item_in_manufacturing', 0)
            frm.set_value({
                is_stock_item: 0,
                is_fixed_asset: 1,
                include_item_in_manufacturing: 0
            })
        }
        else{
            frm.set_value({
                is_stock_item: 1,
                is_fixed_asset: 0,
                include_item_in_manufacturing: 0
            })
        }
    },
    transaction_type: function(frm){
        if(frm.doc.transaction_type == "Sales"){
            frm.set_value({
                is_purchase_item: 0,
                is_sales_item: 1
            })
        }else if(frm.doc.transaction_type == "Purchases"){
            frm.set_value({
                is_purchase_item: 1,
                is_sales_item: 0
            })
        }else if(frm.doc.transaction_type == "Both"){
            frm.set_value({
                is_purchase_item: 1,
                is_sales_item: 1
            })
        }else{
            frm.set_value({
                is_purchase_item: 1,
                is_sales_item: 1
            })
        }
    }
});