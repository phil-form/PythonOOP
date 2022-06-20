from app import app
from flask import render_template
from app.models.Person import Person


class PersonController:
    @app.route('/person')
    def person():
        person = Person("Balthazar", "Picsou")
        person.descr = "Canard le plus riche du monde"
        person.addExperience("Depuis 2010", "Formateur")
        person.addExperience("De 1991 à 2010", "Développeur")
        person.addExperience("De 1947 à 1990", "Banquier")
        person.addSkill("HTML et CSS")
        person.addSkill("C#")
        person.addSkill("Javascript")
        person.addSkill("Base de données")
        person.training = """Lorem ipsum dolor sit amet, consectetur adipiscing 
        elit. Maecenas consectetur iaculis ante non mollis.
        Phasellus varius condimentum justo eu volutpat.
        Donec dapibus est velit, vitae cursus nisl cursus vel.
        Pellentesque eget accumsan tellus, et fringilla tellus.
        Nulla facilisi."""
        return render_template('person/person.html', person=person)
