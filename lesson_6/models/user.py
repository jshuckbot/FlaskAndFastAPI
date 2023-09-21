from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(title='First name', max_length=32)
    last_name: str = Field(title='Last name', max_length=32)
    email: EmailStr = Field(title='Email', max_length=128)
    password: str = Field(title='Password', min_length=5)


class User(UserIn):
    id: int
