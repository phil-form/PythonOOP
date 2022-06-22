class AccountTransfer:
    def __init__(self, testid: int, fromaccount: int, toaccount: int, amount: int) -> None:
        self.transferid = testid
        self.fromaccount = fromaccount
        self.toaccount = toaccount
        self.amount = amount