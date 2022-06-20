from app import conn
from app.forms.TestForm import TestForm
from app.models.Test import Test

class TestService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM test")
        tests = []
        for test in cur.fetchall():
            tests.append(Test(test[0], test[1]))

        return tests

    def findOne(self, testid):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM test WHERE testid = {testid}")
        testData = cur.fetchone()        

        return Test(testData[0], testData[1])

    def insert(self, data: TestForm):
        cur = conn.cursor()
        cur.execute("INSERT INTO test(testid, testtext) VALUES(" + str(data.testid.data) + ", '" + str(data.testtext.data) + "')")
        conn.commit()

        return self.findOne(int(data.testid.data))