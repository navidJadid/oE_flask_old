import pytest
from webrob.app_and_db import app, db
import tutorial_test_constants as CONSTANTS
from webrob.models.tutorials import Tutorial, read_tutorial_page

backup_config = app.config['SQLALCHEMY_DATABASE_URI']

def create_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = CONSTANTS.TEST_DB_PATH

    db.drop_all()
    db.create_all()
    tut1 = Tutorial(cat_id = CONSTANTS.CAT_ID, cat_title = CONSTANTS.CAT_TITLE, title = CONSTANTS.TITLE_ONE,
                    text = CONSTANTS.TEXT_ONE, page = CONSTANTS.PAGE)
    tut2 = Tutorial(cat_id = CONSTANTS.CAT_ID, cat_title = CONSTANTS.CAT_TITLE, title = CONSTANTS.TITLE_TWO,
                    text = CONSTANTS.TEXT_TWO, page = CONSTANTS.PAGE)
    db.session.add(tut1)
    db.session.add(tut2)
    db.session.commit()

def test_read_tutorial_page():
    create_database()
    result = read_tutorial_page(CONSTANTS.CAT_ID, CONSTANTS.PAGE)
    assert result.title == CONSTANTS.TITLE_ONE
    app.config['SQLALCHEMY_DATABASE_URI'] = backup_config





