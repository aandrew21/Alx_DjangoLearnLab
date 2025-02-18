# CRUD Operations for Book Model

This document contains all CRUD (Create, Retrieve, Update, Delete) operations performed on the `Book` model using Django's ORM.

---

##  1. Create a Book Instance

### **Command:**
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```

### **Expected Output:**
```python
1984 by George Orwell (1949)
```

---

##  2. Retrieve a Book Instance

### **Command:**
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```

### **Expected Output:**
```python
1984 George Orwell 1949
```

---

##  3. Update a Book Instance

### **Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Verify the update
updated_book = Book.objects.get(id=retrieved_book.id)
print(updated_book.title)
```

### **Expected Output:**
```python
Nineteen Eighty-Four
```

---

##  4. Delete a Book Instance

### **Command:**
```python
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
retrieved_book.delete()

# Verify deletion
print(Book.objects.all())  # Should return an empty QuerySet
```

### **Expected Output:**
```python
<QuerySet []>
```

---

##  CRUD Operations Completed Successfully!

