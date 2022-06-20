from app   import app
from flask import render_template

class ExampleController:
    @app.route('/')
    def example():
        return render_template('example/example.html')

    @app.route('/example')
    def exampleExample():
        return render_template('example/superExample.html', example="C'est un test")
