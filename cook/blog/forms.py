from django import forms
from .models import Comment


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
