import frappe


FIELD_SPECS = (
    {
        "fieldname": "accord_flow_state",
        "label": "Accord Flow State",
        "fieldtype": "Int",
        "insert_after": "remarks",
    },
    {
        "fieldname": "accord_customer_state",
        "label": "Accord Customer State",
        "fieldtype": "Int",
        "insert_after": "accord_flow_state",
    },
    {
        "fieldname": "accord_customer_reason",
        "label": "Accord Customer Reason",
        "fieldtype": "Small Text",
        "insert_after": "accord_customer_state",
    },
    {
        "fieldname": "accord_delivery_actor",
        "label": "Accord Delivery Actor",
        "fieldtype": "Data",
        "insert_after": "accord_customer_reason",
    },
)


def ensure_delivery_note_state_fields():
    for spec in FIELD_SPECS:
        _ensure_custom_field("Delivery Note", spec)


def _ensure_custom_field(dt: str, spec: dict):
    existing_name = frappe.db.exists("Custom Field", {"dt": dt, "fieldname": spec["fieldname"]})
    if existing_name:
        doc = frappe.get_doc("Custom Field", existing_name)
        changed = False
        for key, value in (
            ("label", spec["label"]),
            ("fieldtype", spec["fieldtype"]),
            ("insert_after", spec["insert_after"]),
            ("hidden", 0),
            ("read_only", 1),
            ("allow_on_submit", 1),
            ("no_copy", 1),
        ):
            if doc.get(key) != value:
                doc.set(key, value)
                changed = True
        if changed:
            doc.save(ignore_permissions=True)
        return

    doc = frappe.get_doc(
        {
            "doctype": "Custom Field",
            "dt": dt,
            "fieldname": spec["fieldname"],
            "label": spec["label"],
            "fieldtype": spec["fieldtype"],
            "insert_after": spec["insert_after"],
            "hidden": 0,
            "read_only": 1,
            "allow_on_submit": 1,
            "no_copy": 1,
        }
    )
    doc.insert(ignore_permissions=True)
