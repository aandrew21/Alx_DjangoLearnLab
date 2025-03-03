from django.shortcuts import render
# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing list view for books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
