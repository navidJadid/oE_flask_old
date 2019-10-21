# *******************DB Test Constants**********************

from webrob.app_and_db import db
from webrob.models.tutorials import Tutorial as Tutorial

DB_COLUMNS = [{"name": "id", "type":Tutorial.id.type, "nullable":False}, {"name": "cat_id", "type":Tutorial.cat_id.type, "nullable":False}]

