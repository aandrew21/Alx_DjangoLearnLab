from django.contrib import admin
from .models import Book
from rest_framework.authtoken.models import Token  # Import the Token model

# Register the Book model
admin.site.register(Book)

# Register the Token model to manage tokens via the admin panel
admin.site.register(Token)



# Register your models here.
