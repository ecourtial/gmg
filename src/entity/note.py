from src.entity.abstract_entity import AbstractEntity

class Note(AbstractEntity):
    expected_fields = {
        'title': {
            'field': 'title',
            'method': '_title',
            'required': True,
            'type': 'text',
            'default': ''
        },
        'content': {
            'field': 'content',
            'method': '_content',
            'required': False,
            'type': 'text',
            'default': ''
        },
    }

    table_name = 'notes'
    primary_key = 'id'

    """ This class represent a note entry """
    def __init__(
            self,
            entity_id,
            title,
            content,
    ):
        self.entity_id = entity_id
        self.title = title
        self.content = content

    def get_id(self):
        return self.entity_id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def serialize(self):
        values = super().serialize()

        return values
