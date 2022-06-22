from flask import render_template, request
from app import app
from app.services.userService import userService
from app.forms.userForm import userForm

us = userService()

@app.route('/users', methods=['GET'])
def showUsers():
    users = us.getAllUsers()
    return render_template('user.html', users=users)

@app.route('/register', methods=['GET'])
def register():
    return render_template('userForm.html')

@app.route('/register', methods=['POST'])
def registerUser():
    user = us.register(userForm(request.form))
    return render_template('user.html', user=user)