from django.db import models
from django.contrib.auth.models import User

# Author model to store author details
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author
    birth_date = models.DateField(default='1900-01-01')  # Birth date with a default value
    nationality = models.CharField(max_length=50, default='Unknown')  # Nationality with a default value

    def __str__(self):
        return self.name  # String representation of the model

# Publisher model to store publisher details
class Publisher(models.Model):
    name = models.CharField(max_length=100)  # Name of the publisher
    address = models.CharField(max_length=255, default='Default Address')  # Address with a default value
    website = models.URLField(default='http://default.com')  # Website with a default value

    def __str__(self):
        return self.name  # String representation of the model

# Category model to store book categories
class Category(models.Model):
    name = models.CharField(max_length=100)  # Name of the category

    def __str__(self):
        return self.name  # String representation of the model

# Book model to store book details
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Foreign key to Author model
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, default=1)  # Foreign key to Publisher model with a default value
    published_date = models.DateField(default='1900-01-01')  # Published date with a default value
    isbn = models.CharField(max_length=13)  # ISBN number of the book
    pages = models.IntegerField(default=0)  # Number of pages with a default value
    cover = models.URLField(default='http://example.com/default_cover.jpg')  # Cover URL with a default value
    language = models.CharField(max_length=30, default='English')  # Language with a default value
    categories = models.ManyToManyField(Category)  # Many-to-many relationship with Category model
    favorited_by = models.ManyToManyField(User, related_name='favorite_books', blank=True)  # Many-to-many relationship with User model, allowing blank values

    def __str__(self):
        return self.title  # String representation of the model

# Explanation of the Models
# •	Author: Stores details about authors, including name, birth date, and nationality.
# •	Publisher: Stores details about publishers, including name, address, and website.
# •	Category: Stores book categories.
# •	Book: Stores details about books, including title, author, publisher, published date, ISBN, pages, cover URL, language, and categories. It also tracks which users have favorited the book.

# Logic Behind the Design
# •	Relationships: The models are designed to have clear relationships. For example, a book can have one author, one publisher, and multiple categories.
# •	Defaults: Default values are provided for fields where applicable to ensure data consistency.
# •	String Representation: Each model has a __str__ method to provide a human-readable representation of the model instances.


