from datetime import timedelta, datetime
from jose import JWTError, jwt
from decouple import config
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
from apps.authentication.schema import TokenData, Token
from apps.users.schema import UserSchema, UserActiveSchema
from database.dao import dao_handler
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token/")
JWT_SECRET = config('JWT_SECRET_KEY')
JWT_ALGORITHM = config('JWT_ALGORITHM')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(email: str, password: str):
    user = dao_handler.user_dao.get_by_email(email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def get_user(email: str):
    if email in [i.email for i in dao_handler.user_dao.get_all()]:
        user_dict = dao_handler.user_dao.get_by_email(email)
        return UserActiveSchema(**user_dict.__dict__)

# function used for signing the JWT string
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: UserActiveSchema = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

    
