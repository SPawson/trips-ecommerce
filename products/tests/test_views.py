from django.test import Client, RequestFactory, TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
import datetime
from django.contrib.auth.models import User
from products.views import return_products, create_comment, return_categories, return_countries, is_valid_query, return_comments, product_detail
from products.models import Product, Country, Category, Comment

class TestProductViews(TestCase):
    """Class to test the various functions in the product view file"""

    def setUp(self):
        self.client = Client()
        self.product_url = reverse('products')
        self.product_detail_url = reverse("product_detail", kwargs={'pk': 1})
        self.create_comment_url = reverse("create_comment", kwargs={'pk': 1})
        self.factory = RequestFactory()
        self.country = Country.objects.create(name= "England")
        self.category = Category.objects.create(name="sports")
        self.user = User.objects.create_user(username='TestUser', email="testuser@test.com", password="tester123")
        self.product = Product.objects.create(name= "Test Product",
                                description= "test description",
                                location= "test town",
                                country= self.country,
                                price= 50.00,
                                start_date= datetime.date.today(),
                                end_date= datetime.date.today(),
                                category= self.category,
                                latitude= 51.5074,
                                longitude= 0.1278,
                                likes= 2)
        self.comment = Comment.objects.create(title= "test comment",
                                            comment="this is a test comment",
                                            like= True,
                                            post_date= datetime.date.today(),
                                            product_id= self.product,
                                            user_id= self.user)
        

    #Response tests
    def test_product_view_response(self):
        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)
    
    def test_product_detail_view_response(self):
        response = self.client.get(self.product_detail_url)

        self.assertEquals(response.status_code, 200)

    def test_create_comment_response(self):
        response = self.client.get(self.create_comment_url)

        self.assertEquals(response.status_code, 302)

    #Returns correct Template
    def test_product_view_returns_products_template(self):
        response = self.client.get(self.product_url)

        self.assertTemplateUsed(response, 'products.html')
    
    #test view helper functions
    def test_is_valid_query(self):
        test = is_valid_query("highest")
        
        self.assertTrue(test)
    
    def test_is_valid_query_invalid(self):
        test = is_valid_query("")
        
        self.assertFalse(test)
    
    def test_return_categories(self):
        categories = return_categories()
        self.assertTrue(len(categories) == 1)
    
    def test_return_countries(self):
        countries = return_countries()
        self.assertTrue(len(countries) == 1)
    
    def test_return_comments(self):
        comments = return_comments(1)
        self.assertTrue(len(comments) == 1)

    def test_create_comment(self):
        form_data = {
            "title": "test comment",
            "like": "",
            "comment": "This is a test comment"
        }

        self.client.login()
        response = self.client.post(self.create_comment_url,
                                form_data)

        self.assertEqual(response.status_code, 302)

    def test_return_product_detail(self):
        request = RequestFactory().get(self.product_detail_url)

        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
    
        response = product_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)
    
    def test_return_product_listing(self):
        request = RequestFactory().get(self.product_url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = return_products(request)
        
        self.assertEqual(response.status_code, 200)
