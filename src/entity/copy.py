""" Copy entity for the GMG project """
from typing import Any

from src.entity.abstract_entity import AbstractEntity


class Copy(AbstractEntity):
    expected_fields: dict[str, Any] = {
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
        'language': {
            'field': 'language',
            'method': '_language',
            'required': True,
            'type': 'string'
        },
        'boxType': {
            'field': 'box_type',
            'method': '_box_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {'Big box', 'Medium box', 'Special box', 'Cartridge box', 'Other', 'None'}
        },
        'isBoxRepro': {
            'field': 'is_box_repro',
            'method': '_is_box_repro',
            'required': True,
            'type': 'int'
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
                'Plastic tube',
                'Other',
                'None'
            }
        },
        'supportType': {
            'field': 'support_type',
            'method': '_support_type',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {
                'Blu-ray',
                'DVD-ROM',
                'CD-ROM',
                'GD-ROM',
                'MINI-Blu-ray',
                'MINI-DVD-ROM',
                'MINI-CD-ROM',
                'Cartridge',
                '3.5-inch floppy',
                '5.25-inch floppy',
                'Other disc',
                'Other floppy',
                'External drive',
                'None'
            }
        },
        'onCompilation': {
            'field': 'on_compilation',
            'method': '_on_compilation',
            'required': True,
            'type': 'int'
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
        'region': {
            'field': 'region',
            'method': '_region',
            'required': True,
            'type': 'strict-text',
            'allowed_values': {
                'PAL',
                'JAP',
                'NTSC',
                'CHINA'
            }
        },
        'comments': {
            'field': 'comments',
            'method': '_comments',
            'required': False,
            'type': 'text',
            'default': ''
        },
        'isROM': {
            'field': 'is_rom',
            'method': '_is_rom',
            'required': False,
            'type': 'int'
        },
    }

    authorized_extra_fields_for_filtering: dict[str, Any] = {
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
            entity_id: int | None,
            version_id: int,
            is_original: int,
            language: str,
            box_type: str,
            is_box_repro: int,
            casing_type: str,
            support_type: str,
            on_compilation: int,
            is_reedition: int,
            has_manual: int,
            status: str,
            type: str,
            region: str,
            comments: str,
            is_rom: int | None = None,
            platform_name: str | None = None,
            game_title: str | None = None,
            transaction_count: int | None = None,
    ) -> None:
        self.entity_id = entity_id
        self.version_id = int(version_id)
        self.is_original = bool(is_original)
        self.language = language
        self.box_type = box_type
        self.is_box_repro = bool(is_box_repro)
        self.casing_type = casing_type
        self.support_type = support_type
        self.on_compilation = bool(on_compilation)
        self.is_reedition = bool(is_reedition)
        self.has_manual = bool(has_manual)
        self.status = status
        self.type = type
        self.region = region
        self.is_rom = bool(is_rom)
        self.comments = comments
        self.platform_name = platform_name
        self.game_title = game_title
        self.transaction_count = int(transaction_count or 0)

    def get_id(self) -> int | None:
        return self.entity_id

    def get_version_id(self) -> int:
        return self.version_id

    def get_is_original(self) -> bool:
        return self.is_original

    def get_language(self) -> str:
        return self.language

    def get_box_type(self) -> str:
        return self.box_type

    def get_is_box_repro(self) -> bool:
        return bool(self.is_box_repro)

    def get_casing_type(self) -> str:
        return self.casing_type

    def get_support_type(self) -> str:
        return self.support_type

    def get_on_compilation(self) -> bool:
        return self.on_compilation

    def get_is_reedition(self) -> bool:
        return self.is_reedition

    def get_has_manual(self) -> bool:
        return self.has_manual

    def get_status(self) -> str:
        return self.status

    def get_type(self) -> str:
        return self.type

    def get_is_rom(self) -> bool:
        return self.is_rom

    def get_region(self) -> str:
        return self.region

    def get_comments(self) -> str:
        return self.comments

    def set_version_id(self, version_id: int) -> None:
        self.version_id = version_id

    def set_is_original(self, is_original: int) -> None:
        self.is_original = bool(is_original)

    def set_language(self, language: str) -> None:
        self.language = language

    def set_box_type(self, type: str) -> None:
        self.box_type = type

    def set_is_box_repro(self, is_repro: int) -> None:
        self.is_box_repro = bool(is_repro)

    def set_casing_type(self, type: str) -> None:
        self.casing_type = type

    def set_support_type(self, support_type: str) -> None:
        self.support_type = support_type

    def set_on_compilation(self, status: int) -> None:
        self.on_compilation = bool(status)

    def set_is_reedition(self, status: int) -> None:
        self.is_reedition = bool(status)

    def set_has_manual(self, status: int) -> None:
        self.has_manual = bool(status)

    def set_status(self, status: str) -> None:
        self.status = status

    def set_type(self, type: str) -> None:
        self.type = type

    def set_is_rom(self, is_rom: int) -> None:
        self.is_rom = bool(is_rom)

    def set_region(self, region: str) -> None:
        self.region = region

    def set_comments(self, comments: str) -> None:
        self.comments = comments

    def get_game_title(self) -> str | None:
        return self.game_title

    def set_game_title(self, title: str) -> None:
        self.game_title = title

    def get_platform_name(self) -> str | None:
        return self.platform_name

    def set_platform_name(self, platform_name: str) -> None:
        self.platform_name = platform_name

    def get_transaction_count(self) -> int:
        return self.transaction_count

    def set_transaction_count(self, transaction_count: int | None) -> None:
        self.transaction_count = int(transaction_count or 0)

    def serialize(self) -> dict[str, Any]:
        values = super().serialize()
        values['platformName'] = self.get_platform_name()
        values['gameTitle'] = self.get_game_title()
        values['transactionCount'] = self.get_transaction_count()
        return values
