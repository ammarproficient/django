from django.shortcuts import render
from .models import Blog, Alert, GalleryImage  # GalleryImage model hona chahiye


def home(request):
    blogs = Blog.objects.all()
    alert = Alert.objects.first()
    gallery_images = GalleryImage.objects.all()
    context = {
        "blogs": blogs,
        "alert": alert,
        "gallery_images": gallery_images,
    }
    return render(request, 'application/home.html', context)
