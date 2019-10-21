import  pytest
from webrob.models.tutorials import Tutorial as Tutorial
from webrob.test.models import db_test_constants as CONSTANTS


def test_db_columns():
    from webrob.models.db import db_columns
    columns = db_columns(Tutorial)
    assert columns[1] == CONSTANTS.DB_COLUMNS[1]
    print 'priyanka'