from fastapi import FastAPI
import uvicorn
from apps.users import user  
from apps.group import group


tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
        "name": "User-Groups",
        "description": "Operations with groups.",
    },
    {
        "name": "Product-Owner",
        "description": "Operations that product-owner can do.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(user.router)
app.include_router(group.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload= True)
