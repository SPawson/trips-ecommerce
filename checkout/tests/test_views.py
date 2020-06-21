from django.test import Client, RequestFactory, TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
import datetime
from django.contrib.auth.models import User, AnonymousUser
from checkout.views import checkout


class TestCheckoutViews(TestCase):
    """Class to test the various functions in the checkout view file"""

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.checkout_url = reverse('checkout')
        self.user = User.objects.create_user(username='TestUser', email="testuser@test.com", password="tester123")
    
    #Response tests
    def test_checkout_view_response_unauthenticated_redirects(self):
        request = self.factory.get(self.checkout_url)
        request.user = AnonymousUser()

        response = checkout(request)

        self.assertEquals(response.status_code, 302)

    def test_checkout_view_response_authenticated(self):
        request = self.factory.get(self.checkout_url)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = checkout(request)

        self.assertEquals(response.status_code, 302)
    
    def test_checkout_bad_form_data(self):
        form_data = {
            "firstname": "test",
            "lastname": "",
            "phone_number": "07896675463",
            "address1": "Test",
            "address2": "Test",
            "town_or_city": "Test",
            "postcode": "TE43 5TQ",
            "county": "Test",
            "country": "Test",
            "credit_card_number": "4242424242424234",
            "cvv": "876",
            "expiry_month": "7",
            "expiry_year": "2021",
            "stripe_id": "Test",
        }

        self.client.login(username='TestUser', password='tester123' )
        response = self.client.post(self.checkout_url,
                                form_data)
        self.assertEquals(response.status_code, 302)
        
