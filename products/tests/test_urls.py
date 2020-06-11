from django.test import TestCase
from django.urls import reverse, resolve
from products.views import return_products, product_detail, create_comment

class TestProductUrls(TestCase):
    """Test the urls within the products app"""

    def test_product_url_resolves(self):
        url = reverse("products")
        self.assertEqual(resolve(url).func, return_products)

    def test_product_detail_url_resolves(self):
        url = reverse("product_detail", kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, product_detail)

    def test_comment_url_resolves(self):
        url = reverse("create_comment", kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, create_comment)