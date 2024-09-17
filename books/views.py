# books/views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Book, Author, Publisher, Category
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, CategorySerializer, UserSerializer
from django.db.models import Q

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query) | Q(author__name__icontains=search_query))
        return queryset

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        book = self.get_object()
        user = request.user
        user.favorite_books.add(book)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def recommend(self, request):
        # Implement recommendation logic here
        recommended_books = Book.objects.all()[:5]  # Simple example
        serializer = self.get_serializer(recommended_books, many=True)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class FavoriteBookView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        request.user.favorite_books.add(book)
        return Response({'status': 'book favorited'})

class RecommendBooksView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Implement the logic to recommend books here
        # Step 1: Retrieve all books not in the user's favorites
        user_favorites = request.user.favorite_books.all()
        other_books = Book.objects.exclude(id__in=user_favorites.values_list('id', flat=True))

        # Step 2: Calculate similarity (placeholder logic)
        # For simplicity, we are using a random selection of books
        recommended_books = other_books.order_by('?')[:5]

        # Step 3: Serialize and return the top 5 most similar books
        serializer = BookSerializer(recommended_books, many=True)
        return Response(serializer.data)

# Steps of the Algorithm
# 1.	Retrieve Non-Favorite Books:
# •	The algorithm first retrieves all books that are not in the user's favorites.
# •	This is done using the exclude method on the Book model, filtering out books that are in the user's favorite_books.
# 2.	Calculate Similarity:
# •	In this placeholder implementation, the algorithm randomly selects books to recommend.
# •	In a more sophisticated implementation, you would calculate the similarity based on shared attributes like categories, author, and publisher.
# 3.	Recommend Books:
# •	The top 5 most similar books are selected and serialized to be returned in the response.







