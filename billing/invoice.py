"""Invoice totals."""


def line_total(quantity, unit_price):
    return quantity * unit_price


def invoice_total(lines):
    # lines are (quantity, unit_price) pairs
    return round(sum(line_total(q, p) for q, p in lines), 2)


def format_total(amount_minor, currency):
    return f"{currency} {amount_minor / 100:.2f}"
