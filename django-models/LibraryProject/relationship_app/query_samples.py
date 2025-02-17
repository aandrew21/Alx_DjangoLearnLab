import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.filter(name=author_name).first()
if author:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name = "Central Library"
library = Library.objects.filter(name=library_name).first()
if library:
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian = Librarian.objects.filter(library=library).first()
if librarian:
    print(f"Librarian of {library_name}: {librarian.name}")

