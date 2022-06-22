from app import conn
from app.models import user

class userService:
    def __init__(self) -> None:
        pass

    def getAllUsers(self):
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM users')

            users = []
            for row in cur.fetchall():
                users.append(user(row))
            return users

    def getUser(self, userID=None, username=None):
        with conn.cursor() as cur:
            if userID:
                cur.execute(f'SELECT * FROM users WHERE userid={userID}')
            else:
                cur.execute(f'SELECT * FROM users WHERE username={username}')
            return user(cur.fetchone())

    def register(self, username, password, mail, description=None):
        with conn.cursor() as cur:
            