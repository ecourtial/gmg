from flask import request, jsonify
from src.exception.inconsistent_operation import InconsistentOperation
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.unsupported_value_exception import UnsupportedValueException

class AbstractController:# pylint: disable=no-member
    @classmethod
    def get_by_id(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            copy = service.get_by_id(entity_id)
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404

        return jsonify(copy.serialize()), 200

    @classmethod
    def create(cls, mysql):
        service = cls.service(mysql)

        try:
            object = service.get_for_create()
        except UnsupportedValueException as error:
            return jsonify({'message': str(error)}), 400
        except MissingFieldException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceAlreadyExistsException as error:
            return jsonify({'message': str(error)}), 400
        except InconsistentOperation as error:
            return jsonify({'message': str(error)}), 400
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404

        repo = cls.repository(mysql)
        object = repo.insert(object)

        return cls.get_by_id(mysql, object.get_id())

    @classmethod
    def update(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            object = service.get_for_update(entity_id)
        except UnsupportedValueException as error:
            return jsonify({'message': str(error)}), 400
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404
        except ResourceAlreadyExistsException as error:
            return jsonify({'message': str(error)}), 400
        except InconsistentOperation as error:
            return jsonify({'message': str(error)}), 400

        repo = cls.repository(mysql)
        object = repo.update(object)

        return cls.get_by_id(mysql, object.get_id())

    @classmethod
    def delete(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            service.delete(entity_id)
        except ResourceNotFoundException as error:
            return jsonify({'message': str(error)}), 404
        except RessourceHasChildrenException as error:
            return jsonify({'message': str(error)}), 400

        return jsonify({'message': service.resource_type + ' successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        repo = cls.repository(mysql)

        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)

        return jsonify(repo.get_list(request.args, page, limit))
