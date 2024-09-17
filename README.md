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
