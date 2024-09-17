# books/serializers.py
from rest_framework import serializers
from .models import Author, Book, Publisher, Category
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all(), source='publisher', write_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, source='categories', write_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        book = Book.objects.create(**validated_data)
        book.categories.set(categories_data)
        return book

    def validate(self, data):
        print("Validating data:", data)
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user




