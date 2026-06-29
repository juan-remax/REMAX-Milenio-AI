import asyncio

from github import Github, GithubException
from loguru import logger

from src.config.settings import settings


class GitHubService:
    def __init__(self):
        self._client = None
        self._repo = None

    def _ensure_client(self):
        if self._client is None and settings.github_token:
            self._client = Github(settings.github_token)
            self._repo = self._client.get_repo(settings.github_repo)
        return self._client is not None

    async def create_issue(self, title: str, body: str, labels: list[str] | None = None) -> str:
        if not self._ensure_client():
            return "⚠️ GitHub no configurado. Añade GITHUB_TOKEN en .env"

        try:
            issue = await asyncio.to_thread(
                self._repo.create_issue, title=title, body=body, labels=labels or []
            )
            logger.info(f"Issue created: #{issue.number} - {title}")
            return f"✅ Issue creado: #{issue.number} - {issue.html_url}"
        except GithubException as e:
            logger.error(f"Error creating issue: {e}")
            return f"❌ Error al crear issue: {e}"

    async def list_open_issues(self) -> list[dict]:
        if not self._ensure_client():
            return []

        try:
            issues = await asyncio.to_thread(self._repo.get_issues, state="open")
            return [{"number": i.number, "title": i.title, "url": i.html_url} for i in issues]
        except GithubException:
            return []


github_service = GitHubService()
