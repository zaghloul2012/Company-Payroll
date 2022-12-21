class Payroll:
    """
    The payroll consists of a payables list
    Each payable is either employee or invoice
    The total paid money is the total paid money for the added employees and invoices
    """

    def __init__(self) -> None:
        self.payables = list()
    
    def add_payable(self, payable):
        self.payables.append(payable)
    
    def total_amount_of_money(self):
        return sum([payable.total_payment() for payable in self.payables])
    
    def __str__(self) -> str:
        self.payables.sort()

        return '\n'.join([str(payable) for payable in self.payables])
