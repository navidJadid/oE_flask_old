import pytest
from webrob.app_and_db import app
import tutorial_test_constants as CONSTANTS

backup_config = app.config['SQLALCHEMY_DATABASE_URI']


@pytest.fixture(scope="module")
def create_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test/models/tutotest.db'
    from webrob.app_and_db import db
    from webrob.models.tutorials import Tutorial, read_tutorial_page

    testDB = db
    testDB.create_all()
    tut1 = Tutorial(cat_id = CONSTANTS.CAT_ID, cat_title = CONSTANTS.CAT_TITLE, title = CONSTANTS.TITLE_ONE,
                    text = CONSTANTS.TEXT_ONE, page = CONSTANTS.PAGE)
    tut2 = Tutorial(cat_id = CONSTANTS.CAT_ID, cat_title = CONSTANTS.CAT_TITLE, title = CONSTANTS.TITLE_TWO,
                    text = CONSTANTS.TEXT_TWO, page = CONSTANTS.PAGE)
    testDB.session.add(tut1)
    testDB.session.add(tut2)
    testDB.session.commit()
    result = read_tutorial_page(CONSTANTS.CAT_ID, CONSTANTS.PAGE)

    yield result
    testDB.drop_all()
    app.config['SQLALCHEMY_DATABASE_URI'] = backup_config


def test_read_tutorial_page(create_database):
    result = create_database
    assert result.title == CONSTANTS.TITLE_ONE





