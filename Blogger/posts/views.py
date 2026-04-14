from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest
from .models import Post

def create_post_view(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title and content:
            new_post = Post(
                title=title,
                content=content,
                is_published=True,
            )
            new_post.save()
            return redirect('main:home_view')

    return render(request, "posts/create.html")


def post_detail_view(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    return render(request, "posts/detail.html", {"post": post})
