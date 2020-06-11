from django.test import TestCase
from checkout.forms import MakePaymentForm, OrderForm

class TestForms(TestCase):
    """Test Checkout form functionality"""

    def test_order_form_passes_valid_data(self):
        form = OrderForm({"firstname": "test",
                        "lastname": "Test",
                        "phone_number": "07896675463",
                        "address1": "Test",
                        "address2": "Test",
                        "town_or_city": "Test",
                        "postcode": "TE43 5TQ",
                        "county": "Test",
                        "country": "Test",})
        self.assertTrue(form.is_valid())

    def test_order_form_fails_invalid_data(self):
        form = OrderForm({"firstname": "t",
                        "lastname": "Test",
                        "phone_number": "",
                        "address1": "Test",
                        "address2": "Test",
                        "town_or_city": "Test",
                        "postcode": "TE43 5TQ",
                        "county": "Test",
                        "country": "Test",})
        self.assertFalse(form.is_valid())

    def test_payment_form_passes_valid_data(self):
        form = MakePaymentForm({"credit_card_number": "4242424242424242",
                            "cvv": "876",
                            "expiry_month": "7",
                            "expiry_year": "2021",
                            "stripe_id": "Test",
                            })
        self.assertTrue(form.is_valid())
    
    def test_payment_form_fails_invalid_data(self):
        form = MakePaymentForm({"credit_card_number": "",
                            "cvv": "876",
                            "expiry_month": "07",
                            "expiry_year": "2021",
                            "stripe_id": "Test",
                            })
        self.assertFalse(form.is_valid())

