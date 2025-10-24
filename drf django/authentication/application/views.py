from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer, PostSerializer
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


class ProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, "application/home.html")


def signup_page(request):
    return render(request, "application/signup.html")


def login_page(request):
    return render(request, "application/login.html")


def dashboard_page(request):
    return render(request, "application/dashboard.html")

