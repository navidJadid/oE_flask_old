import pytest
from webrob.app_and_db import db
from webrob.models.tutorials import Tutorial
import webrob.models.tutorials as tutorials

MOCK_DB = list()
MOCK_DB  = [
             {
            'id': 1,
            'cat_id': 'robot programing',
            'cat_title': 'ros tutorial',
            'title': 'ros installation',
            'text': 'check ros documentation',
            'page': 1
            },

            {
                'id': 2,
                'cat_id': 'robot programing',
                'cat_title': 'ros tutorial',
                'title': 'ros installation',
                'text': 'check ros documentation',
                'page': 1
            }

        ]


class MockModel():
    def __init__(self, cat_id, page):
        self.cat_id = cat_id
        self.page = page

    def get_tutorial(self):
        result = list()
        result = [
             {
            'id': 1,
            'cat_id': self.cat_id,
            'cat_title': 'ros tutorial',
            'title': 'ros installation',
            'text': 'check ros documentation',
            'page': self.page
            },

            {
                'id': 2,
                'cat_id': self.cat_id,
                'cat_title': 'ros tutorial',
                'title': 'ros installation',
                'text': 'check ros documentation',
                'page': self.page
            }

        ]
        return result


def read_tuto_page(cat_id, page):
    MOCK_MODEL = MockModel(cat_id, page)
    output = MOCK_MODEL.get_tutorial()
    return output


@pytest.fixture
def monkeypatch_setup(monkeypatch):
    monkeypatch.setattr(tutorials, 'read_tutorial_page', read_tuto_page)

    return monkeypatch


def test_read_tutorial_page(monkeypatch_setup):
    result = tutorials.read_tutorial_page('robot programing', 1)
    assert result == MOCK_DB
