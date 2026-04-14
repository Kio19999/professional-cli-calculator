from app.security import hash_password, verify_password
from app.schemas import UserCreate
from pydantic import ValidationError
import pytest

def test_hash_password():
    password = "mypassword123"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True

def test_verify_wrong_password():
    password = "mypassword123"
    hashed = hash_password(password)

    assert verify_password("wrongpass", hashed) is False

def test_usercreate_valid():
    user = UserCreate(
        username="himanshu",
        email="himanshu@example.com",
        password="secret123"
    )
    assert user.username == "himanshu"

def test_usercreate_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="himanshu",
            email="bad-email",
            password="secret123"
        )