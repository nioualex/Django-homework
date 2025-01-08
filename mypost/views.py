from django.shortcuts import render, redirect
from .forms import UserForm, BlogPostForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import BlogPost
from django.contrib.auth.decorators import login_required


def postList(request):
    blog_posts = BlogPost.objects.all()  # 查詢所有 BlogPost 文章
    return render(request, 'postList.html', {'blog_posts': blog_posts})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postList')  # 假設你有一個顯示部落格文章列表的 URL 名稱
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

# 新增運動版的視圖
def sports_page(request):
    # 篩選出 category 為 'sports' 的文章
    sports_posts = BlogPost.objects.filter(category='sports')
    return render(request, 'sports.html', {'sports_posts': sports_posts})

def foods_page(request):
    # 篩選出 category 為 'foods' 的文章
    foods_posts = BlogPost.objects.filter(category='foods')
    return render(request, 'foods.html', {'foods_posts': foods_posts})

def feels_page(request):
    # 篩選出 category 為 'feels' 的文章
    feels_posts = BlogPost.objects.filter(category='feels')
    return render(request, 'feels.html', {'feels_posts': feels_posts})

@login_required  # 需要登录才能编辑个人资料
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.userprofile
        )
        if form.is_valid():
            form.save()
            return redirect("profile")  # 重定向到个人资料页面
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "edit_profile.html", {"form": form})

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

# 首頁視圖 - 顯示海報圖片
def homepage(request):
    # 可以在這裡加入其他邏輯，根據需求進行擴展
    return render(request, 'mainpage.html', {'poster_image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1DcuE9u6tj_hZ6-12B5o3-tE-hyJMWSvpmA&s'})
