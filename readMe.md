# JWT Authentication API with Django Rest Framework

This project implements a secure authentication API using JSON Web Tokens (JWT) with Django Rest Framework. It allows users to authenticate, generate access tokens, refresh tokens, and manage their sessions.

## Features

- User registration and login endpoints.
- JWT-based authentication for secure communication.
- Token expiration and refresh mechanism.
- CORS (Cross-Origin Resource Sharing) handling using `django-cors-headers`.
- Access control through accepted origins.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-authentication-api.git
   cd your-authentication-api
2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install project dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Setup the database**
    ```bash
    python manage.py migrate
    ```
5. **Start the development server**
    ```bash
    python manage.py runserver
    ```

## Endpoints
- Login: `POST accounts/token/`
    - Request
    ```
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
    - Response
    ```
    {
        "access": "your_access_token",
        "refresh": "your_refresh_token"
    }
    ```
- Verify: `POST accounts/token/verify/`
    - Request
    ```
    {
        "token": "your_token"
    }
    ```
    - Response
    ```
    { } if valid
    ```
- Refresh: `POST accounts/token/refresh/`
    - Request
    ```
    {
        "refresh": "your_refresh_token"
    }
    ```
    - Response
    ```
    {
        "access": "your_new_access_token"
    }
    ```

## Token Expiry
**Access Token**: Expires in 10 seconds. Use the refresh token to get a new access token.
**Refresh Token**: Expires in 30 seconds. After expiration, users need to log in again

## CORS Configuration
Cross-Origin Resource Sharing (CORS) is configured using django-cors-headers. You can customize allowed origins and headers in the project settings
```
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-domain.com",
]
```