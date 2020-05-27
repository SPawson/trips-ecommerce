from django import forms
from .models import Comment
import datetime
from django.http import request

class CommentForm(forms.ModelForm):
    """Form for product comments"""

    class Meta:
        model = Comment
        fields = ('title','like', 'comment') 