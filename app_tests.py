import unittest 
import json
from app import app

class My_TestClass (unittest.TestCase):
	def setup(self):
		self.app = app.app.test_client()
		self.entry_id = 1

	def test_entry(self):
		response = self.app.get('/api/v1/entries')
		self.assertEqual(response.status_code, 200) 	
		self.assertEqual(response.content_type, 'application/json')
