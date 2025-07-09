import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from crud.user import user_crud
from jose import jwt, JWTError
from auth import oauth2_scheme
from models.user import User


load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')  # Change this in production
ALOGRITHM = os.environ.get('ALOGRITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', 30))





def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "bearer"},
    )
    try:
       

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALOGRITHM])
        

        username = payload.get("username")
        if not username:
            
            raise credentials_exception
    except JWTError as e:
       
        raise credentials_exception

    user = user_crud.get_user_with_username(username=username)

    if user is None:
        raise credentials_exception

    return User(**user)
