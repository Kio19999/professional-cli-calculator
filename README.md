# Calculator API – User & Calculation Routes

## Overview
This project implements a FastAPI-based backend with:
- User registration and login
- Calculation CRUD (BREAD) operations
- SQLAlchemy database integration
- Pydantic validation
- Integration and unit testing
- CI/CD using GitHub Actions

---

## Features

### User Endpoints
- POST `/users/register` → Register new user
- POST `/users/login` → Login user (password verification)

### Calculation Endpoints (BREAD)
- GET `/calculations` → Get all calculations
- GET `/calculations/{id}` → Get single calculation
- POST `/calculations` → Create calculation
- PUT `/calculations/{id}` → Update calculation
- DELETE `/calculations/{id}` → Delete calculation

---

## Technologies Used
- FastAPI  
- SQLAlchemy  
- Pydantic  
- PostgreSQL  
- Pytest  
- GitHub Actions (CI/CD)  
- Docker (configured)

---

## How to Run the Application

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
uvicorn app.calculator.app:app --reload
```

### 3. Open API Docs
Go to:
```
http://127.0.0.1:8000/docs
```

---

## How to Run Tests

```bash
pytest -v
```

All tests (unit + integration) should pass.

---

## Database Setup

Make sure PostgreSQL is running and update your connection string if needed:

```
postgresql://postgres:postgres@localhost:5432/fastapi_db
```

---

## CI/CD Pipeline

GitHub Actions is configured to:
- Run all tests automatically on push
- Ensure code correctness before deployment

Workflow file:
```
.github/workflows/python-tests.yml
```

---

## Project Structure

```
app/
  ├── calculator/
  │     └── app.py
  ├── crud.py
  ├── database.py
  ├── models.py
  ├── schemas.py
  ├── security.py

tests/
  ├── test_users_integration.py
  ├── test_routes_integration.py
  ├── test_calculations.py
```

---

## Key Concepts Implemented

- Pydantic validation for input/output  
- Secure password hashing  
- SQLAlchemy ORM models  
- Integration testing with TestClient  
- Factory-style logic for calculations  
- RESTful API design  

---

## Notes

- Passwords are securely hashed before storage  
- Input validation prevents invalid data (e.g., bad email, division by zero)  
- Integration tests verify full API + DB flow  

---

## Author
Himanshu Singh