from .models import *
from django.db.models import Q

from django.shortcuts import redirect, render, get_object_or_404


def post_renderer(request):
    page_contents = PageContents.objects.latest(
        'updated') if PageContents.objects.all().count() > 0 else None
    category = Category.objects.all()
    counts = []
    for c in category:
        category_count = Video.objects.filter(category=c).count()
        counts.append(category_count)

    category_count = zip(category, counts)
    # post = get_object_or_404(Post, slug=slug)
    # category = Category.objects.all()
    # counts = []
    # for c in category:
    #     category_count = Post.objects.filter(category=c).count()
    #     counts.append(category_count)

    # category_count = zip(category,counts)
    # side_recent_post = Blog.objects.all().order_by('-created_at')[8:11]
    # side_popular_post = Blog.objects.all().order_by('-created_at')[12:16]

    return {
        'page_contents': page_contents,
        'category_count': category_count,
        # 'posts': post,
    }
