from app   import app
from flask import render_template

from app.models.Personne import Personne

class MyController:
    @app.route('/moi')
    def getMoi():
        je = Personne("Etienne", "ANDRÉ", "Analyste programmeur depuis 25 ans")

        je.addExperience("2000", "Idem Papers")
        je.addExperience("1998", "Datapoint")

        je.addSkills("Uniface")
        je.addSkills("VB")

        je.addFormation("Paul Lambin")

        return render_template('moi/moi.html', personne = je)
