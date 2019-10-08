import pytest
from webrob.app_and_db import app

backup_config = app.config['SQLALCHEMY_DATABASE_URI']
CAT_ID = 'robot programming'
PAGE = 1

TUTORIAL_TITLE = 'ros installation'

@pytest.fixture(scope="module")
def create_database():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test/models/tutotest.db'
    from webrob.app_and_db import db
    from webrob.models.tutorials import Tutorial, read_tutorial_page

    testDB = db
    testDB.create_all()
    tut1 = Tutorial(cat_id='robot programming', cat_title='ros tutorial', title='ros installation',
                    text='check ros documentation', page=1)
    tut2 = Tutorial(cat_id='robot programming', cat_title='ros tutorial', title='getting started',
                    text='installing and configuring ros workspace', page=1)
    testDB.session.add(tut1)
    testDB.session.add(tut2)
    testDB.session.commit()
    result = read_tutorial_page(CAT_ID,PAGE)

    yield result
    testDB.drop_all()
    app.config['SQLALCHEMY_DATABASE_URI'] = backup_config


def test_read_tutorial_page(create_database):
    result = create_database
    assert result.title == TUTORIAL_TITLE





