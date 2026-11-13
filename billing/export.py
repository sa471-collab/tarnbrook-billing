"""CSV export."""
import csv
import io


def export_invoices(invoices):
    rows = sorted(invoices, key=lambda i: i["number"])
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=["number", "customer", "total"])
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()
