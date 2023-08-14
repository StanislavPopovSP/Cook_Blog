from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CommentForm(forms.ModelForm):
    """Форма, для отправки комментариев"""

    class Meta:
        model = Comment
        exclude = ['post', 'create_at']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'website': forms.TextInput(attrs={'placeholder': 'Website'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'})
        }


class RegisterUserForm(UserCreationForm):
    """Форма для регистрации пользователя."""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name*'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))

    class Meta:
        """Для отображения правильного порядка который нам нужен"""
        model = User  # В данную модель будем данные сохранять
        fields = ['username', 'password1', 'password2', 'email', 'fullname']


class LoginUserForm(AuthenticationForm):
    """Форма для авторизации пользователя."""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name*'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        """Для отображения правильного порядка который нам нужен"""
        model = User  # В данную модель будем данные сохранять
        fields = ['username', 'password']