from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest
from .models import Post

# Create posts
def create_post_view(request: HttpRequest):
    
    if request.method == 'POST':
        new_post = Post(title=request.POST["title"], content=request.POST["content"])
        new_post.save()
        return redirect("main:home_view")

    return render(request, "posts/create.html")

# Read posts
def post_detail_view(request: HttpRequest, post_id: int):

    post = Post.objects.get(pk=post_id)

    return render(request, "posts/detail.html", {"post": post})

# Update posts
def update_post_view(request: HttpRequest, post_id: int):

    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        if "poster" in request.FILES: post.poster = request.FILES["poster"]
        post.save()

        return redirect("posts:post_detail_view", post_id=post.id)

    return render(request, "posts/post_update.html", {"post": post})

# Delete posts
def delete_post_view(request: HttpRequest, post_id: int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")



