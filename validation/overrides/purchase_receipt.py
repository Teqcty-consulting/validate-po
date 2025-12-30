import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_receipt as original_make_purchase_receipt

@frappe.whitelist()
def validate_purchase_receipt(source_name, target_doc=None):
    gate_entry_exists = frappe.db.exists("Gate Entry", {"purchase_order": source_name})
    

    if not gate_entry_exists:
        frappe.throw(_("Please create a Gate Entry before creating a Purchase Receipt."))

    # return get_mapped_doc(
    #         "Purchase Order",
    #         source_name,
    #         {
    #             "Purchase Order": {
    #                 "doctype": "Purchase Receipt",
    #                 "validation": {"docstatus": ["=", 1]}
    #             },
    #             "Purchase Order Item": {
    #                 "doctype": "Purchase Receipt Item",
    #                 "field_map": {
    #                     "parent": "purchase_order",
    #                     "name": "purchase_order_item"
    #                 }
    #             }
    #         },
    #         target_doc,
    #         ignore_permissions=True  
    # )
    return original_make_purchase_receipt(source_name, target_doc)


