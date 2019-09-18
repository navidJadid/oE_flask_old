import pytest
import  webrob.config.settings
from webrob.config.settings import Config

MAIL_PASSWORD = 'abc'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'Paul'
FBOOK_APP_TOKENS = ("Paul01", "abCD123ef")
TWIT_APP_TOKENS = ("Paul01", "abCDef123hi")
GIT_APP_TOKENS = ("Paul01", "abCD-ef123hi")
GOOGLE_APP_TOKENS = ("Paul01", "abCD-ef123hi/456")
SERVICE_TOKENS = ("Paul01", "abCD-ef123hi/456")
ROS_DISTRIBUTION = 'indigo'


def oauth_token_mock(token_service_name):
    service_tokens = ('{}_APP_TOKENS'.format(token_service_name))
    service_tokens = ("Paul01", "abCD-ef123hi/456")
    return service_tokens

@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setenv('OPENEASE_MAIL_PASSWORD', MAIL_PASSWORD)
    monkeypatch.setenv('OPENEASE_MAIL_SERVER', MAIL_SERVER)
    monkeypatch.setenv('OPENEASE_MAIL_PORT', MAIL_PORT)
    monkeypatch.setenv('OPENEASE_MAIL_USE_TLS', MAIL_USE_TLS)
    monkeypatch.setenv('OPENEASE_MAIL_USE_SSL', MAIL_USE_SSL)
    monkeypatch.setenv('OPENEASE_MAIL_USERNAME', MAIL_USERNAME)
    monkeypatch.setenv('FACEBOOK_APP_ID', FBOOK_APP_TOKENS[0])
    monkeypatch.setenv('FACEBOOK_APP_SECRET', FBOOK_APP_TOKENS[1])
    monkeypatch.setenv('TWITTER_APP_ID', TWIT_APP_TOKENS[0])
    monkeypatch.setenv('TWITTER_APP_SECRET', TWIT_APP_TOKENS[1])
    monkeypatch.setenv('GITHUB_APP_ID', GIT_APP_TOKENS[0])
    monkeypatch.setenv('GITHUB_APP_SECRET', GIT_APP_TOKENS[1])
    monkeypatch.setenv('GOOGLE_APP_ID', GOOGLE_APP_TOKENS[0])
    monkeypatch.setenv('GOOGLE_APP_SECRET', GOOGLE_APP_TOKENS[1])
    monkeypatch.setenv('OPENEASE_ROS_DISTRIBUTION', ROS_DISTRIBUTION)


    # TODO: mock all other environment variables, so it does not need to be done twice
    return monkeypatch


# -------------------------------TESTS---------------------------------

# TODO:
#   add tests for all other environment variables

def test_variables_loaded():
    assert Config.config_variables_initialized() == False


def test_set_variables_loaded_to_true():
    Config._set_variables_loaded_to_true()
    assert Config._variables_loaded == True


def test_retrieve_mail_password(monkeypatch_setup):
    Config._retrieve_mail_password()
    assert Config.MAIL_PASSWORD == MAIL_PASSWORD


def test_retrieve_mail_password_error():
    with pytest.raises(KeyError):
        Config._retrieve_mail_password()


def test_retrieve_mail_server(monkeypatch_setup):
    Config._retrieve_mail_server()
    assert Config.MAIL_SERVER == MAIL_SERVER


def test_retrieve_mail_server_default():
    Config._retrieve_mail_server()
    assert Config.MAIL_SERVER == 'smtp.gmail.com'

def test_retrieve_mail_port(monkeypatch_setup):
    Config._retrieve_mail_port()
    assert Config.MAIL_PORT == MAIL_PORT

def test_retrieve_mail_port_default():
    Config._retrieve_mail_port()
    assert Config.MAIL_PORT == 465

def test_retrieve_mail_use_tls(monkeypatch_setup):
    Config._retrieve_mail_use_tls()
    assert Config.MAIL_USE_TLS == MAIL_USE_TLS

def test_retrieve_mail_use_tls_default():
    Config._retrieve_mail_use_tls()
    assert Config.MAIL_USE_TLS == True

def test_retrieve_mail_use_ssl(monkeypatch_setup):
    Config._retrieve_mail_use_ssl()
    assert  Config.MAIL_USE_SSL == MAIL_USE_SSL

def test_retrieve_mail_use_ssl_default():
    Config._retrieve_mail_use_ssl()
    assert Config.MAIL_USE_SSL == True

def test_retrieve_mail_username(monkeypatch_setup):
    Config._retrieve_mail_username()
    assert Config.MAIL_USERNAME == MAIL_USERNAME

def test_retrieve_facebook_tokens(monkeypatch_setup):
    Config._retrieve_facebook_tokens()
    assert Config.FACEBOOK_APP_TOKENS == FBOOK_APP_TOKENS

def test_retrieve_twitter_tokens(monkeypatch_setup):
    Config._retrieve_twitter_tokens()
    assert Config.TWITTER_APP_TOKENS == TWIT_APP_TOKENS

def test_retrieve_github_tokens(monkeypatch_setup):
    Config._retrieve_github_tokens()
    assert  Config.GITHUB_APP_TOKENS == GIT_APP_TOKENS

def test_retrieve_google_tokens(monkeypatch_setup):
    Config._retrieve_google_tokens()
    assert  Config.GOOGLE_APP_TOKENS == GOOGLE_APP_TOKENS

def test_retrieve_oauth_tokens(monkeypatch_setup):
    Config._retrieve_oauth_tokens()
    assert Config.FACEBOOK_APP_TOKENS == FBOOK_APP_TOKENS
    assert Config.TWITTER_APP_TOKENS == TWIT_APP_TOKENS
    assert  Config.GITHUB_APP_TOKENS == GIT_APP_TOKENS
    assert  Config.GOOGLE_APP_TOKENS == GOOGLE_APP_TOKENS

def test_retrieve_ros_distribution():
    Config._retrieve_ros_distribution()
    assert Config.ROS_DISTRIBUTION == ROS_DISTRIBUTION

def test_retrieve_mail_server_vars(monkeypatch_setup):
    Config._retrieve_mail_server_vars()
    assert Config.MAIL_SERVER == MAIL_SERVER
    assert Config.MAIL_PORT == MAIL_PORT
    assert Config.MAIL_USE_TLS == MAIL_USE_TLS
    assert  Config.MAIL_USE_SSL == MAIL_USE_SSL
    assert Config.MAIL_USERNAME == MAIL_USERNAME
    assert Config.MAIL_PASSWORD == MAIL_PASSWORD













