from django.contrib import admin
from core.models import Post, LikePost, FollowersCount, DisLikePost, ViewsCount, Comment, Category, PageContents

# Register your models here.
admin.site.register(PageContents)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(DisLikePost)
admin.site.register(Comment)
admin.site.register(ViewsCount)
admin.site.register(Category)
