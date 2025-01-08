from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mypost.views import (
    postList,
    create_blog_post,
    sports_page,
    foods_page,
    feels_page,
    register,
    homepage,
    user_profile,
)
from django.contrib.auth import views as auth_views  # 確保這一行存在

urlpatterns = [
    # 管理後台
    path('admin/', admin.site.urls),
    
    # 主頁面
    path('', homepage, name='homepage'),
    
    # 文章相關路徑
    path('postList/', postList, name='postList'),
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    
    # 分類頁面
    path('sports/', sports_page, name='sports_page'),
    path('foods/', foods_page, name='foods_page'),
    path('feels/', feels_page, name='feels_page'),
    
    # 使用者相關路徑
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    
    # 密碼重置相關路徑
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# 靜態文件與媒體文件的路徑設置
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
