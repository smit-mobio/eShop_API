from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1605@localhost:5432/eShop_API"

engine = create_engine(DATABASE_URL, echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
db = SessionLocal()