from app import app
from flask import render_template, request
from app.forms.ContactForm import ContactForm
from app.models.Contact import Contact

from app.models.Person import Person

class CvController:
    @app.route('/cv')
    def getCV():
        picsou = Person("Balthazar", "Picsou", "Canard le plus riche du monde!")
        
        picsou.addExperience("Depuis 2019", "Solution manager")
        picsou.addExperience("Depuis 2010", "Formateur")
        picsou.addExperience("De 1991 à 2010", "Développeur")
        picsou.addExperience("De 1947 à 1990", "Banquier")

        picsou.addSkills("HTML et CSS")
        picsou.addSkills("C#")
        picsou.addSkills("C++")
        picsou.addSkills("C")
        picsou.addSkills("ASM")
        picsou.addSkills("Javascript")
        picsou.addSkills("Base de donnée")

        picsou.addFormation("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt in reiciendis illum architecto voluptates, blanditiis neque, labore earum? Nihil libero illum distinctio cupiditate consequuntur quis vitae unde amet excepturi labore.")
        picsou.addFormation("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt in reiciendis illum architecto voluptates, blanditiis neque, labore earum? Nihil libero illum distinctio cupiditate consequuntur quis vitae unde amet excepturi labore.")
        picsou.addFormation("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt in reiciendis illum architecto voluptates, blanditiis neque, labore earum? Nihil libero illum distinctio cupiditate consequuntur quis vitae unde amet excepturi labore.")

        return render_template('cv/cv.html', person = picsou)

    @app.route('/cv/contact', methods=["GET"])
    def contactPage():
        return render_template('cv/contact.html')

    @app.route('/cv/contact', methods=["POST"])
    def contactPost():
        form = ContactForm(request.form)
        if form.validate():
            contact = Contact(form.email.data, form.text.data)
            return render_template('cv/contact.html', contact = contact)

        return render_template('cv/contact.html', errors = form.errors)