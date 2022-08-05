from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from decouple import config
from fastapi.security import  OAuth2PasswordRequestForm
from apps.authentication.schema import Token
from apps.authentication.jwt_handler import authenticate_user, fake_users_db, create_access_token
router = APIRouter(prefix='/auth', tags=['Authentication'])




@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config("ACCESS_TOKEN_EXPIRE_MINUTES"))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


