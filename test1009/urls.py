"""
URL configuration for test1009 project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mypost.views import postList, create_blog_post, sports_page, foods_page, feels_page, register, homepage  # 引入首頁視圖
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),  # 新增首頁視圖路徑
    path('postList/', postList, name='postList'),  # 文章列表頁面
    path('create_blog_post/', create_blog_post, name='create_blog_post'),  # 新增文章頁面
    path('sports/', sports_page, name='sports_page'),  # 運動版頁面
    path('foods/', foods_page, name='foods_page'),  # 美食版頁面
    path('feels/', feels_page, name='feels_page'),  # 心情版頁面
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),  # 註冊頁面
    
    # 密碼重置路徑
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

