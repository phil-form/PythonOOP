from app import conn
from app.models.User import User
from app.forms.UserForm import UserForm

class UserService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        with conn.cursor() as cur:
            cur.execute("SELECT userid, username, userpassword, email, userdescription FROM users")
            users = []

            for user in cur.fetchall():
                users.append(User(user[0], user[1], user[2], user[3], user[4]))

            return users

    def findOne(self, userid):
        with conn.cursor() as cur:
            cur.execute(f"SELECT userid, username, userpassword, email, userdescription FROM users WHERE userid = %s", (str(userid),))
            user = cur.fetchone()

            if cur.rowcount == 1:
                return User(user[0], user[1], user[2], user[3], user[4])
            else:
                return None

    def findOneBy(self, **kwargs):
        with conn.cursor() as cur:
            query = "SELECT userid, username, userpassword, email, userdescription FROM users"
            isFirst = True
            values = []
            for key, val in kwargs.items():
                query += " WHERE " if isFirst else " AND "
                query += f"{key} = %s"
                values.append(str(val))
            cur.execute(query, tuple(values))
            user = cur.fetchone()

            if cur.rowcount >= 1:
                return User(user[0], user[1], user[2], user[3], user[4])
            else:
                return None

    def insert(self, data: UserForm):
        with conn.cursor() as cur:
            query = "INSERT INTO users(username, userpassword, email, userdescription) VALUES(%(username)s, " \
                    "%(userpassword)s, %(email)s, %(userdescription)s); "
            values = {'username': data.username.data,
                      "userpassword": data.userpassword.data,
                      "email": data.email.data,
                      "userdescription": data.userdescription.data}
            cur.execute(query, values)
            conn.commit()


