import pytest
from webrob.utility.db_connection_checker import got_db_connection
from webrob.app_and_db import app,db
from flask_sqlalchemy import SQLAlchemy
from webrob.test.startup import init_app_test_constants as CONSTANTS
from webrob.startup.init_db import init_db

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
