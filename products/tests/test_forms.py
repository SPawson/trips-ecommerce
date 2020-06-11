from django.test import TestCase
from products.forms import CommentForm

class TestForms(TestCase):
    """Test product form functionality"""

    def test_can_create_a_comment(self):
        form = CommentForm({"title": "test comment",
                             "like": "",
                             "comment": "This is a test comment"})
        self.assertTrue(form.is_valid())
    
    def test_can_create_a_comment_validation_fail(self):
        form = CommentForm({"title": "t",
                             "like": "",
                             "comment": ""})
        self.assertFalse(form.is_valid())
        
