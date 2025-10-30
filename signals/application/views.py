from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse('home')


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(
            title=title,
            content=content,
            user=request.user
        )
        return redirect('/')
    return render(request, 'application/create_post.html')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'application/delete_post.html', {'post': post})
