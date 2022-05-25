""" Version controller for the GMG project """
from flask import jsonify, request
from src.repository.version_repository import VersionRepository
from src.service.version_service import VersionService
from src.entity.version import Version
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.unknown_resource_exception import ResourceNotFoundException

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
        repo = VersionRepository(mysql)
        version = repo.get_by_id(version_id)

        if version is None:
            return jsonify({'message': 'Version not found.'}), 404

        title = request.form.get('title', '')
        
        if title == '':
            return jsonify({'message': 'Incomplete payload. The request need the title field to be filled.'}), 400

        version.set_name(title)
        service = VersionService(mysql)
        result = service.update(version)

        if isinstance(result, Version) is False:
            return jsonify({'message': 'The following field must be unique: ' + result}), 400
        
        return cls.get_by_id(mysql, result.get_id())

    @classmethod
    def delete(cls, mysql, version_id):
        repo = VersionRepository(mysql)
        version = repo.get_by_id(version_id)

        if version is None:
            return jsonify({'message': 'Version not found.'}), 404

        service = VersionService(mysql)
        result = service.delete(version)

        if result is False:
            return jsonify({'message': 'Version has versions. Cannot delete it.'}), 400

        return jsonify({'message': 'Version successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        repo = VersionRepository(mysql)
        
        return jsonify(repo.get_list(page, limit))
