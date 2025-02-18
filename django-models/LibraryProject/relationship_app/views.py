from .models import Library
from django.shortcuts import render, redirect
from .models import Book, Library  # ✅ Make sure Library is imported here
from django.views.generic.detail import DetailView  # ✅ Import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("book_list")  # Redirect to the main page after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# User Registration View
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("book_list")  # Redirect to main page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

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
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - accessible only by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - accessible only by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
