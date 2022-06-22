from app import conn
from app.forms.TestForm import TestForm
from app.models.Test import Test

class TestService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        # cur = conn.cursor()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test")
            tests = []

            for test in cur.fetchall():
                tests.append(Test(test[0], test[1]))

            return tests

    def findOne(self, testid):
        # cur = conn.cursor()
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM test WHERE testid = %s", (str(testid),))
            testData = cur.fetchone()

            if cur.rowcount == 1:
                return Test(testData[0], testData[1])
            else:
                return None

    def findOneBy(self, **kwargs):
        # cur = conn.cursor()
        with conn.cursor() as cur:
            query = "SELECT * FROM test"
            isFirst = True
            values = []
            for key, val in kwargs.items():
                query += " WHERE " if isFirst else " AND "
                query += f"{key} = %s"
                values.append(str(val))

            cur.execute(query, tuple(values))
            testData = cur.fetchone()        

            if cur.rowcount == 1:
                return Test(testData[0], testData[1])
            else:
                return None

    def insert(self, data: TestForm):
        # cur = conn.cursor()
        with conn.cursor() as  cur:
            cur.execute("INSERT INTO test(testid, testtext) VALUES(" + str(data.testid.data) + ", '" + str(data.testtext.data) + "')")
            conn.commit()

            return self.findOne(int(data.testid.data))