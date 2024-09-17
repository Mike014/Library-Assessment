# Library Assessment

## Application Description
This Django application provides a RESTful API for managing books and authors, with features for authentication, search, and recommendation. The application is designed to meet the following requirements:

### 1. Book Management:
- Retrieve a list of all books.
- Retrieve a specific book by ID.
- Create a new book (protected).
- Update an existing book (protected).
- Delete a book (protected).

### 2. Author Management:
- Retrieve a list of all authors.
- Retrieve a specific author by ID.
- Create a new author (protected).
- Update an existing author (protected).
- Delete an author (protected).

### 3. Authentication:
- Use JWT for user authentication.
- Implement endpoints for user registration and login.

### 4. Search Functionality:
- Implement search for books by title or author name.

### 5. Recommendation System:
- Allow users to add/remove books from their favorites list.
- Recommend similar books based on the user's favorites list.

## Configuration and Installation

### Prerequisites:
- Python 3.8 or higher
- Django 5.1
- SQLite (default)

### Installation

```bash
# 1. Clone the Repository:
git clone <REPOSITORY_URL>
cd libraryassessment
```

```bash
# 2. Install Dependencies:
pip install -r requirements.txt
```

```bash
# 3. Apply Database Migrations:
python manage.py migrate
```

```bash
# 4. Load Initial Data (Optional):
python manage.py loaddata initial_data.json 
```  

## Running the Application

```bash
# 1. Start the Development Server:
python manage.py runserver 
```

2. **Access the Application**: Open a browser and navigate to **http://127.0.0.1:8000/**.

## Running Tests

- To run the automated tests, use the following command:

```bash
python manage.py test
```

## API Endpoints

### Books:
- **GET** `/books` - Retrieve a list of all books.
- **GET** `/books/:id` - Retrieve a specific book by ID.
- **POST** `/books` - Create a new book (protected).
- **PUT** `/books/:id` - Update an existing book (protected).
- **DELETE** `/books/:id` - Delete a book (protected).

### Authors:
- **GET** `/authors` - Retrieve a list of all authors.
- **GET** `/authors/:id` - Retrieve a specific author by ID.
- **POST** `/authors` - Create a new author (protected).
- **PUT** `/authors/:id` - Update an existing author (protected).
- **DELETE** `/authors/:id` - Delete an author (protected).

### Authentication:
- **POST** `/register` - Register a new user.
- **POST** `/login` - Log in a user.

### Search:
- **GET** `/books?search=query` - Search for books by title or author name.

### Recommendations:
- **POST** `/books/:id/favorite` - Add a book to the user's favorites.
- **GET** `/books/recommendations` - Retrieve a list of recommended books.

# Loading Authors Data
- To load authors data, follow these steps:
1. **Download the dataset**: [Large Books Metadata Dataset](https://www.kaggle.com/datasets/opalskies/large-books-metadata-dataset-50-mill-entries?resource=download)
2. Extract the dataset and place the authors.json file in the root directory of the project (libraryassessment).
3. Run the script to load authors data:

```bash
python load_authors.py
```

## Conclusion
This Django application provides a comprehensive system for managing a library, with features for authentication, search, and recommendation. Follow the steps above to configure and run the application. If you have any questions or need further clarification, refer to the official Django documentation or contact the development team.


