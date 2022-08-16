from fastapi import APIRouter, Depends, HTTPException, status, Response
from datetime import timedelta
from decouple import config
from fastapi.security import  OAuth2PasswordRequestForm
from database.models import Data, User
from database.dao import dao_handler
from utils import common_function
from apps.authentication.schema import Token, ChangePasswordSchema, TokenData
from apps.authentication.jwt_handler import authenticate_user, create_access_token, get_current_active_user
from apps.users.schema import UserSchema

router = APIRouter(prefix='/auth', tags=['Authentication'])



@router.post("/token/", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(config("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/user/')
def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user


@router.post('/user/change_password/')
def change_password(form: ChangePasswordSchema, user:User = Depends(get_current_active_user)):
    current_user = dao_handler.user_dao.get_by_id(user.id)
    if form.password != form.new_password:
        return {'message':'Your password did not changed due to mismatch!'}
    current_user.password = common_function.get_password_hash(form.password)
    Data.commit()
    return {'message':'Your password is successfully changed!'}

