from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout

class TestCheckoutUrls(TestCase):
    """Test the urls within the products app"""

    def test_product_url_resolves(self):
        url = reverse("checkout")
        self.assertEqual(resolve(url).func, checkout)