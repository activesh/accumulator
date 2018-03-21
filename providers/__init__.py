from typing import NamedTuple
from typing import Type
from .base import BaseProvider
from .github import GitHubProvider
from utils import parser
from exceptions import NoProviderFound

SUPPORTTED_PROVIDERS = {'github': GitHubProvider}


def get_provider_class(resource_name: str) -> Type[BaseProvider]:
    resource_name = resource_name.split('.')[0]
    if resource_name not in SUPPORTTED_PROVIDERS:
        raise NoProviderFound()

    return SUPPORTTED_PROVIDERS.get(resource_name)


def get_provider(url: str) -> BaseProvider:
    try:
        parsed: NamedTuple = parser.Parser(url).parse()
    except parser.ParserError:
        raise NoProviderFound()

    provider_class = get_provider_class(parsed.resource)  # type: ignore

    return provider_class()


__all__ = ('get_provider', 'BaseProvider')
