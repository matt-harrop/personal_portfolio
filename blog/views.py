from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def blog_home(request):
    blog_posts = BlogPost.objects.all().order_by('-date')
    return render(request, 'blog/blog_home.html', {'blog_posts': blog_posts})

def detail(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    return render(request, 'blog/detail.html', {'blog_post': blog_post})