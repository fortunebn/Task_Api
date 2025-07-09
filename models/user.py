from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    last_name: str
    email: EmailStr


class Usercreate(UserBase):
    password: str


class UserDb(UserBase):
    id: str

class User(Usercreate):
    pass



