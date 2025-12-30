
# import frappe
# from frappe import _
# from frappe.model.mapper import get_mapped_doc
# from erpnext.accounts.doctype.payment_request.payment_request import make_payment_request as original_make_payment_request

# @frappe.whitelist()
# def validate_payment_request(**args):
#     source_name = args.get("reference_name")

#     if args.get("reference_doctype") == "Purchase Order":
#         if not frappe.db.exists("Gate Entry", {"purchase_order": source_name}):
#             frappe.throw(_("Please create a Gate Entry before creating a Payment Request."))

#     return original_make_payment_request(**args)



import frappe
from frappe import _
from erpnext.accounts.doctype.payment_request.payment_request import make_payment_request as original_make_payment_request

@frappe.whitelist()
def validate_payment_request(**args):
    # frappe.msgprint("Custom Payment Request Override Triggered")  # Debug

    source_name = args.get("reference_name")

    # Validate Gate Entry only if reference is Purchase Order
    if args.get("reference_doctype") == "Purchase Order":
        if not frappe.db.exists("Gate Entry", {"purchase_order": source_name}):
            # Stop process completely
            frappe.throw(_("Please create a Gate Entry before creating a Payment Request."))

    # If validation passes, proceed with original method
    return original_make_payment_request(**args)



