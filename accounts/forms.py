from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    """User creation form which registers new users"""
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            'username': None,
        }

    def clean_username(self):
        """Checks the username for length"""
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError(u'Username must be more than 3 characters in length.')
        if len(username) > 40:
            raise forms.ValidationError(u'Username must be less than 40 characters in length.')
        return username

    def clean_email(self):
        """Checks email and username for uniqueness"""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password1(self):
        """ Validates password1 field"""
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError(u'Password is too short, it must be at least 8 characters.')
        if password1.isdigit():
            raise forms.ValidationError(u'Password cannot contain only numbers.')
        return password1

    def clean_password2(self):
        """ Validates password fields"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1"]


#Code snippets taken from Code Institutes Authentication Lesson