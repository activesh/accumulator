import asyncio
import uvloop
from providers import BaseProvider
from providers import GitHubProvider


def get_provider(url: str) -> BaseProvider:
    return GitHubProvider()


async def fetch_data(url: str) -> None:
    provider = get_provider(url)
    provider.fetch()


if __name__ == '__main__':
    asyncio.set_event_loop(uvloop.new_event_loop())
    loop = asyncio.get_event_loop()
    main()
