from .models import Library
from django.shortcuts import render
from .models import Book, Library  # ✅ Make sure Library is imported here
from django.views.generic.detail import DetailView  # ✅ Import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details along with books in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Function to check user role
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - accessible only by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view - accessible only by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view - accessible only by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
