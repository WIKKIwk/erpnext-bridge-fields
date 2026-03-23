# Accord State Core

Minimal backend-only custom app for Accord workflow state on ERPNext documents.

This app is intentionally small:
- no desk workspace
- no page UI
- no website routes
- only installable backend hooks and state-field helpers

Current responsibility:

- ensure `Delivery Note` custom fields exist
- keep `accord_ui_status` visible on the form
- keep internal workflow fields available for backend state handling

Managed `Delivery Note` fields:

- `accord_flow_state`
- `accord_customer_state`
- `accord_customer_reason`
- `accord_delivery_actor`
- `accord_status_section`
- `accord_ui_status`
