""" Repository to handle the magazines """
from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.magazine import Magazine
from src.entity.magazine_issue import MagazineIssue


class MagazineRepository(AbstractRepository):
    entity = Magazine

    def get_select_request_start(self) -> str:
        request = f"SELECT {Magazine.table_name}.*, i.issueCount AS issueCount "
        request += 'FROM '
        request += f"     (SELECT COUNT(*) AS issueCount, {Magazine.table_name}.id AS magazine_id "
        request += f"      FROM {MagazineIssue.table_name}, {Magazine.table_name}  "
        request += f"      WHERE {MagazineIssue.table_name}.magazine_id = {Magazine.table_name}.{Magazine.primary_key} "
        request += f"      GROUP BY {Magazine.table_name}.{Magazine.primary_key}) AS i "
        request += f"RIGHT JOIN {Magazine.table_name} ON "
        request += f"{Magazine.table_name}.{Magazine.primary_key} = i.magazine_id WHERE TRUE "

        return request

    def get_by_title(self, title: str) -> Magazine | None:
        """Get one magazine by its title."""
        request = self.get_select_request_start() + f"AND {Magazine.table_name}.title = %s LIMIT 1;"

        return self.fetch_one(request, (title,))

    def hydrate(self, row: dict[str, Any]) -> Magazine:
        """Hydrate an object from a row."""
        magazine = super().hydrate(row)
        magazine.set_issue_count(row['issueCount'])

        return magazine
