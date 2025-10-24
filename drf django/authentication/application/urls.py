from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, LogoutView, home, signup_page, login_page, dashboard_page, MeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'users', ProfileViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    # Profile & Post CRUD (viewsets)
    path('', include(router.urls)),

    # JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/logout/', LogoutView.as_view(), name='token_logout'),

    # Custom endpoints / templates
    path("home/", home, name="home"),
    path("signup/", signup_page, name="signup_page"),
    path("login/", login_page, name="login_page"),
    path("me/", MeView.as_view(), name="me"),
    path("dashboard/", dashboard_page, name="dashboard_page"),

    # Djoser URLs
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
