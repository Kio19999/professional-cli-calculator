# Calculator API – Full Stack (JWT + Frontend + BREAD + E2E Testing + Advanced Operations)

## Overview

This project is a full-stack FastAPI web application that implements secure authentication, advanced calculator operations, frontend integration, automated testing, CI/CD, and Docker deployment.

The application includes:
- User registration and login with JWT authentication
- Full BREAD (Browse, Read, Edit, Add, Delete) operations
- Advanced calculation operations including power calculations
- PostgreSQL database integration using SQLAlchemy
- Pydantic validation and schemas
- Frontend pages using HTML + JavaScript
- Automated backend and frontend testing
- GitHub Actions CI/CD pipeline
- Docker containerization

---

# Features

## Authentication Features

- Register new users
- Login users securely
- JWT token generation
- Password hashing using secure encryption
- LocalStorage JWT token support

### Authentication Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /register | Register a new user |
| POST | /login | Login and receive JWT token |

---

# Calculation Features

## Supported Operations

- Addition
- Subtraction
- Multiplication
- Division
- Power operation

## Calculation Endpoints (BREAD)

| Method | Endpoint | Description |
|---|---|---|
| GET | /calculations | Get all calculations |
| GET | /calculations/{id} | Get calculation by ID |
| POST | /calculations | Create new calculation |
| PUT | /calculations/{id} | Update calculation |
| DELETE | /calculations/{id} | Delete calculation |

---

# Frontend Pages

| Route | Description |
|---|---|
| /register-page | User registration page |
| /login-page | User login page |
| /calculations-page | Full calculator BREAD UI |

---

# Frontend Functionality

The frontend includes:

- User registration form
- User login form
- Real-time API interaction
- Success and error messages
- Create calculations
- Browse calculations
- Update calculations
- Delete calculations
- JSON response viewer
- JWT token storage using localStorage

---

# Technologies Used

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication
- Pytest
- Playwright
- GitHub Actions
- Docker
- HTML
- JavaScript

---

# Project Structure

app/
│
├── calculator/
│   └── app.py
│
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── security.py

frontend/
│
├── register.html
├── login.html
├── calculations.html

e2e/
│
├── auth.spec.js
├── calculations.spec.js

tests/
│
├── test_api.py
├── test_routes_integration.py
├── test_users_integration.py
├── test_calculation_schemas.py
├── test_final_power_integration.py

.github/
│
└── workflows/
    └── python-tests.yml

Dockerfile
docker-compose.yml
requirements.txt
README.md

---

# Database Configuration

Default PostgreSQL connection:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db

Environment variables used:

DATABASE_URL
TEST_DATABASE_URL
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES

---

# How to Run the Application

## 1. Clone Repository

git clone <your-github-repo-url>
cd Calculator-cli2

---

## 2. Create Virtual Environment

python -m venv .venv

Activate virtual environment:

### Mac/Linux

source .venv/bin/activate

### Windows

.venv\Scripts\activate

---

## 3. Install Dependencies

pip install -r requirements.txt

---

## 4. Start PostgreSQL using Docker

docker compose up -d

Verify containers:

docker ps

---

## 5. Start FastAPI Server

uvicorn app.calculator.app:app --reload

Server runs at:

http://127.0.0.1:8000

---

# API Documentation

Open Swagger Docs:

http://127.0.0.1:8000/docs

---

# Frontend URLs

Open in browser:

http://127.0.0.1:8000/register-page
http://127.0.0.1:8000/login-page
http://127.0.0.1:8000/calculations-page

---

# Running Tests

## Backend Tests

Run all backend tests:


pytest -v

Expected result:


58 passed

---

# Playwright End-to-End Tests

## First-Time Setup


npm init -y
npm install -D @playwright/test
npx playwright install


---

## Run Playwright Tests

Keep FastAPI server running first:


uvicorn app.calculator.app:app --reload

Then open another terminal and run:


npx playwright test

Expected result:

7 passed


---

# Docker Support

## Build Docker Image


docker build -t calculator-api .

---

## Run Docker Container

docker compose up -d

---

# CI/CD Pipeline

GitHub Actions automatically:

- Starts PostgreSQL service
- Installs dependencies
- Runs Pytest backend tests
- Runs Playwright E2E tests
- Verifies Docker build
- Fails workflow if tests fail

Workflow file:

.github/workflows/python-tests.yml

---

# Testing Coverage

## Unit Tests

Verify:
- Calculation logic
- Password hashing
- Validation logic

## Integration Tests

Verify:
- Database interaction
- API endpoints
- Authentication flow

## End-to-End Tests

Verify:
- Frontend + backend interaction
- User login flow
- User registration flow
- Full calculation workflow

---

# Security Features

- JWT token authentication
- Secure password hashing
- Input validation using Pydantic
- Division-by-zero protection
- Protected calculation operations

---

# Key Concepts Implemented

- REST API development
- FastAPI routing
- SQLAlchemy ORM
- PostgreSQL integration
- JWT authentication
- Pydantic schemas
- CRUD/BREAD operations
- Frontend integration
- Playwright testing
- Pytest testing
- Docker containerization
- CI/CD automation

---

# Notes

- Passwords are securely hashed before storage
- JWT tokens are generated during login
- Frontend stores JWT token in localStorage
- Playwright simulates real user interactions
- All BREAD operations are fully tested
- Docker simplifies deployment
- CI/CD ensures application reliability

---

# Author

Himanshu Singh
MS in Data Science – NJIT