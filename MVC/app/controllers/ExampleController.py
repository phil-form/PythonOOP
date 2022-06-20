from requests import request
from app import app
from flask import render_template, request

from app.forms.ExampleForm import ExampleForm

class ExampleController:
    @app.route('/')
    def example():
        return render_template('example/example.html')

    # @app.route('/example', methods=['GET', 'POST'])
    @app.route('/example', methods=['GET'])
    def exampleExample():
        # if request.method == 'POST':
        #     return render_template('example/superExample.html', example="POST")
        return render_template('example/superExample.html', example="GET")

    @app.route('/example', methods=['POST'])
    def examplePostExample():
        form = ExampleForm(request.form)

        if form.validate():
            return render_template('example/superExample.html', example=f"{form.firstname.data} {form.lastname.data}")

        return render_template('example/superExample.html', example="POST")