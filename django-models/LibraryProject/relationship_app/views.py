from .models import Library
from django.shortcuts import render
from .models import Book, Library  # ✅ Make sure Library is imported here
from django.views.generic.detail import DetailView  # ✅ Import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details along with books in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

