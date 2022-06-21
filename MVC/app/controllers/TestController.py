from requests import request
from app import app
from flask import render_template, request
from app.forms.TestForm import TestForm
from app.services.TestService import TestService

from app.forms.ExampleForm import ExampleForm

testService = TestService()

class ExampleController:
    @app.route('/test', methods=['GET'])
    def getAllTests():
        tests = testService.findAll()
        return render_template('test/test.html', tests=tests)

    @app.route('/test/<int:testid>', methods=['GET'])
    def getOneTests(testid):
        test = testService.findOne(testid)
        return render_template('test/info.html', test=test)

    @app.route('/test/by/name', methods=['GET'])
    def getOneByName():
        testtext = request.args.get('testtext')
        test = None
        if testtext != None:
            test = testService.findOneBy(testtext = testtext)
        return render_template('test/search.html', test=test)

    @app.route('/test/add', methods=['GET', 'POST'])
    def postTest():
        form = TestForm(request.form)

        if request.method == 'POST':
            if form.validate():
                test = testService.insert(form)
                return render_template('test/info.html', test=test)
            
            return render_template('test/add.html', errors=form.errors)

        return render_template('test/add.html', example="POST")