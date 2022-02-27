from werkzeug.security import safe_str_cmp
from models.user import UserModel

#function to authenticate using /auth and return JWT token 
def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

#function to use JWT token for identity verification & provide access to run JWT secure code 
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)