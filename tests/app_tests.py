import unittest
import json
from app import app


class My_TestClass(unittest.TestCase):

    data = [{'date': "21/07/2017", 'description': 'lorem ipsum', 'entry_id': 1, 'title': 'jonathan in never land'}]

    def setUp(self):
        self.app = app.test_client()
        self.entry_id = [1]

    def test_entry(self):
        """tests for all entries in the data storage"""
        response =  self.app.get('/api/v2/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_single_entry(self):
        """ tests for a single entry """
        pos = self.app.post('/api/v2/entries',  data=json.dumps({'description': 'lorem ipsum'}), content_type='application/json')
        self.assertEqual(pos.status_code, 200)
        resp = self.app.get('/api/v2/entries/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_add_one(self):
        """ tests for adding a single entry """
        resp = self.app.get('/api/v2/entries')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

    def test_edit_one(self):
        """ tests for editing a single entry """
        resp = self.app.put('/api/v2/entries/1', data=json.dumps(dict(description='advkbfsdkjbv',title='first safari')),content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_delete_one(self):
        """ tests for deleting a single entry """
        pos = self.app.post('/api/v2/entries',  data=json.dumps({'description': 'lorem ipsum'}), content_type='application/json')
        self.assertEqual(pos.status_code, 200)
        resp = self.app.delete('/api/v2/entries/1')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
       
if __name__ == '__main__':
    unittest.main()