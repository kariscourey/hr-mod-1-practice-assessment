from datetime import datetime
class Invoice:
    def __init__(self, customer_name, amount, invoice_date):
        self.customer_name = customer_name
        self.amount_due = amount
        self.invoice_date = invoice_date

def amount_due(invoices, days=30):
    past_due = 0
    for invoice in invoices:
        if (datetime.now() - invoice.invoice_date).days > days:
            past_due += invoice.amount_due
    return past_due

invoices = [
    Invoice("Raul", 25.00, datetime(2010, 4, 15)),
    Invoice("Poli", 50.00, datetime(2029, 11, 5)),
    Invoice("Don", 75.00, datetime(2012, 7, 21)),
    Invoice("Anne", 100.00, datetime(2035, 6, 17))
]

result = amount_due(invoices, 90)
print(result)
