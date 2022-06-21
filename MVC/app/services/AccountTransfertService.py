from app import conn
from app.forms.AccountTransferForm import AccountTransfertForm
from app.models.AccountTransfer import AccountTransfer

class AccountTransfertService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM accounttransfer;")
        tests = []
        for test in cur.fetchall():
            tests.append(AccountTransfer(test[0], test[1], test[2], test[3]))

        return tests

    def findOne(self, transferid):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM accounttransfer WHERE transferid = {transferid};")
        testData = cur.fetchone()
        conn.commit()

        return AccountTransfer(testData[0], testData[1], testData[2], testData[3])

    def insert(self, data: AccountTransfertForm):
        cur = conn.cursor()
        cur.execute("INSERT INTO accounttransfer(fromaccount, toaccount, amount) VALUES(" + str(data.fromaccount.data) + ", " + str(data.toaccount.data) + ", " + str(data.amount.data) + ");")
        conn.commit()

        return None