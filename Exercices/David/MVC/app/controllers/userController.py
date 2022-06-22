from flask import render_template
from app import app
from app.services.userService import userService

us = userService()

@app.route('/users', methods=['GET'])
def showUsers():
    users = us.getAllUsers()
    return render_template('user.html', users=users)

@app.route('/register', methods=['POST'])
def registerUser():
    user = us.register():