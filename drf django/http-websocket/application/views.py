from django.shortcuts import render
from .models import Notification


def home(request):
    notification = Notification.objects.all()
    context = {'notification': notification }
    return render(request, 'application/home.html', context)
