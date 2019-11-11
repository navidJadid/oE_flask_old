import pytest
import os
from flask import Flask
from webrob.utility.db_connection_checker import got_db_connection
from webrob.app_and_db import app,db
from flask_sqlalchemy import SQLAlchemy
from webrob.test.startup import init_db_test_constants as CONSTANTS
from webrob.test.utility.db_connection_checker_test import MockAppLogger

backup_config = app.config[CONSTANTS.DATABASE_URI]


class MockDbEngineNormal:
    def __init__(self):
        self.cmd = "SELECT 1"

    def execute(self, command):
        # FIXME: Find way to remove hard-coding mock-method
        if command == self.cmd:
            app.config[CONSTANTS.DATABASE_URI] = CONSTANTS.TEST_DB_PATH
            return True
        else:
            raise Exception


class MockDbEngineRaiseError:
    def __init__(self):
        return

    def execute(self, command):
        app.config[CONSTANTS.DATABASE_URI] = CONSTANTS.TEST_DB_PATH
        raise Exception


MOCK_LOGGER = MockAppLogger()
MOCK_DB_ENGINE = MockDbEngineNormal()
MOCK_DB_ENGINE_MALFUNCTIONING = MockDbEngineRaiseError()

def check_db_file_path():
    import os.path
    if os.path.exists(CONSTANTS.DB_FILE):
        os.remove(CONSTANTS.DB_FILE)

@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setattr(Flask, 'logger', MOCK_LOGGER)

    return monkeypatch

# **************************TESTS****************************

def test_init_db_with_db_connection(monkeypatch_setup):
    check_db_file_path()
    from webrob.startup.init_db import init_db
    monkeypatch_setup.setattr(SQLAlchemy, 'engine', MOCK_DB_ENGINE)
    init_db(app,db)
    assert os.path.exists(CONSTANTS.DB_FILE) is True
    app.config[CONSTANTS.DATABASE_URI] = backup_config


def test_init_db_without_db_connection(monkeypatch_setup):
    check_db_file_path()
    from webrob.startup.init_db import init_db
    monkeypatch_setup.setattr(SQLAlchemy, 'engine', MOCK_DB_ENGINE_MALFUNCTIONING)
    init_db(app, db)
    assert os.path.exists(CONSTANTS.DB_FILE) is False
    app.config[CONSTANTS.DATABASE_URI] = backup_config





