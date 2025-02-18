# Retrieve a Book Instance

### Command:
```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```

### Expected Output:
```python
1984 George Orwell 1949
```

