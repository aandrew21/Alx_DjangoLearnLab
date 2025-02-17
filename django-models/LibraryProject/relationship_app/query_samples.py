import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)  # ✅ Using get() instead of filter().first()
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)  # ✅ Fix: Using get() instead of filter().first()
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library=library)  # ✅ Using get() instead of filter().first()
    print(f"Librarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}.")

