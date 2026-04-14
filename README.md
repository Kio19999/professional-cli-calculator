Calculator CLI + FastAPI Application

Overview

This project is a Python-based calculator application extended with a FastAPI backend and PostgreSQL database integration. It supports arithmetic operations and user creation with proper validation, along with comprehensive testing.

⸻

Features
	•	Basic calculator operations:
	•	Add
	•	Subtract
	•	Multiply
	•	Divide
	•	REST API built using FastAPI
	•	PostgreSQL database integration using SQLAlchemy
	•	User creation with validation and password hashing
	•	Dockerized setup for easy deployment
	•	Full test coverage:
	•	Unit Tests
	•	Integration Tests
	•	End-to-End Tests

⸻

Tech Stack
	•	Python 3.13
	•	FastAPI
	•	PostgreSQL
	•	SQLAlchemy
	•	Docker & Docker Compose
	•	Pytest

⸻

Setup Instructions

1. Clone the repository

git clone (https://github.com/Kio19999/professional-cli-calculator)
cd calculator-cli2

2. Start the application using Docker

docker compose up --build

3. Access API

Open browser:

http://localhost:8000/docs


⸻

Running Tests

# Calculator API

## Run locally
```bash
pip install -r requirements.txt
pytest -v


✔ All tests passing (42/42)

⸻

docker build -t k1oo/calculator-api .
docker run -p 8000:8000 k1oo/calculator-api

https://hub.docker.com/r/k1oo/calculator-api



API Endpoints

Method	Endpoint	Description
GET	/	Home        route
GET	/   add	        Add numbers
GET	/.  subtract	Subtract numbers
GET	/.  multiply	Multiply numbers
GET	/   divide	    Divide numbers
POST/.  users	    Create user


⸻

Example Request (Create User)

{
  "username": "himanshu",
  "email": "himanshu@example.com",
  "password": "Strong123"
}


⸻

Project Structure

app/
  calculator/
  operation/
  database.py
  models.py
  schemas.py
  crud.py
  security.py

tests/
  test_api.py
  test_calculations.py
  test_operations.py
  test_users_unit.py
  test_users_integration.py


⸻

Notes
	•	Integration tests use PostgreSQL database.
	•	Database connection is configured using SQLAlchemy.
	•	Password hashing is implemented for security.

⸻

Author

Himanshu Singh
