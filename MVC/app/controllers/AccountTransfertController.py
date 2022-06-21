from requests import request
from app import app
from flask import render_template, request
from app.forms.AccountTransferForm import AccountTransfertForm
from app.services.AccountTransfertService import AccountTransfertService

from app.forms.ExampleForm import ExampleForm

accountService = AccountTransfertService()

class ExampleController:
    @app.route('/transfer', methods=['GET'])
    def getAllTransfert():
        tests = accountService.findAll()
        return render_template('test/test.html', tests=tests)

    @app.route('/transfer/add', methods=['GET', 'POST'])
    def postAddTransfert():
        form = AccountTransfertForm(request.form)

        if request.method == 'POST':
            if form.validate():
                test = accountService.insert(form)
                return render_template('transfert/info.html', test=test)
            
            return render_template('transfert/add.html', form=form, errors=form.errors)

        return render_template('transfert/add.html', form=form, testHtml="<h1>TEST</h1>")