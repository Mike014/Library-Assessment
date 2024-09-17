# books/tests.py
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import Author, Publisher, Book, Category
from django.contrib.auth.models import User
import datetime
from rest_framework_simplejwt.tokens import RefreshToken

class AuthorModelTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author Name", birth_date=datetime.date(1970, 1, 1), nationality="Italian")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Author Name")
        self.assertEqual(self.author.birth_date.strftime('%Y-%m-%d'), "1970-01-01")
        self.assertEqual(self.author.nationality, "Italian")

class PublisherModelTest(APITestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Publisher Name", address="Publisher Address", website="http://example.com")

    def test_publisher_creation(self):
        self.assertEqual(self.publisher.name, "Publisher Name")
        self.assertEqual(self.publisher.address, "Publisher Address")
        self.assertEqual(self.publisher.website, "http://example.com")

class CategoryModelTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fiction")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Fiction")

class BookModelTest(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author Name", birth_date=datetime.date(1970, 1, 1), nationality="Italian")
        self.publisher = Publisher.objects.create(name="Publisher Name", address="Publisher Address", website="http://example.com")
        self.category = Category.objects.create(name="Fiction")
        self.book = Book.objects.create(
            title="Book Title",
            author=self.author,
            publisher=self.publisher,
            published_date=datetime.date(2023, 1, 1),
            isbn="1234567890123",
            pages=300,
            cover="http://example.com/cover.jpg",
            language="English"
        )
        self.book.categories.add(self.category)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Book Title")
        self.assertEqual(self.book.author.name, "Author Name")
        self.assertEqual(self.book.publisher.name, "Publisher Name")
        self.assertEqual(self.book.published_date.strftime('%Y-%m-%d'), "2023-01-01")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertEqual(self.book.pages, 300)
        self.assertEqual(self.book.cover, "http://example.com/cover.jpg")
        self.assertEqual(self.book.language, "English")
        self.assertIn(self.category, self.book.categories.all())

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.author = Author.objects.create(name="Author Name", birth_date=datetime.date(1970, 1, 1), nationality="Italian")
        self.publisher = Publisher.objects.create(name="Publisher Name", address="Publisher Address", website="http://example.com")
        self.category = Category.objects.create(name="Fiction")
        self.book = Book.objects.create(
            title="Book Title",
            author=self.author,
            publisher=self.publisher,
            published_date=datetime.date(2023, 1, 1),
            isbn="1234567890123",
            pages=300,
            cover="http://example.com/cover.jpg",
            language="English"
        )
        self.book.categories.add(self.category)

    def test_get_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        author = Author.objects.create(name='Autore Test')
        data = {
            "title": "New Book",
            "author_id": author.id,
            "publisher_id": self.publisher.id,
            "published_date": "2023-01-01",
            "isbn": "1234567890124",
            "pages": 250,
            "cover": "http://example.com/new_cover.jpg",
            "language": "English",
            "category_ids": [self.category.id]
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {
            "title": "Updated Book Title",
            "author_id": self.author.id,
            "publisher_id": self.publisher.id,
            "published_date": "2023-01-01",
            "isbn": "1234567890123",
            "pages": 300,
            "cover": "http://example.com/cover.jpg",
            "language": "English",
            "category_ids": [self.category.id]
        }
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), data, format='json')
        print("Response data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_books(self):
        response = self.client.get(reverse('book-list') + '?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_favorite_book(self):
        response = self.client.post(reverse('favorite-book', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.book, self.user.favorite_books.all())

    def test_recommend_books(self):
        response = self.client.get(reverse('recommend-books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) <= 5)

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            "username": "newuser",
            "password": "newpassword",
            "email": "newuser@example.com"
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='testpassword')
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(reverse('token_obtain_pair'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthorAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.author = Author.objects.create(name="Author Name", birth_date=datetime.date(1970, 1, 1), nationality="Italian")

    def test_get_authors(self):
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_author_by_id(self):
        response = self.client.get(reverse('author-detail', kwargs={'pk': self.author.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author(self):
        data = {
            "name": "New Author",
            "birth_date": "1980-01-01",
            "nationality": "American"
        }
        response = self.client.post(reverse('author-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_author(self):
        data = {
            "name": "Updated Author Name"
        }
        response = self.client.put(reverse('author-detail', kwargs={'pk': self.author.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        response = self.client.delete(reverse('author-detail', kwargs={'pk': self.author.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)









