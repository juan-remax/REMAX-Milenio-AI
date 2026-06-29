from github import Github, GithubException
from loguru import logger

from src.config.settings import settings


class GitHubService:
    def __init__(self):
        self.client = None
        self.repo = None
        if settings.github_token:
            self.client = Github(settings.github_token)
            self.repo = self.client.get_repo(settings.github_repo)

    async def create_issue(self, title: str, body: str, labels: list[str] | None = None) -> str:
        if not self.client:
            return "⚠️ GitHub no configurado. Añade GITHUB_TOKEN en .env"

        try:
            issue = self.repo.create_issue(title=title, body=body, labels=labels or [])
            logger.info(f"Issue created: #{issue.number} - {title}")
            return f"✅ Issue creado: #{issue.number} - {issue.html_url}"
        except GithubException as e:
            logger.error(f"Error creating issue: {e}")
            return f"❌ Error al crear issue: {e}"

    async def list_open_issues(self) -> list[dict]:
        if not self.client:
            return []

        issues = self.repo.get_issues(state="open")
        return [{"number": i.number, "title": i.title, "url": i.html_url} for i in issues]


github_service = GitHubService()
