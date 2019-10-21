# *******************DB Test Constants**********************

from webrob.models.tutorials import Tutorial as Tutorial

DB_COLUMNS = [{"name": "id", "type":Tutorial.id.type, "nullable":False}, {"name": "cat_id", "type":Tutorial.cat_id.type, "nullable":False}]
COLUMN_NAMES =['id', 'cat_id', 'cat_title', 'title', 'text', 'page']

