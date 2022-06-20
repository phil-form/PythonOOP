from app import app
from flask import render_template
from app.models.Person import Person


class ExampleController:
    @app.route('/person')
    def person():
        person = Person("Claire", "Bretton", 30)
        return render_template('person/person.html', person=person)
