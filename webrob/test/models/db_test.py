import  pytest
from webrob.models.tutorials import Tutorial as Tutorial
from webrob.test.models import db_test_constants as CONSTANTS

def test_db_columns():
    from webrob.models.db import db_columns
    columns = db_columns(Tutorial)
    assert columns[1] == CONSTANTS.DB_COLUMNS[1]

def test_db_column_names():
    from webrob.models.db import db_column_names
    column_names = db_column_names(Tutorial)
    assert column_names == CONSTANTS.COLUMN_NAMES

@pytest.mark.skip(reason="yet to resolve user_manager attribute problem")
def test_db_find_all():
    from webrob.app_and_db import app
    with app.app_context():
        from webrob.models.db import db_find_all
        out = db_find_all(Tutorial)


