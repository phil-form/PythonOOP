from app import app
from flask import render_template

class AmauryController:
    @app.route('/')
    def example():
        return render_template('amaury/amaury.html')

    @app.route('/amaury')
    def exampleExample():
        return render_template('amaury/amauryBis.html', example="AMAURY")

    @app.route('/CV')
    def cv():
        return render_template('amaury/amauryCV.html', name = "Crenier Amaury")