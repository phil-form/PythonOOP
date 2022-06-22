from requests import request
from app import app
from flask import render_template, request
from app.forms.contactForm import ContactForm
from app.services.contactService import ContactService
from app.forms.contactForm import ContactForm

contactService = ContactService()

class ContactController:
    @app.route('/contact', methods=['GET'])
    def getContacts():
        datas = contactService.findAll()
        return render_template('page.html', datas = datas)

    @app.route('/contact', methods=['POST'])
    def postContact():
        form = ContactForm(request.form)

        if form.validate():
            data = contactService.insert(form)
            return render_template('page.html', data = data)
            
        return render_template('page.html', form = form, errors = form.errors)