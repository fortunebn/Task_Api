from models.user import Usercreate
from fastapi.encoders import jsonable_encoder
from database import User_Collection
from bson import ObjectId
from auth import get_password_hash
from serializers import user_serializer
from fastapi import HTTPException

class UserCrud:

    @staticmethod
    def create_User(data: Usercreate):
        data = data.model_dump()
        data["password"] = get_password_hash(data["password"])
        data_in = jsonable_encoder(data)
        user_id = User_Collection.insert_one(data_in).inserted_id
        user = User_Collection.find_one({"_id": user_id})
        payload = user_serializer(user)
        return {"message": "User created successfully", "data": payload}
    

   
    
    @staticmethod
    def get_user_with_username(username: str):
        user = User_Collection.find_one({"username": username})
        return user
    
    @staticmethod
    def get_user_with_username_return_seralizer(username: str):
        user = User_Collection.find_one({"username": username})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user_serializer(user)
    

user_crud = UserCrud()