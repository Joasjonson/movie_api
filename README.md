# 🎬 Movie API

This is a REST API developed with Django REST Framework, with the goal of practicing and deepening knowledge in back-end development.

The API manages information related to movies, genres, actors and reviews, in addition to having user authentication and authorization with JWT.

## ⚙️ Features

- 🔐 User registration and login with JWT authentication
- 📽️ Movie CRUD
- 🏷️ Genre CRUD
- 🎭 Actor CRUD
- ✍️ Reviews CRUD
- 🔎 Possible expansion with filters, pagination and search
---

## 🛠️ Technologies used

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite (default, but can be changed to PostgreSQL, etc.)

---

## 📦How to run the project

### 1. Clone the repository
``` bash
git clone https://github.com/Joasjonson/movie_api.git
cd movie_api

# Virtual Environment
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

pip install -r requirements.txt
python manage.py migrate

python manage.py runserver
The API will be available at http://127.0.0.1:8000/
```

---

### 🔐 JWT Authentication
Authentication is done with JSON Web Tokens (JWT) using the djangorestframework-simplejwt package.

🔄 Main endpoints
Method Endpoint Description
- POST /api/token/ Login (get token)
- POST /api/token/refresh/ Refresh token
- POST /api/register/ New user registration
- GET /api/movies/ List of movies
- POST /api/movies/ Create new movie (authenticated)
- GET /api/genres/ List of genres
- GET /api/actors/ List of actors
- GET /api/reviews/ List of reviews
- POST /api/reviews/ Create new review (authenticated)

