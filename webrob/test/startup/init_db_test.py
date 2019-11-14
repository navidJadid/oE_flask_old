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

def delete_existing_test_db_file():
    import os.path
    db_file = os.path.abspath(CONSTANTS.DB_FILE)
    if os.path.exists(db_file):
        os.remove(db_file)

@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setattr(Flask, 'logger', MOCK_LOGGER)

    return monkeypatch

# **************************TESTS****************************

def test_init_db_with_db_connection(monkeypatch_setup):
    delete_existing_test_db_file()
    from webrob.startup.init_db import init_db
    monkeypatch_setup.setattr(SQLAlchemy, 'engine', MOCK_DB_ENGINE)
    init_db(app,db)
    db_file = os.path.abspath(CONSTANTS.DB_FILE)
    assert os.path.exists(db_file) is True
    app.config[CONSTANTS.DATABASE_URI] = backup_config


def test_init_db_without_db_connection(monkeypatch_setup):
    delete_existing_test_db_file()
    from webrob.startup.init_db import init_db
    monkeypatch_setup.setattr(SQLAlchemy, 'engine', MOCK_DB_ENGINE_MALFUNCTIONING)
    init_db(app, db)
    db_file = os.path.abspath(CONSTANTS.DB_FILE)
    assert os.path.exists(db_file) is False
    app.config[CONSTANTS.DATABASE_URI] = backup_config





