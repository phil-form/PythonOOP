from app import app
from flask import render_template, request
from app.forms.ContactForm import ContactForm


class ContactController:

    @app.route('/contact', methods=['GET'])
    def contactForm():
        # if request.method == 'POST':
        return render_template('contact/contactForm.html', contact="GET")

    @app.route('/contact', methods=['POST'])
    def contactPostForm():
        form = ContactForm(request.form)

        if form.validate():
            contact = {}
            contact["first_name"] = form.first_name.data
            contact["last_name"] = form.last_name.data
            contact["email"] = form.email.data
            contact["descr"] = form.descr.data
            return render_template('contact/contactDone.html', contact=contact)

        return render_template('contact/contactForm.html', error=True)
