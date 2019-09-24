import pytest
from  webrob.config import settings
from webrob.config.settings import Config
import pyjsonrpc
import webrob.test.config.settings_constants as CONSTANT

@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setenv('OPENEASE_MAIL_PASSWORD', CONSTANT.MAIL_PASSWORD)
    monkeypatch.setenv('OPENEASE_MAIL_SERVER', CONSTANT.MAIL_SERVER)
    monkeypatch.setenv('OPENEASE_MAIL_PORT', CONSTANT.MAIL_PORT)
    monkeypatch.setenv('OPENEASE_MAIL_USE_TLS', CONSTANT.MAIL_USE_TLS)
    monkeypatch.setenv('OPENEASE_MAIL_USE_SSL', CONSTANT.MAIL_USE_SSL)
    monkeypatch.setenv('OPENEASE_MAIL_USERNAME', CONSTANT.MAIL_USERNAME)
    monkeypatch.setenv('FACEBOOK_APP_ID', CONSTANT.FBOOK_APP_TOKENS[0])
    monkeypatch.setenv('FACEBOOK_APP_SECRET', CONSTANT.FBOOK_APP_TOKENS[1])
    monkeypatch.setenv('TWITTER_APP_ID', CONSTANT.TWIT_APP_TOKENS[0])
    monkeypatch.setenv('TWITTER_APP_SECRET', CONSTANT.TWIT_APP_TOKENS[1])
    monkeypatch.setenv('GITHUB_APP_ID', CONSTANT.GIT_APP_TOKENS[0])
    monkeypatch.setenv('GITHUB_APP_SECRET', CONSTANT.GIT_APP_TOKENS[1])
    monkeypatch.setenv('GOOGLE_APP_ID', CONSTANT.GOOGLE_APP_TOKENS[0])
    monkeypatch.setenv('GOOGLE_APP_SECRET', CONSTANT.GOOGLE_APP_TOKENS[1])
    monkeypatch.setenv('OPENEASE_ROS_DISTRIBUTION', CONSTANT.ROS_DISTRIBUTION)
    monkeypatch.setenv('POSTGRES_PORT_5432_TCP_ADDR', CONSTANT.POSTGRES_PORT_5432_TCP_ADDR)
    monkeypatch.setenv('POSTGRES_PORT_5432_TCP_PORT', CONSTANT.POSTGRES_PORT_5432_TCP_PORT)
    monkeypatch.setenv('OPENEASE_ROS_DISTRIBUTION', CONSTANT.ROS_DISTRIBUTION)

    monkeypatch.setenv('DOCKERBRIDGE_PORT_5001_TCP_ADDR', CONSTANT.DOCKBRIDGE_PORT_5001_TCP_ADDR)
    monkeypatch.setenv('DOCKERBRIDGE_PORT_5001_TCP_PORT', CONSTANT.DOCKBRIDGE_PORT_5001_TCP_PORT)

    # TODO: mock all other environment variables, so it does not need to be done twice
    return monkeypatch


# -------------------------------TESTS---------------------------------

# TODO:
#   add tests for all other environment variables

def test_oauth_token(monkeypatch_setup):
    token = Config._oauth_token('TWITTER')
    assert token == CONSTANT.TWIT_APP_TOKENS

def test_oauth_token_error():
    tokens = Config._oauth_token('TWITTER')
    assert tokens == (None,None)

def test_init_http_client(monkeypatch_setup):
    Config._init_http_client()
    assert type(Config.HTTP_CLIENT) is pyjsonrpc.HttpClient
    assert Config.HTTP_CLIENT.url == CONSTANT.URL

def test_init_http_client_error():
    with pytest.raises(KeyError):
        Config._init_http_client()

def test_variables_loaded():
    assert Config.config_variables_initialized() == False


def test_set_variables_loaded_to_true():
    Config._set_variables_loaded_to_true()
    assert Config._variables_loaded == True


def test_retrieve_mail_password(monkeypatch_setup):
    Config._retrieve_mail_password()
    assert Config.MAIL_PASSWORD == CONSTANT.MAIL_PASSWORD


def test_retrieve_mail_password_error():
    with pytest.raises(KeyError):
        Config._retrieve_mail_password()

def test_retrieve_sqlalchemy_db_uri(monkeypatch_setup):
    Config._retrieve_sqlalchemy_db_uri()
    assert Config.SQLALCHEMY_DATABASE_URI == CONSTANT.SQLALCHEMY_DATABASE_URI

def test_retrieve_sqlalchemy_db_uri_error():
    with pytest.raises(KeyError):
        Config._retrieve_sqlalchemy_db_uri()

def test_retrieve_mail_server(monkeypatch_setup):
    Config._retrieve_mail_server()
    assert Config.MAIL_SERVER == CONSTANT.MAIL_SERVER


def test_retrieve_mail_server_default():
    Config._retrieve_mail_server()
    assert Config.MAIL_SERVER == 'smtp.gmail.com'

def test_retrieve_mail_port(monkeypatch_setup):
    Config._retrieve_mail_port()
    assert Config.MAIL_PORT == CONSTANT.MAIL_PORT

def test_retrieve_mail_port_default():
    Config._retrieve_mail_port()
    assert Config.MAIL_PORT == 465

def test_retrieve_mail_use_tls(monkeypatch_setup):
    Config._retrieve_mail_use_tls()
    assert Config.MAIL_USE_TLS == CONSTANT.MAIL_USE_TLS

def test_retrieve_mail_use_tls_default():
    Config._retrieve_mail_use_tls()
    assert Config.MAIL_USE_TLS == True

def test_retrieve_mail_use_ssl(monkeypatch_setup):
    Config._retrieve_mail_use_ssl()
    assert  Config.MAIL_USE_SSL == CONSTANT.MAIL_USE_SSL

def test_retrieve_mail_use_ssl_default():
    Config._retrieve_mail_use_ssl()
    assert Config.MAIL_USE_SSL == True

def test_retrieve_mail_username(monkeypatch_setup):
    Config._retrieve_mail_username()
    assert Config.MAIL_USERNAME == CONSTANT.MAIL_USERNAME

def test_retrieve_mail_username_error():
    Config._retrieve_mail_username()
    assert Config.MAIL_USERNAME == None

def test_retrieve_facebook_tokens(monkeypatch_setup):
    Config._retrieve_facebook_tokens()
    assert Config.FACEBOOK_APP_TOKENS == CONSTANT.FBOOK_APP_TOKENS

def test_retrieve_facebook_tokens_error():
    Config._retrieve_facebook_tokens()
    assert  Config.FACEBOOK_APP_TOKENS == (None,None)

def test_retrieve_twitter_tokens(monkeypatch_setup):
    Config._retrieve_twitter_tokens()
    assert Config.TWITTER_APP_TOKENS == CONSTANT.TWIT_APP_TOKENS

def test_retrieve_twitter_tokens_error():
    Config._retrieve_twitter_tokens()
    assert Config.TWITTER_APP_TOKENS == (None, None)

def test_retrieve_github_tokens(monkeypatch_setup):
    Config._retrieve_github_tokens()
    assert  Config.GITHUB_APP_TOKENS == CONSTANT.GIT_APP_TOKENS

def test_retrieve_github_tokens_error():
    Config._retrieve_github_tokens()
    assert Config.GITHUB_APP_TOKENS == (None, None)

def test_retrieve_google_tokens(monkeypatch_setup):
    Config._retrieve_google_tokens()
    assert  Config.GOOGLE_APP_TOKENS == CONSTANT.GOOGLE_APP_TOKENS

def test_retrieve_google_tokens_error():
    Config._retrieve_google_tokens()
    assert Config.GOOGLE_APP_TOKENS == (None, None)

def test_retrieve_oauth_tokens(monkeypatch_setup):
    Config._retrieve_oauth_tokens()
    assert Config.FACEBOOK_APP_TOKENS == CONSTANT.FBOOK_APP_TOKENS
    assert Config.TWITTER_APP_TOKENS == CONSTANT.TWIT_APP_TOKENS
    assert  Config.GITHUB_APP_TOKENS == CONSTANT.GIT_APP_TOKENS
    assert  Config.GOOGLE_APP_TOKENS == CONSTANT.GOOGLE_APP_TOKENS

def test_oauth_tokens_with_default_none():
    Config._retrieve_oauth_tokens()
    assert Config.FACEBOOK_APP_TOKENS == (None,None)
    assert Config.TWITTER_APP_TOKENS == (None, None)
    assert Config.GITHUB_APP_TOKENS == (None, None)
    assert Config.GOOGLE_APP_TOKENS == (None, None)

def test_retrieve_ros_distribution(monkeypatch_setup):
    Config._retrieve_ros_distribution()
    assert Config.ROS_DISTRIBUTION == CONSTANT.ROS_DISTRIBUTION

def test_retrieve_ros_distribution_default():
    Config._retrieve_ros_distribution()
    assert Config.ROS_DISTRIBUTION == CONSTANT.ROS_DISTRIBUTION

def test_retrieve_mail_server_vars(monkeypatch_setup):
    Config._retrieve_mail_server_vars()
    assert Config.MAIL_SERVER == CONSTANT.MAIL_SERVER
    assert Config.MAIL_PORT == CONSTANT.MAIL_PORT
    assert Config.MAIL_USE_TLS == CONSTANT.MAIL_USE_TLS
    assert  Config.MAIL_USE_SSL == CONSTANT.MAIL_USE_SSL
    assert Config.MAIL_USERNAME == CONSTANT.MAIL_USERNAME
    assert Config.MAIL_PASSWORD == CONSTANT.MAIL_PASSWORD













