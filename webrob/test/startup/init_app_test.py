import pytest
from webrob.utility.db_connection_checker import got_db_connection
from webrob.startup.init_app import _check_password_and_display_message_on_error
from webrob.app_and_db import app,db
from webrob.test.startup import init_app_test_constants as CONSTANTS
from flask_sqlalchemy import SQLAlchemy

def test_for_null_password():
    msg = _check_password_and_display_message_on_error(app,CONSTANTS.NAME, None)
    assert msg == False