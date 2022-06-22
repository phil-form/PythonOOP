from getpass import getuser
from app import conn
from app.models.user import user
from lxml.html.clean import clean_html

class userService:
    def __init__(self) -> None:
        pass

    def getAllUsers(self):
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM users')

            users = []
            for row in cur.fetchall():
                users.append(user(row[0], row[1], row[2], row[3], row[4]))
            return users

    def getUser(self, userID=None, username=None):
        with conn.cursor() as cur:
            if userID:
                cur.execute(f'SELECT * FROM users WHERE userid={userID}')
            else:
                cur.execute(f"SELECT * FROM users WHERE username='{username}'")
            data = cur.fetchone()
            return user(data[0], data[1], data[2], data[3], data[4],)

    def register(self, form):
        with conn.cursor() as cur:
            cur.execute(f"""INSERT INTO users(username, password, mail, description) Values(
                '{form.data["username"]}',
                '{form.data["password"]}',
                '{form.data["mail"]}',
                '{form.data["description"]}'
            )""")
            cur.execute(f"SELECT * FROM users WHERE username='{form.data['username']}'")
            rval = self.getUser(userID=None, username=form.data["username"])
            return rval