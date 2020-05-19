from django import forms
from .models import Comment
import datetime

class CommentForm(forms.ModelForm):
    """Form for product comments"""

    # name = forms.CharField()
    # comment = forms.TextInput(None)
    post_date = forms.DateField(initial=datetime.date.today())

    class Meta:
        model = Comment
        fields = ('name', 'comment') 