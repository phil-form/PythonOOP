from requests import request
from app import app
from flask import render_template, request
from app.forms.dbForm import DbForm
from app.services.DbService import DbService

from app.forms.form import Form

dbService = DbService()

class DbController:
    @app.route('/db', methods=['GET'])
    def getAllDatas():
        datas = dbService.findAll()
        return render_template('db/db.html', datas=datas)

    @app.route('/db/<int:id>', methods=['GET'])
    def getOneData(id):
        data = dbService.findOne(id)
        return render_template('db/info.html', data=data)

    @app.route('/db/add', methods=['GET', 'POST'])
    def postTest():
        form = DbForm(request.form)

        if request.method == 'POST':
            if form.validate():
                data = DbService.insert(form)
                return render_template('db/info.html', data=data)
            
            return render_template('db/add.html', errors=form.errors)

        return render_template('db/add.html', example="POST")