import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc
from erpnext.buying.doctype.purchase_order.purchase_order import make_purchase_invoice as original_make_purchase_invoice
@frappe.whitelist()
def validate_purchase_invoice(source_name, target_doc=None):
    gate_entry_exists = frappe.db.exists("Gate Entry", {"purchase_order": source_name})

    if not gate_entry_exists:
        frappe.throw(_("Please create a Gate Entry before creating a Purchase Invoice."))

    # return get_mapped_doc(
    #     "Purchase Order",
    #     source_name,
    #     {
    #         "Purchase Order": {
    #             "doctype": "Purchase Invoice",
    #             "validation": {"docstatus": ["=", 1]}
    #         }
    #     },
    #     target_doc,
    #     ignore_permissions=True
    # )
    return original_make_purchase_invoice(source_name, target_doc)