"""Controller to handle user operations"""
from flask import request, redirect, url_for, session, render_template
from flask_login import login_user, logout_user
from src.service.user_service import UserService

class UserController:
    """Another useless comment"""

    BAD_REQUEST = "Bad request"
    FORM_INCOMPLETE = "Form is incomplete"

    @classmethod
    def register(cls, mysql):
        """Endpoint to register an user"""
        if request.method == 'GET':
            user_service = UserService(mysql)
            user_service.add_token_to_session()
            return render_template(
                'user/register.html',
                show_menu=False,
                content_title="Créer un compte", token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return UserController.BAD_REQUEST

        if request.form['email'] == '' \
            or request.form['user_name'] == '' \
            or request.form['password'] == '' \
            or request.form['confirmPassword'] == '':
            return UserController.FORM_INCOMPLETE

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
        """Endpoint for login"""
        if request.method == 'GET':
            user_service = UserService(mysql)
            user_service.add_token_to_session()
            return render_template(
                'user/login.html',
                show_menu=False,
                content_title="Connexion", token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return UserController.BAD_REQUEST

        user_service = UserService(mysql)

        if request.form['email'] == '' or request.form['password'] == '':
            return UserController.FORM_INCOMPLETE

        user = user_service.get_authenticated_user(request.form['email'], request.form['password'])

        if user is False:
            return 'Bad login or account is inactive'

        login_user(user)
        return redirect(url_for('home'))

    @classmethod
    def edit(cls, mysql):
        """Endpoint for editing user profile"""
        if request.method == 'GET':
            return render_template(
                'user/edit.html',
                show_menu=False,
                content_title="Edition du profil",
                token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return UserController.BAD_REQUEST

        fields_to_validate = (
            'currentEmail',
            'newEmail',
            'confirmNewEmail',
            'currentPassword',
            'newPassword',
            'confirmNewPassword'
        )

        for field in fields_to_validate:
            if request.form[field] == '':
                return UserController.FORM_INCOMPLETE

        email = request.form['currentEmail']
        new_email = request.form['newEmail']
        password = request.form['currentPassword']
        new_password = request.form['newPassword']

        user_service = UserService(mysql)
        user = user_service.get_authenticated_user(email, password)

        error_message = ""
        if user is False:
            error_message += 'Bad login or account is inactive. '

        if new_email != request.form['confirmNewEmail']:
            error_message += "New email does not match. "

        if new_password != request.form['confirmNewPassword']:
            error_message += "New password does not match. "

        if error_message != '':
            return error_message

        user_service.update(user, new_password, new_email)

        return 'Done'

    @classmethod
    def logout(cls):
        """Endpoint for logout"""
        logout_user()

        return redirect(url_for('home'))
