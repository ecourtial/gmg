""" Repository to handle the magazine issues """
from typing import Any

from src.repository.abstract_repository import AbstractRepository
from src.entity.magazine_issue import MagazineIssue
from src.entity.magazine_issue_copy import MagazineIssueCopy
from src.entity.game_version_magazine_mention import GameVersionMagazineMention


class MagazineIssueRepository(AbstractRepository):
    entity = MagazineIssue

    def get_select_request_start(self) -> str:
        t = MagazineIssue.table_name
        pk = MagazineIssue.primary_key
        copies = MagazineIssueCopy.table_name
        mentions = GameVersionMagazineMention.table_name

        request = f"SELECT {t}.*, c.copyCount AS copyCount, m.mentionCount AS mentionCount "
        request += f"FROM {t} "
        request += f"LEFT JOIN (SELECT magazine_issue_id, COUNT(*) AS copyCount FROM {copies} GROUP BY magazine_issue_id) AS c ON c.magazine_issue_id = {t}.{pk} "
        request += f"LEFT JOIN (SELECT magazine_issue_id, COUNT(*) AS mentionCount FROM {mentions} GROUP BY magazine_issue_id) AS m ON m.magazine_issue_id = {t}.{pk} "
        request += f"WHERE {t}.{pk} IS NOT NULL "

        return request

    def hydrate(self, row: dict[str, Any]) -> MagazineIssue:
        issue = super().hydrate(row)
        issue.set_copy_count(row['copyCount'])
        issue.set_mention_count(row['mentionCount'])

        return issue

    def get_by_magazine_and_issue_number(self, magazine_id: int, issue_number: int) -> MagazineIssue | None:
        """Get one issue by its magazine and issue number."""
        request = self.get_select_request_start()
        request += f"AND {MagazineIssue.table_name}.magazine_id = %s "
        request += f"AND {MagazineIssue.table_name}.issue_number = %s LIMIT 1;"

        return self.fetch_one(request, (magazine_id, issue_number))
