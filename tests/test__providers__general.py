from providers import get_provider
from providers import BaseProvider
from exceptions import NoProviderFound

# from providers.github import GitHubProvider
import pytest


@pytest.fixture
def github_repo_strings():
    return [
        'git@github.com:ahopkins/sanic-jwt.git',
        'https://github.com/ahopkins/sanic-jwt.git',
        'https://github.com/ahopkins/sanic-jwt',
    ]


@pytest.fixture
def repo_strings(github_repo_strings):
    return github_repo_strings


@pytest.fixture
def invalid_repo_strings():
    return [
        'https://github.com/ahopkins', 'https://github.com', 'somerandomtext'
    ]


def test__get_provider__returns_provider(repo_strings):
    for repo in repo_strings:
        provider = get_provider(repo)
        assert isinstance(provider, BaseProvider)


def test__get_provider__raises_exception_on_invalid(invalid_repo_strings):
    for repo in invalid_repo_strings:
        with pytest.raises(NoProviderFound):
            get_provider(repo)
