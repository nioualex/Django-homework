from django.contrib import admin
from .models import Post, BlogPost

# Post 模型的管理界面
class PostAdmin(admin.ModelAdmin):
    # 顯示的字段
    list_display = ('title', 'slug', 'pub_date')
    # 允許過濾的字段
    list_filter = ('pub_date',)
    # 允許在列表頁面進行搜索
    search_fields = ('title', 'body')
    # 可以直接在列表頁面進行編輯的字段
    list_editable = ('slug',)

    # 自定義顯示日期格式
    date_hierarchy = 'pub_date'

# BlogPost 模型的管理界面
class BlogPostAdmin(admin.ModelAdmin):
    # 顯示的字段
    list_display = ('title', 'category', 'updated_at')
    # 允許過濾的字段
    list_filter = ('category', 'updated_at')
    # 允許在列表頁面進行搜索
    search_fields = ('title', 'content')
    # 可以直接在列表頁面進行編輯的字段
    list_editable = ('category',)

    # 顯示更新時間
    date_hierarchy = 'updated_at'

# 註冊模型和它們的管理界面
admin.site.register(Post, PostAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
