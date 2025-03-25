from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'email': user.email})

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class FollowUserView(generics.GenericAPIView):
    """API endpoint for following a user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.follow(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """API endpoint for unfollowing a user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

