import unittest
from app.my_app import ProductApp


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = ProductApp('abdul', '1234')
        self.test_id = 14
        self.test_product = {'product_id': self.test_id,
                             'properties': {
                                'title': "Non-Alcoholic Concentrated Perfume Oil",
                                'price': 120,
                                'rating': 4.23
                                }}

    def test_load_data(self):

        products = self.app.products

        self.assertIsNot(products, 'Not Allowed', 'Improper instantiation')

    def test_get_data(self):

        self.assertIsNotNone(self.app.get_data({'query': 'product', 'payload': {'id': self.test_id}}), 'Its None')

    def test_data_integrity(self):
        
        product = self.app.get_product(product_id=self.test_product.get('product_id'))

        self.assertEqual(self.test_product['properties']['title'], product['title'], 'Corrupted...')
        self.assertEqual(self.test_product['properties']['price'], product['price'], 'Corrupted...')
        self.assertEqual(self.test_product['properties']['rating'], product['rating'], 'Corrupted...')

if __name__ == "__main__":
    unittest.main()
