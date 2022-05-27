""" Games controller for the GMG project """
from flask import jsonify, request 
from src.repository.platform_repository import PlatformRepository
from src.service.platform_service import PlatformService
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException

class PlatformController:
    @classmethod
    def get_by_id(cls, mysql, platform_id):
        service = PlatformService(mysql)

        try:
            platform = service.get_by_id(platform_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404

        return jsonify(platform.serialize()), 200

    @classmethod
    def create(cls, mysql):
        service = PlatformService(mysql)

        try:
            platform = service.validate_payload_for_creation_and_hydrate()
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        repo = PlatformRepository(mysql)
        platform = repo.insert(platform)

        return cls.get_by_id(mysql, platform.get_id())

    @classmethod
    def update(cls, mysql, platform_id):
        service = PlatformService(mysql)

        try:
            platform = service.validate_payload_for_update_and_hydrate(platform_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        repo = PlatformRepository(mysql)
        platform = repo.update(platform)

        return cls.get_by_id(mysql, platform.get_id())

    @classmethod
    def delete(cls, mysql, platform_id):
        service = PlatformService(mysql)

        try:
            service.delete(platform_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except RessourceHasChildrenException as e:
            return jsonify({'message': str(e)}), 400

        return jsonify({'message': 'Platform successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        repo = PlatformRepository(mysql)
        
        return jsonify(repo.get_list(page, limit))
