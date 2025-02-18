# Delete a Book Instance

### Command:
```python
from bookshelf.models import Book

# Retrieve the book
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
retrieved_book.delete()

# Verify deletion
print(Book.objects.all())  # Should return an empty QuerySet
```

### Expected Output:
```python
<QuerySet []>
```

