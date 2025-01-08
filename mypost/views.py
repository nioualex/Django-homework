from django.shortcuts import render, redirect
from .forms import UserForm, BlogPostForm, UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import BlogPost, UserProfile
from django.contrib.auth.decorators import login_required


def postList(request):
    blog_posts = BlogPost.objects.all()  # 查詢所有 BlogPost 文章
    return render(request, 'postList.html', {'blog_posts': blog_posts})


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # 將當前用戶設為文章作者
            blog_post.save()
            return redirect('postList')  # 返回文章列表頁
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})


# 新增運動版的視圖
def sports_page(request):
    sports_posts = BlogPost.objects.filter(category='sports')
    return render(request, 'sports.html', {'sports_posts': sports_posts})


def foods_page(request):
    foods_posts = BlogPost.objects.filter(category='foods')
    return render(request, 'foods.html', {'foods_posts': foods_posts})


def feels_page(request):
    feels_posts = BlogPost.objects.filter(category='feels')
    return render(request, 'feels.html', {'feels_posts': feels_posts})


# 新增註冊視圖
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 密碼加密
            user.save()  # 保存用戶
            login(request, user)  # 登錄用戶
            return redirect('homepage')  # 重定向到首頁
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


# 首頁視圖 - 顯示海報圖片
def homepage(request):
    return render(request, 'mainpage.html', {'poster_image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1DcuE9u6tj_hZ6-12B5o3-tE-hyJMWSvpmA&s'})


# 新增個人資料編輯視圖
@login_required
def user_profile(request):
    # 獲取當前用戶的個人資料（如果不存在則創建）
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        # 使用 UserProfileForm 更新資料
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("user_profile")  # 更新成功後重定向回個人資料頁面
        else:
            # 如果表單無效，顯示錯誤信息
            form_errors = form.errors
    else:
        # 加載當前用戶的個人資料表單
        form = UserProfileForm(instance=user_profile)
        form_errors = None
    
    # 渲染模板並顯示表單
    return render(request, "user_profile.html", {
        "form": form,
        "user_profile": user_profile,
        "form_errors": form_errors  # 傳遞表單錯誤信息
    })