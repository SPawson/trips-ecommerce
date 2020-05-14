from django.test import TestCase
from django.urls import reverse, resolve
from products.views import return_products

class TestProductUrls(TestCase):
    """Test the urls within the products app"""

    def test_product_url_resolves(self):
        url = reverse("products")
        self.assertEqual(resolve(url).func, return_products)

