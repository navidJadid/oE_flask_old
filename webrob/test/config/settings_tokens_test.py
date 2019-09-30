import pytest
from webrob.config.settings import Config
import webrob.test.config.settings_constants as CONSTANT


@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setenv('FACEBOOK_APP_ID', CONSTANT.FBOOK_APP_TOKENS[0])
    monkeypatch.setenv('FACEBOOK_APP_SECRET', CONSTANT.FBOOK_APP_TOKENS[1])
    monkeypatch.setenv('TWITTER_APP_ID', CONSTANT.TWIT_APP_TOKENS[0])
    monkeypatch.setenv('TWITTER_APP_SECRET', CONSTANT.TWIT_APP_TOKENS[1])
    monkeypatch.setenv('GITHUB_APP_ID', CONSTANT.GIT_APP_TOKENS[0])
    monkeypatch.setenv('GITHUB_APP_SECRET', CONSTANT.GIT_APP_TOKENS[1])
    monkeypatch.setenv('GOOGLE_APP_ID', CONSTANT.GOOGLE_APP_TOKENS[0])
    monkeypatch.setenv('GOOGLE_APP_SECRET', CONSTANT.GOOGLE_APP_TOKENS[1])

    return monkeypatch

# *******************TOKEN TESTS********************

def test_oauth_token(monkeypatch_setup):
    token = Config._oauth_token('TWITTER')
    assert token == CONSTANT.TWIT_APP_TOKENS

def test_oauth_token_with_default_none():
    tokens = Config._oauth_token('TWITTER')
    assert tokens == CONSTANT.NULL_TOKENS

def test_retrieve_facebook_tokens(monkeypatch_setup):
    Config._retrieve_facebook_tokens()
    assert Config.FACEBOOK_APP_TOKENS == CONSTANT.FBOOK_APP_TOKENS

def test_facebook_tokens_without_default():
    Config._retrieve_facebook_tokens()
    assert  Config.FACEBOOK_APP_TOKENS == CONSTANT.NULL_TOKENS

def test_retrieve_twitter_tokens(monkeypatch_setup):
    Config._retrieve_twitter_tokens()
    assert Config.TWITTER_APP_TOKENS == CONSTANT.TWIT_APP_TOKENS

def test_twitter_tokens_with_default_none():
    Config._retrieve_twitter_tokens()
    assert Config.TWITTER_APP_TOKENS == CONSTANT.NULL_TOKENS

def test_retrieve_github_tokens(monkeypatch_setup):
    Config._retrieve_github_tokens()
    assert  Config.GITHUB_APP_TOKENS == CONSTANT.GIT_APP_TOKENS

def test_github_tokens_with_default_none():
    Config._retrieve_github_tokens()
    assert Config.GITHUB_APP_TOKENS == CONSTANT.NULL_TOKENS

def test_retrieve_google_tokens(monkeypatch_setup):
    Config._retrieve_google_tokens()
    assert  Config.GOOGLE_APP_TOKENS == CONSTANT.GOOGLE_APP_TOKENS

def test_google_tokens_with_default_none():
    Config._retrieve_google_tokens()
    assert Config.GOOGLE_APP_TOKENS == CONSTANT.NULL_TOKENS

def test_retrieve_oauth_tokens(monkeypatch_setup):
    Config._retrieve_oauth_tokens()
    assert Config.FACEBOOK_APP_TOKENS == CONSTANT.FBOOK_APP_TOKENS
    assert Config.TWITTER_APP_TOKENS == CONSTANT.TWIT_APP_TOKENS
    assert  Config.GITHUB_APP_TOKENS == CONSTANT.GIT_APP_TOKENS
    assert  Config.GOOGLE_APP_TOKENS == CONSTANT.GOOGLE_APP_TOKENS

def test_retrieve_oauth_tokens_with_default_none():
    Config._retrieve_oauth_tokens()
    assert Config.FACEBOOK_APP_TOKENS == CONSTANT.NULL_TOKENS
    assert Config.TWITTER_APP_TOKENS == CONSTANT.NULL_TOKENS
    assert Config.GITHUB_APP_TOKENS == CONSTANT.NULL_TOKENS
    assert Config.GOOGLE_APP_TOKENS == CONSTANT.NULL_TOKENS
