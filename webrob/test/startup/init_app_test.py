import pytest

from webrob.app_and_db import app
from webrob.startup.init_app import _check_password_and_display_message_on_error

from webrob.test.startup import init_app_test_constants as CONSTANTS


backup_config = app.config[CONSTANTS.DATABASE_URI]

def test_for_null_password():
    msg = _check_password_and_display_message_on_error(app,CONSTANTS.NAME, None)
    assert msg == False

def test_for_valid_password():
    msg = _check_password_and_display_message_on_error(app, CONSTANTS.NAME, CONSTANTS.PASSWORD)
    assert  msg == True



