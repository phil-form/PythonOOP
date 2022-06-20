from requests import request
from app import app
from flask import render_template, request

from app.forms.form import Form

class FormController:

    @app.route('/form', methods=['GET'])
    def getForm():
        return render_template('form/form.html', res="GET")

    @app.route('/form', methods=['POST'])
    def postForm():
        form = Form(request.form)

        if form.validate():
            return render_template('form/form.html', res=f"{form.firstname.data} {form.lastname.data}")

        return render_template('form/form.html', res="POST")