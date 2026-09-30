from pydantic import BaseModel


class UserRegistrationSchema(BaseModel):
    username: str
    email: str
    password: str


class UserSchema(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True