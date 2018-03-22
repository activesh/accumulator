class BaseProvider:

    def __init__(self, repo):
        self.repo = repo

    async def fetch(self):
        pass
