"""Tests"""

import unittest
from src.app import app
from src.config import OK_STATUS, BAD_REQUEST

app.config['DEBUG'] = True
app.config['TESTING'] = True

class TestApp(unittest.TestCase):
    """Unittest class"""
    def setUp(self) -> None:
        self.headers = {'Content-type': 'application/json'}
        return super().setUp()

    def test_test(self):
        response = app.test_client().get('/test')
        assert response.status_code == OK_STATUS
        assert response.json == {'TEST': 'OK'}
    
    def test_post(self):
        data = {"hello": "world"}
        response = app.test_client().post('/test/post', json=data)
        assert response.status_code == OK_STATUS
        assert response.json == data