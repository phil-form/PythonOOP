from app import app
from flask import render_template, request, redirect, url_for
from app.forms.ContactForm import ContactForm
from app.services.ContactService import ContactService

contactService = ContactService()


class ContactController:

    @app.route('/contacts', methods=['GET'])
    def getAllContacts():
        contacts = contactService.findAll()
        return render_template('contact/contactList.html', contacts=contacts)

    # @app.route('/test/<int:testid>', methods=['GET'])
    # def getOneTests(testid):
    #     test = testService.findOne(testid)
    #     return render_template('test/info.html', test=test)

    @app.route('/contacts/add', methods=['GET', 'POST'])
    def insertContact():
        form = ContactForm(request.form)

        if request.method == 'POST':
            if form.validate():
                contactService.insert(form)
                return redirect(url_for('getAllContacts'))

        return render_template('contact/contactForm.html', errors=form.errors)
