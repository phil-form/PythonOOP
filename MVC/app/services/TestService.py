from app import conn
from app.forms.TestForm import TestForm
from app.models.Test import Test

class TestService:
    def __init__(self) -> None:
        pass

    def findAll(self):
<<<<<<< HEAD
        # cur = conn.cursor()
=======
>>>>>>> 91d46e5330bb8ec0d519071b1ed6f6d0c3c82622
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test")
            tests = []

            for test in cur.fetchall():
                tests.append(Test(test[0], test[1]))

            return tests

    def findOne(self, testid):
<<<<<<< HEAD
        # cur = conn.cursor()
=======
>>>>>>> 91d46e5330bb8ec0d519071b1ed6f6d0c3c82622
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM test WHERE testid = %s", (str(testid),))
            testData = cur.fetchone()

            if cur.rowcount == 1:
                return Test(testData[0], testData[1])
            else:
                return None

    def findOneBy(self, **kwargs):
<<<<<<< HEAD
        # cur = conn.cursor()
=======
>>>>>>> 91d46e5330bb8ec0d519071b1ed6f6d0c3c82622
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
<<<<<<< HEAD
        # cur = conn.cursor()
        with conn.cursor() as  cur:
            cur.execute("INSERT INTO test(testid, testtext) VALUES(" + str(data.testid.data) + ", '" + str(data.testtext.data) + "')")
=======
        with conn.cursor() as  cur:
            cur.execute("INSERT INTO test(testid, testtext) VALUES(%s, %s)",
                str(data.testid.data), str(data.testtext.data))
>>>>>>> 91d46e5330bb8ec0d519071b1ed6f6d0c3c82622
            conn.commit()

            return self.findOne(int(data.testid.data))