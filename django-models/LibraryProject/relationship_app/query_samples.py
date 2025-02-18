import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return [book.title for book in library.books.all()]

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian.name

# Example usage
if __name__ == "__main__":
    print("Books by J.K. Rowling:", books_by_author("J.K. Rowling"))
    print("Books in City Library:", books_in_library("City Library"))
    print("Librarian of City Library:", librarian_of_library("City Library"))

