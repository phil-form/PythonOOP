from app import conn
from app.models.Contact import Contact
from app.forms.ContactForm import ContactForm


class ContactService:
    def __init__(self) -> None:     
        pass

    def findAll(self):
        cur = conn.cursor()
        cur.execute("SELECT firstName, lastName, email FROM contacts;")
        contacts = []
        for contact in cur.fetchall():
            contacts.append(Contact(contact[0], contact[1], contact[2]))
        return contacts

    def insert(self, data: ContactForm):
        cur = conn.cursor()
        cur.execute(f"INSERT INTO contacts(firstName, lastName, email) VALUES('{data.first_name.data}', '{data.last_name.data}', '{data.email.data}')")
        conn.commit()
