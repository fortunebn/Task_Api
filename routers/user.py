from datetime import timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password
from models.token import TokenData
from models.user import User, Usercreate
from crud.user import user_crud


user_routers = APIRouter()

@user_routers.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(payload: Usercreate):
    user = user_crud.create_User(payload)
    return user



@user_routers.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = user_crud.get_user_with_username(form_data.username)
    
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    token_data = TokenData(
        id=str(user["_id"]),
        username=user["username"]
    ).model_dump()

    access_token = create_access_token(
        data=token_data,
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@user_routers.get("/getuser", status_code=status.HTTP_200_OK)
def get_user(username:str):
    user = user_crud.get_user_with_username_return_seralizer(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User retrieved successfully", "data": user}
