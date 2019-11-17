import pytest

from webrob.startup.init_app import _check_password_and_display_message_on_error
from webrob.app_and_db import app,db
from webrob.test.startup import init_app_test_constants as CONSTANTS
from flask_sqlalchemy import SQLAlchemy

backup_config = app.config[CONSTANTS.DATABASE_URI]

class MockDbEngineNormal:
    def __init__(self):
        self.cmd = "SELECT 1"

    def execute(self, command):
        # FIXME: Find way to remove hard-coding mock-method
        if command == self.cmd:
            return True
        else:
            raise Exception

MOCK_DB_ENGINE = MockDbEngineNormal()

@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setattr(SQLAlchemy, 'engine', MOCK_DB_ENGINE)
    return monkeypatch

def test_for_null_password():
    msg = _check_password_and_display_message_on_error(app,CONSTANTS.NAME, None)
    assert msg == False

def test_for_valid_password():
    msg = _check_password_and_display_message_on_error(app, CONSTANTS.NAME, CONSTANTS.PASSWORD)
    assert  msg == True
