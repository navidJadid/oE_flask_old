import pytest

from webrob.config.settings import Config

MAIL_PASSWORD = 'abc'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'Paul'


@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setenv('OPENEASE_MAIL_PASSWORD', MAIL_PASSWORD)
    monkeypatch.setenv('OPENEASE_MAIL_SERVER', MAIL_SERVER)
    monkeypatch.setenv('OPENEASE_MAIL_PORT', MAIL_PORT)
    monkeypatch.setenv('OPENEASE_MAIL_USE_TLS', MAIL_USE_TLS)
    monkeypatch.setenv('OPENEASE_MAIL_USE_SSL', MAIL_USE_SSL)
    monkeypatch.setenv('OPENEASE_MAIL_USERNAME', MAIL_USERNAME)

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

# def test_retrieve_mail_username_error():
#     with pytest.raises(KeyError):
#         Config._retrieve_mail_username()
