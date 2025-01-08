# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import BlogPost, UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'name', 'bio']  # 修改這裡，使用 profile_picture 而非 avatar
        labels = {
            'profile_picture': '用户头像',  # 修改标签名为“用户头像”
            'name': '昵称',
            'bio': '个人简介'
        }
        help_texts = {
            'profile_picture': '请选择您的头像（可选）',
            'name': '输入您的昵称',
            'bio': '填写个人简介'
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
