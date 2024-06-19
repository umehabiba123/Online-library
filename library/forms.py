from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Review, Books

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']

        from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'date', 'image']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=("Password"), strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

