from .base import BaseProvider


class GitHubProvider(BaseProvider):

    async def fetch(self):
        print(f'fetching from {self.repo}')
