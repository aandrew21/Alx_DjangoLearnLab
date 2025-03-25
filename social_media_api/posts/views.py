from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.contenttypes.models import ContentType

class UserFeedView(generics.ListAPIView):
    """API endpoint for fetching user feed."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # Get users that the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Order by newest first

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    Users can create, retrieve, update, and delete posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments on posts.
    Users can create, retrieve, update, and delete comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Post already liked."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)

# Create your views here.
