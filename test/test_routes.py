import unittest
from service import app
from tests.factories import ProductFactory
import json

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.product = ProductFactory()
        # Assume product is added to DB or mocked

    def test_read_product(self):
        response = self.client.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        data = {'name': 'New Product Name'}
        response = self.client.put(f'/products/{self.product.id}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('New Product Name', response.get_data(as_text=True))

    def test_delete_product(self):
        response = self.client.delete(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        response = self.client.get(f'/products?name={self.product.name}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_category(self):
        response = self.client.get(f'/products?category={self.product.category}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability(self):
        availability = 'true' if self.product.available else 'false'
        response = self.client.get(f'/products?available={availability}')
        self.assertEqual(response.status_code, 200)
