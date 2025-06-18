import unittest
from service.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Setup can create some fake products in memory or database mock
        self.product = ProductFactory()

    def test_create_product(self):
        self.assertIsNotNone(self.product.id)
        self.assertIsInstance(self.product.name, str)

    def test_read_product(self):
        product = Product.find_by_id(self.product.id)
        self.assertEqual(product.id, self.product.id)

    def test_update_product(self):
        self.product.name = "Updated Name"
        self.product.save()
        updated = Product.find_by_id(self.product.id)
        self.assertEqual(updated.name, "Updated Name")

    def test_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        self.assertIsNone(Product.find_by_id(product_id))

    def test_list_all_products(self):
        products = Product.list_all()
        self.assertTrue(len(products) > 0)

    def test_find_by_name(self):
        products = Product.find_by_name(self.product.name)
        self.assertTrue(any(p.name == self.product.name for p in products))

    def test_find_by_category(self):
        products = Product.find_by_category(self.product.category)
        self.assertTrue(all(p.category == self.product.category for p in products))

    def test_find_by_availability(self):
        products = Product.find_by_availability(self.product.available)
        self.assertTrue(all(p.available == self.product.available for p in products))
