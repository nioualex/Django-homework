from django.db import models
from django.contrib.auth.models import User

# 定义 Post 模型
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
class BlogPost(models.Model):
    TITLE_MAX_LENGTH = 200

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('sports', '運動'),
        ('feels', '心情'),
        ('foods', '美食'),
    ], default='tech')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 添加這一行

    def __str__(self):
        return self.title
    
# 定义 UserProfile 模型
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # 默认头像

    def __str__(self):
        return self.user.username
