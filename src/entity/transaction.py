from src.entity.abstract_entity import AbstractEntity

class Transaction(AbstractEntity):
    expected_fields = {
        'copyId': {'field': 'copy_id', 'method': '_copy_id', 'required': True, 'type': 'int'},
        'year': {'field': 'year', 'method': '_year', 'required': True, 'type': 'int'},
        'month': {'field': 'month', 'method': '_month', 'required': True, 'type': 'int'},
        'day': {'field': 'day', 'method': '_day', 'required': True, 'type': 'int'},
        'type': {
            'field': 'type',
            'method': '_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {
                'Bought', 'Sold',
                'Loan-out',
                'Loan-out-return',
                'Loan-in', 'Loan-in-return'
            }
        },
        'notes': {
            'field': 'notes',
            'method': '_notes',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    authorized_extra_fields_for_filtering = {
        'transaction_id'
    }

    table_name = 'transactions'
    primary_key = 'transaction_id'

    transaction_in = {'Bought', 'Loan-out-return', 'Loan-in',}
    transaction_out = {'Sold', 'Loan-out', 'Loan-in-return'}

    """ This class represent a transaction entry, for instance I sell or bought a game """
    def __init__(
            self,
            entity_id,
            copy_id,
            year,
            month,
            day,
            type,
            notes,
            platform_name = None,
            game_title = None,
    ):
        self.entity_id = entity_id
        self.copy_id = copy_id
        self.year = year
        self.month = month
        self.day = day
        self.type = type
        self.notes = notes
        self.platform_name = platform_name
        self.game_title = game_title

    def get_id(self):
        return self.entity_id

    def get_copy_id(self):
        return self.copy_id

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_type(self):
        return self.type

    def get_notes(self):
        return self.notes

    def set_copy_id(self, entity_id):
        self.copy_id = entity_id

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def set_type(self, type):
        self.type = type

    def set_notes(self, notes):
        self.notes = notes

    def get_game_title(self):
        return self.game_title

    def set_game_title(self, title):
        self.game_title = title

    def get_platform_name(self):
        return self.platform_name

    def set_platform_name(self, platform_name):
        self.platform_name = platform_name

    def serialize(self):
        values = super().serialize()

        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()

        return values
