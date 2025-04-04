from pydantic import BaseModel, validator, ValidationError


class User(BasModel):
    email: str
    password: str
    age: int


@validator("password")
def password_length(cls, v):
    if len(v) < 8:
        raise ValueError("Password must be at least 8 characters long")
    return v

@validator("age")
def age_range(cls, v):
    if v < 18 or v > 120:
        raise ValueError("Age must be between 18 and 120")
    return v