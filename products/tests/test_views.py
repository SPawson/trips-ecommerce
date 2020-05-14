from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from products.views import return_products, return_categories, return_countries, is_valid_query


class TestProductViews(TestCase):
    """Class to test the various functions in the product view file"""

    def setUp(self):
        self.client = Client()
        self.product_url = reverse('products')
        self.factory = RequestFactory()

    #Response tests
    def test_product_view_response(self):
        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)

    #Returns correct Template
    def test_product_view_returns_products_template(self):
        response = self.client.get(self.product_url)

        self.assertTemplateUsed(response, 'products.html')