from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),


    # djoser ke urls
    path('api/auth/', include('djoser.urls')),  # register, reset, etc.
    path('api/auth/', include('djoser.urls.jwt')),  # login, refresh, logout
]
