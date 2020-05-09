from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.views import register, login, logout

#The following youtube tutorial was used to guide my testing process https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3

class TestAccountViews(TestCase):
    """Test the views in the account app"""

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username='TestUser', email="testuser@test.com", password="tester123")
        self.factory = RequestFactory()
    
    #Response tests
    def test_register_view_response(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
    
    def test_login_view_response(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)

    def test_logout_view_response(self):
        request = self.factory.get(self.logout_url)
        request.user = self.user
        response = logout(request)

        self.assertEquals(response.status_code, 200)
    
    
    #Returns correct templates tests
    def test_register_view_returns_register_template(self):
        response = self.client.get(self.register_url)

        self.assertTemplateUsed(response, 'register.html')
    
    def test_login_view_returns_logout_template(self):
        response = self.client.get(self.login_url)

        self.assertTemplateUsed(response, 'login.html')
    
    def test_logout_view_returns_index_template(self):
        response = self.client.get(self.logout_url)

        self.assertTemplateUsed(response, 'index.html')


