from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import add_to_cart, adjust_cart, view_cart

class TestCartUrls(TestCase):
    """Test the urls within the accounts app"""

    def test_add_to_cart_url_resolves(self):
        url = reverse("add_to_cart", args=(2,))
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_adjust_cart_url_resolves(self):
        url = reverse("adjust_cart", args=(2,))
        self.assertEqual(resolve(url).func, adjust_cart)

    def test_view_cart_url_resolves(self):
        url = reverse("view_cart")
        self.assertEqual(resolve(url).func, view_cart)

