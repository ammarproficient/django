from django.urls import path, include
from .views import home, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home, name="home"),        # normal view
    path('api/', include(router.urls)), # API routes via router
]
