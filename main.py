from fastapi import FastAPI
import uvicorn
from apps.users import user  
from apps.group import group
from apps.authentication import auth


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
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload= True)
