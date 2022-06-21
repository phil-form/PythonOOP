from app import conn
from app.forms.dbForm import DbForm
from app.models.db import Db

class DbService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM dbDatas")
        datas = []
        for data in cur.fetchall():
            datas.append(Db(data[0], data[1]))

        return tests

    def findOne(self, testid):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM dbDatas WHERE id = {id}")
        data = cur.fetchone()        

        return Db(data[0], data[1])

    def insert(self, data: DbForm):
        cur = conn.cursor()
        cur.execute("INSERT INTO dbDatas(id, contentText) VALUES(" + str(data.id.data) + ", '" + str(data.text.data) + "')")
        conn.commit()

        return self.findOne(int(data.id.data))