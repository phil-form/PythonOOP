import psycopg2


conn = psycopg2.connect(dbname='app', user='app', password='1234', host='127.0.0.1', port='5435')

cur = conn.cursor()

cur.execute(f"SELECT * FROM test WHERE testtext = 'asdf'; SELECT * FROM accounttransfer WHERE transferid = 2; --'")

print(cur.fetchall())