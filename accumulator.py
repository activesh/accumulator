import asyncio
import uvloop
from providers import get_provider
from providers import BaseProvider


async def fetch_data(url: str) -> None:
    provider: BaseProvider = get_provider(url)
    await provider.fetch()


if __name__ == '__main__':
    """
    THIS IS FOR DEVELOPMENT PURPOSES ONLY
    =====================================

    In production, the loop and fetch_data will be callable from other scripts,
    for example, a Celery task. This file should not itself be executable.
    """
    asyncio.set_event_loop(uvloop.new_event_loop())
    fetch = fetch_data('git@github.com:ahopkins/sanic-jwt.git')
    loop = asyncio.get_event_loop()
    task = loop.create_task(fetch)
    loop.run_until_complete(asyncio.wait([task]))
