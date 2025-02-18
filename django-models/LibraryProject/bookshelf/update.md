# Update a Book Instance

### Command:
```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Verify the update
updated_book = Book.objects.get(id=retrieved_book.id)
print(updated_book.title)
```

### Expected Output:
```python
Nineteen Eighty-Four
```

