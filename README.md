# Calculator API – Full Stack (JWT + Frontend + E2E Testing)

## Overview
This project implements a full-stack FastAPI application with backend APIs, frontend pages, authentication, and automated testing.

It includes:
- User registration and login with JWT authentication
- Calculation CRUD (BREAD) operations
- PostgreSQL database using SQLAlchemy
- Pydantic validation
- Frontend pages (HTML + JavaScript)
- Playwright End-to-End testing
- CI/CD using GitHub Actions

---

## Features

### Authentication
- POST /register → Register new user
- POST /login → Login user and receive JWT token

### Calculation Endpoints (BREAD)
- GET /calculations → Get all calculations
- GET /calculations/{id} → Get single calculation
- POST /calculations → Create calculation
- PUT /calculations/{id} → Update calculation
- DELETE /calculations/{id} → Delete calculation

---

## Frontend Pages

- /register → User registration page
- /login → User login page

Frontend functionality:
- Input validation (email format, password rules)
- Displays success and error messages
- Stores JWT token in browser (localStorage)

---

## Technologies Used

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Pytest
- Playwright (E2E testing)
- GitHub Actions (CI/CD)
- Docker

---

## How to Run the Application

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start the FastAPI server
uvicorn app.calculator.app:app --reload

### 3. Open API Docs
http://127.0.0.1:8000/docs

### 4. Open Frontend Pages
http://127.0.0.1:8000/register  
http://127.0.0.1:8000/login  

---

## How to Run Tests

### Run backend tests
pytest -v

### Run Playwright (E2E tests)

First-time setup:
npm init -y  
npm install -D @playwright/test  
npx playwright install  

Run tests:
npx playwright test  

---

## Database Configuration

Default connection string:
postgresql://postgres:postgres@localhost:5432/fastapi_db

Environment variables used:
- DATABASE_URL
- TEST_DATABASE_URL

---

## CI/CD Pipeline

GitHub Actions automatically:
- Starts PostgreSQL service
- Runs backend tests (pytest)
- Runs Playwright E2E tests
- Fails if any test fails

Workflow file:
.github/workflows/python-tests.yml

---

## Project Structure

app/
  calculator/
    app.py
  crud.py
  database.py
  models.py
  schemas.py
  security.py

frontend/
  login.html
  register.html

e2e/
  auth.spec.js

tests/
  test_users_integration.py
  test_routes_integration.py
  test_calculations.py

.github/workflows/
  python-tests.yml

---

## Key Concepts Implemented

- JWT authentication (login + token generation)
- Secure password hashing
- Pydantic validation for request and response
- SQLAlchemy ORM for database interaction
- RESTful API design
- Integration testing with TestClient
- End-to-End testing using Playwright
- CI/CD pipeline automation
- Frontend and backend integration

---

## Testing Coverage

- Unit tests → verify logic
- Integration tests → verify API + database
- E2E tests → verify frontend + backend flow

---

## Notes

- Passwords are hashed before storing
- JWT token is generated on login
- Input validation prevents invalid data (e.g., invalid email, division by zero)
- Playwright simulates real user interaction
- CI/CD ensures all tests pass automatically

---

## Author
Himanshu Singh