from flask import request, jsonify
from src.exception.inconsistent_operation import InconsistentOperation
from src.exception.missing_field_exception import MissingFieldException
from src.exception.resource_already_exists_exception import ResourceAlreadyExistsException
from src.exception.resource_has_children_exception import RessourceHasChildrenException
from src.exception.unknown_resource_exception import ResourceNotFoundException
from src.exception.unsupported_value_exception import UnsupportedValueException

class AbstractController:
    @classmethod
    def get_by_id(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            copy = service.get_by_id(entity_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404

        return jsonify(copy.serialize()), 200

    @classmethod
    def create(cls, mysql):
        service = cls.service(mysql)

        try:
            object = service.validate_payload_for_creation_and_hydrate()
        except UnsupportedValueException as e:
            return jsonify({'message': str(e)}), 400
        except MissingFieldException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400
        except InconsistentOperation as e:
            return jsonify({'message': str(e)}), 400
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404

        repo = cls.repository(mysql)
        object = repo.insert(object)

        return cls.get_by_id(mysql, object.get_id())

    @classmethod
    def update(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            object = service.validate_payload_for_update_and_hydrate(entity_id)
        except UnsupportedValueException as e:
            return jsonify({'message': str(e)}), 400
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except ResourceAlreadyExistsException as e:
            return jsonify({'message': str(e)}), 400
        except InconsistentOperation as e:
            return jsonify({'message': str(e)}), 400

        repo = cls.repository(mysql)
        object = repo.update(object)

        return cls.get_by_id(mysql, object.get_id())

    @classmethod
    def delete(cls, mysql, entity_id):
        service = cls.service(mysql)

        try:
            service.delete(entity_id)
        except ResourceNotFoundException as e:
            return jsonify({'message': str(e)}), 404
        except RessourceHasChildrenException as e:
            return jsonify({'message': str(e)}), 400

        return jsonify({'message': service.resource_type + ' successfully deleted.'}), 200

    @classmethod
    def get_list(cls, mysql):
        repo = cls.repository(mysql)
        
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 30)
        order_by = request.args.get('order_by', '')
        order = request.args.get('order', '')

        return jsonify(repo.get_list(request.args, page, limit, order_by, order))
