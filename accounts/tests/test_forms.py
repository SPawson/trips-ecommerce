from django.test import TestCase
from accounts.forms import UserRegistrationForm, UserLoginForm

class TestRegisterForm(TestCase):
    """Test register form functionality"""

    def test_can_create_a_user(self):
        form = UserRegistrationForm({"email": "testuser@gmail.com", "username": "TestUser", "password1": "testpassword", "password2": "testpassword"})
        self.assertTrue(form.is_valid())
        
    #registration form test
    def test_registration_form_fails_invalid_data(self):

        form = UserRegistrationForm({"email": "testuseremail", "username": "TestUser", "password1": "testpassword", "password2": "testpassword"})
        self.assertFalse(form.is_valid())
    
    def test_login_form_fails_invalid_data(self):
        form = UserLoginForm({"username": "TestUser", "password1": "t"})
        self.assertFalse(form.is_valid())


