import random
from database.models import User
from database.database import db
import string
from passlib.context import CryptContext
from database.dao import dao_handler
from datetime import datetime
from database.models import Data
from utils.validations import validate_phonenumber

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALL_ALPHABATES = string.ascii_letters
SYMBOLS = [
    "~",
    ":",
    "'",
    "+",
    "[",
    "\\",
    "@",
    "^",
    "{",
    "%",
    "(",
    "-",
    '"',
    "*",
    "|",
    ",",
    "&",
    "<",
    "`",
    "}",
    ".",
    "_",
    "=",
    "]",
    "!",
    ">",
    ";",
    "?",
    "#",
    "$",
    ")",
    "/",
]

All_CHARACTER = list(ALL_ALPHABATES) + SYMBOLS

def get_all_username():
    usernames = [i.username for i in db.query(User).all()]
    return usernames

def modify_username(username):
    all_usernames = get_all_username()
    if username not in all_usernames:
        return username
    else:
        username = str(username) + str(random.randrange(0, 99))
        username = modify_username(username)
        return username

def create_username(email):
    username = email.split('@')[0]
    if '.' in username:
        username = username.split('.')[0]
    username = modify_username(username)
    return username

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

def update_profile(data, user):
    user_to_update = dao_handler.user_dao.get_by_id(user.id)
    user_to_update.first_name = data.first_name
    user_to_update.last_name = data.last_name
    if not validate_phonenumber(data.phone):
        return False
    user_to_update.phone = data.phone
    user_to_update.updated_on = datetime.now()
    Data.commit()
    return True