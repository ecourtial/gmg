""" Version controller for the GMG project """
from flask import jsonify, request
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.repository.version_repository import VersionRepository
from src.service.version_service import VersionService
from src.entity.version import Version
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.resource_has_children_exception import RessourceHasChildrenException

class VersionController:
    @classmethod
    def get_by_id(cls, mysql, id):
        repo = VersionRepository(mysql)
        version = repo.get_by_id(id)

        if version is None:
            return jsonify({'message': 'Version not found.'}), 404

        return jsonify(version.serialize()), 200

    @classmethod
    def create(cls, mysql):
        service = VersionService(mysql)

        try:
            version = service.validate_payload_for_creation_and_hydrate()
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        version_repository = VersionRepository(mysql)
        version = version_repository.insert(version)

        return cls.get_by_id(mysql, version.get_id())

    @classmethod
    def update(cls, mysql, version_id):
        service = VersionService(mysql)

        try:
            version = service.validate_payload_for_update_and_hydrate(version_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400

        version_repository = VersionRepository(mysql)
        version = version_repository.update(version)

        return cls.get_by_id(mysql, version.get_id())

    @classmethod
    def delete(cls, mysql, version_id):
        service = VersionService(mysql)

        try:
            service.delete(version_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except RessourceHasChildrenException as e:
            return jsonify({'message': str(e)}), 400

        return jsonify({'message': 'Version successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        repo = VersionRepository(mysql)
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        order_by = request.args.get('order_by')
        order = request.args.get('order')

        return jsonify(repo.get_list(request.args, page, limit, order_by, order))
