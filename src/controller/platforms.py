""" Platforms controller for the GMG project """
from flask import jsonify, request, render_template, session
from src.repository.platform_repository import PlatformRepository

class PlatformController:
    """ Platforms controller for the GMG project """
    @classmethod
    def get_list(cls, mysql):
        """Return the platform list."""
        repo = PlatformRepository(mysql)
        platform_list = repo.get_list()
        return jsonify(platforms=[platform.serialize() for platform in platform_list])

    @classmethod
    def add(cls, mysql):
        """Add a new platform."""
        if request.method == 'GET':
            return render_template(
                'general/platform-form.html',
                show_menu=True,
                content_title="Ajouter une plateforme", token=session['csrfToken']
            )

        if request.form['_token'] != session['csrfToken']:
            return jsonify(), 400

        name = request.form['platform_name']
        if name == '':
            return "Form is incomplete"

        repo = PlatformRepository(mysql)
        repo.insert(name)

        return jsonify(message="Success")
