""" Copy entity for the GMG project """
from src.entity.abstract_entity import AbstractEntity

class Copy(AbstractEntity):
    expected_fields = {
        'versionId': {
            'field': 'version_id',
            'method': '_version_id',
            'required': True,
            'type': 'int'
        },
        'original': {
            'field': 'is_original',
            'method': '_is_original',
            'required': True,
            'type': 'int'
        },
        'boxType': {
            'field': 'box_type',
            'method': '_box_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {'Big box', 'Cartridge box', 'Other', 'None'}
        },
        'casingType': {
            'field': 'casing_type',
            'method': '_casing_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {
                'DVD-like',
                'CD-like',
                'Cardboard sleeve',
                'Paper Sleeve',
                'Plastic Sleeve',
                'Other',
                'None'
            }
        },
        'onCompilation': {
            'field': 'on_compilation',
            'method': '_on_compilation',
            'required': True, 'type': 'int'
        },
        'reedition': {
            'field': 'is_reedition',
            'method': '_is_reedition',
            'required': True,
            'type': 'int'
        },
        'hasManual': {
            'field': 'has_manual',
            'method': '_has_manual',
            'required': True,
            'type': 'int'
        },
        'status': {
            'field': 'status',
            'method': '_status',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {'In', 'Out'}
        },
        'type': {
            'field': 'type',
            'method': '_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {
                'Physical',
                'Virtual',
            }
        },
        'comments': {
            'field': 'comments',
            'method': '_comments',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering = {
        'id': {'field': 'copy_id', 'origin': 'native', 'type': 'int'},
        'transactionCount': {'field': 'transactionCount', 'origin': 'computed', 'type': 'int'},
        'platformName': {'field': 'platformName', 'origin': 'computed', 'type': 'string'},
        'gameTitle': {'field': 'gameTitle', 'origin': 'computed', 'type': 'string'},
    }

    table_name = 'copies'
    primary_key = 'copy_id'

# If you change the order here, you need to also change it in the array above!
    def __init__(
            self,
            entity_id,
            version_id,
            is_original,
            box_type,
            casing_type,
            on_compilation,
            is_reedition,
            has_manual,
            status,
            type,
            comments,
            platform_name = None,
            game_title = None,
            transaction_count = None,
    ):
        self.entity_id = entity_id
        self.version_id = int(version_id)
        self.is_original = bool(is_original)
        self.box_type = box_type
        self.casing_type = casing_type
        self.on_compilation = bool(on_compilation)
        self.is_reedition = bool(is_reedition)
        self.has_manual = bool(has_manual)
        self.status = status
        self.type = type
        self.comments = comments
        self.platform_name = platform_name
        self.game_title = game_title
        self.transaction_count = int(transaction_count or 0)

    def get_id(self):
        return self.entity_id

    def get_version_id(self):
        return self.version_id

    def get_is_original(self):
        return self.is_original

    def get_box_type(self):
        return self.box_type

    def get_casing_type(self):
        return self.casing_type

    def get_on_compilation(self):
        return self.on_compilation

    def get_is_reedition(self):
        return self.is_reedition

    def get_has_manual(self):
        return self.has_manual

    def get_status(self):
        return self.status

    def get_type(self):
        return self.type

    def get_comments(self):
        return self.comments

    def set_version_id(self, version_id):
        self.version_id = version_id

    def set_is_original(self, is_original):
        self.is_original = bool(is_original)

    def set_box_type(self, type):
        self.box_type = type

    def set_casing_type(self, type):
        self.casing_type = type

    def set_on_compilation(self, status):
        self.on_compilation = bool(status)

    def set_is_reedition(self, status):
        self.is_reedition = bool(status)

    def set_has_manual(self, status):
        self.has_manual = bool(status)

    def set_status(self, status):
        self.status = status

    def set_type(self, type):
        self.type = type

    def set_comments(self, comments):
        self.comments = comments

    def get_game_title(self):
        return self.game_title

    def set_game_title(self, title):
        self.game_title = title

    def get_platform_name(self):
        return self.platform_name

    def set_platform_name(self, platform_name):
        self.platform_name = platform_name

    def get_transaction_count(self):
        return self.transaction_count

    def set_transaction_count(self, transaction_count):
        self.transaction_count = int(transaction_count or 0)

    def serialize(self):
        values = super().serialize()

        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()
        values['transactionCount'] = self.get_transaction_count()

        return values
