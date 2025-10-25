from django.shortcuts import render
from .models import Notification, Task
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def home(request):
    notification = Notification.objects.all()
    task = Task.objects.all()
    context = {'notification': notification, 'task': task }
    return render(request, 'application/home.html', context)
