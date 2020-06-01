from flask import request, redirect, url_for, session, render_template
from flask_login import login_user, logout_user
from src.service.user_service import UserService

class UserController:

    @classmethod
    def register(cls, mysql):
        if request.method == 'GET':
            user_service = UserService(mysql)
            user_service.add_token_to_session()
            return render_template(
                'user/register.html',
                show_menu=False,
                content_title="Créer un compte", token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return "Bad request"

        if request.form['email'] == '' \
            or request.form['user_name'] == '' \
            or request.form['password'] == '' \
            or request.form['confirmPassword'] == '':
            return "Form is incomplete"

        email = request.form['email']
        user_name = request.form['user_name']
        password = request.form['password']

        if password != request.form['confirmPassword']:
            return "password does not match"

        user_service = UserService(mysql)
        user_service.create(email, password, user_name)

        return 'Done'

    @classmethod
    def login(cls, mysql):
        if request.method == 'GET':
            user_service = UserService(mysql)
            user_service.add_token_to_session()
            return render_template(
                'user/login.html',
                show_menu=False,
                content_title="Connexion", token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return "Bad request"

        user_service = UserService(mysql)

        if request.form['email'] == '' or request.form['password'] == '':
            return "Form is incomplete"

        user = user_service.get_authenticated_user(request.form['email'], request.form['password'])

        if user == False:
            return 'Bad login or account is inactive'
        
        login_user(user)
        return redirect(url_for('home'))

    @classmethod
    def edit(cls, mysql):
        if request.method == 'GET':
            return render_template(
                'user/edit.html',
                show_menu=False,
                content_title="Edition du profil",
                token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return "Bad request"    

        if request.form['currentEmail'] == '' \
            or request.form['newEmail'] == '' \
            or request.form['confirmNewEmail'] == '' \
            or request.form['currentPassword'] == '' \
            or request.form['newPassword'] == '' \
            or request.form['confirmNewPassword'] == '':
            return "Form is incomplete"

        email = request.form['currentEmail']
        newEmail = request.form['newEmail']
        password = request.form['currentPassword']
        new_password = request.form['newPassword']

        user_service = UserService(mysql)
        user = user_service.get_authenticated_user(email, password)

        if user == False:
            return 'Bad login or account is inactive'

        if newEmail != request.form['confirmNewEmail']:
            return "New email does not match"

        if new_password != request.form['confirmNewPassword']:
            return "New password does not match"

        user_service.update(user, new_password, newEmail)
        
        return 'Done'

    @classmethod
    def logout(cls):
        logout_user()

        return redirect(url_for('home'))