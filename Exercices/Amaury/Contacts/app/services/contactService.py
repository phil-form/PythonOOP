from app import conn
from app.forms.contactForm import ContactForm
from app.models.contact import Contact

class ContactService:
    def __init__(self) -> None:
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts;")
        datas = []
        for data in cur.fetchall():
            datas.append(Contact(data[0], data[1], data[2], data[3], data[4]))

        return datas

    def insert(self, data: ContactForm):
        cur = conn.cursor()

        cur.execute("INSERT INTO contacts(firstname, lastname, email, password) VALUES(%s, %s, %s, %s)",
            (str(data.firstname.data), str(data.lastname.data), str(data.email.data), str(data.password.data)))
        conn.commit()

        return str(data.firstname.data) + ' ' + str(data.lastname.data)