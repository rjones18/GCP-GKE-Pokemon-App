import json
import unittest
from main import app

class TestPokeapiApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_valid_pokemon(self):
        response = self.app.get('/pokemon/pikachu')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('name', data)
        self.assertIn('weight', data)
        self.assertIn('height', data)
        self.assertIn('types', data)
        self.assertIn('abilities', data)
        self.assertIn('sprite', data)
        self.assertIn('stats', data)

    def test_invalid_pokemon(self):
        response = self.app.get('/pokemon/invalid-pokemon-name')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Pokemon not found')

if __name__ == "__main__":
    unittest.main()

