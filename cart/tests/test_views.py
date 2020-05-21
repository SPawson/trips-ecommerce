from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from cart.views import add_to_cart, adjust_cart, view_cart

#The following youtube tutorial was used to guide my testing process https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3

class TestCartViews(TestCase):
    """Test the views in the cart app"""

    def setUp(self):
        self.client = Client()
        self.add_to_cart_url = reverse('add_to_cart', args=(2,))
        self.adjust_cart_url = reverse('adjust_cart', args=(2,))
        self.view_cart_url = reverse('view_cart')
        self.data = {
            'quantity': '1'
        }
        self.factory = RequestFactory()
    
    #Response tests
    def test_add_to_cart_view_response(self):
        response = self.client.post(self.add_to_cart_url ,self.data)

        self.assertEquals(response.status_code, 302)
    
    def test_adjust_cart_view_response(self):
        response = self.client.post(self.adjust_cart_url, self.data)

        self.assertEquals(response.status_code, 302)

    def test_view_cart_view_response(self):
        response = self.client.get(self.view_cart_url)

        self.assertEquals(response.status_code, 200)
    
    
    #Returns correct templates tests
    
    def test_view_cart_view_returns_cart_overview_template(self):
        response = self.client.get(self.view_cart_url)

        self.assertTemplateUsed(response, 'cart-overview.html')


