# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import BlogPost, UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
        labels = {
            'avatar': '用户头像',
        }
        help_texts = {
            'avatar': '请选择您的头像（可选）',
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        labels = {
            'username': '用户名',
            'email': '电子邮件',
            'first_name': '名',
            'last_name': '姓',
            'password': '密码'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '用户名'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': '邮箱'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': '名'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': '姓'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': '密码'})


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'category']
