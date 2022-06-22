from app import app
from flask import render_template, request, redirect, url_for
from app.forms.UserForm import UserForm
from app.forms.SearchUserForm import SearchUserForm
from app.services.UserService import UserService

userService = UserService()


class UserController:

    @app.route('/users', methods=['GET'])
    def getAllUsers():
        users = userService.findAll()
        return render_template('user/user_list.html', users=users)

    @app.route('/users/<int:userid>', methods=['GET'])
    def getOneUser(userid):
        user = userService.findOne(userid)
        return render_template('user/user_info.html', user=user)

    @app.route('/users/search', methods=['GET', 'POST'])
    def searchUser(username=None):
        user = None
        if request.method == 'POST':
            form = SearchUserForm(request.form)
            user = userService.findOneBy(username=form.username.data)
        return render_template('user/user_search.html', user=user)

    @app.route('/users/add', methods=['GET', 'POST'])
    def insertUser():
        form = UserForm(request.form)

        if request.method == 'POST':
            if form.validate():
                userService.insert(form)
                return redirect(url_for('getAllUsers'))

        return render_template('user/user_form.html', errors=form.errors)
