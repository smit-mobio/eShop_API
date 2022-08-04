from fastapi import FastAPI
import uvicorn
from apps.users import user  
from apps.group import group

SECRET_KEY = "a8f61fbb213a33775e551aedd4269cf79d68ce93"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
        "name": "User-Groups",
        "description": "Operations with groups.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(user.router)
app.include_router(group.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload= True)
