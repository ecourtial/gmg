""" Platforms controller for the GMG project """
from flask import jsonify, request, render_template, session
from src.repository.platform_repository import PlatformRepository
from src.service.platform_service import PlatformService
from src.entity.platform import Platform

class PlatformController:
    """ Platforms controller for the GMG project """
    @classmethod
    def get_by_id(cls, mysql, id):
        repo = PlatformRepository(mysql)
        platform = repo.get_by_id(id)

        if platform is None:
            return jsonify({'message': 'Platform not found.'}), 404

        return jsonify(platform.serialize()), 200

    @classmethod
    def create(cls, mysql):
        name = request.form.get('name', '')

        if name == '':
            return jsonify({'message': 'Incomplete payload. The request need name field to be filled.'}), 400

        service = PlatformService(mysql)
        result = service.create(name)

        if isinstance(result, Platform) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_id(mysql, result.get_id())

    @classmethod
    def update(cls, mysql, platform_id):
        repo = PlatformRepository(mysql)
        platform = repo.get_by_id(platform_id)

        if platform is None:
            return jsonify({'message': 'Platform not found.'}), 404

        name = request.form.get('name', '')
        
        if name == '':
            return jsonify({'message': 'Incomplete payload. The request need name field to be filled.'}), 400

        platform.set_name(name)
        service = PlatformService(mysql)
        result = service.update(platform)

        if isinstance(result, Platform) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_id(mysql, result.get_id())

    @classmethod
    def delete(cls, mysql, platform_id):
        repo = PlatformRepository(mysql)
        platform = repo.get_by_id(platform_id)

        if platform is None:
            return jsonify({'message': 'Platform not found.'}), 404

        service = PlatformService(mysql)
        result = service.delete(platform)

        if result is False:
            return jsonify({'message': 'Platform has games. Cannot delete it.'}), 400

        return jsonify({'message': 'Platform successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        repo = PlatformRepository(mysql)
        
        return jsonify(repo.get_platforms_list(page, limit))
