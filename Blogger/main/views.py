from django.http import HttpRequest
from django.shortcuts import render
from posts.models import Post

def home_view(request: HttpRequest):
    latest_posts = Post.objects.filter(is_published=True).order_by('-published_at')[:10]
    return render(request, 'main/index.html', {'latest_posts': latest_posts})


