import os
import sqlmodel
from sqlmodel import SQLModel, Session


DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("`DATABASE_URL` is not set")

engine = sqlmodel.create_engine(DATABASE_URL)

# Database models
def init_db():
    print("creating all tables..")
    SQLModel.metadata.create_all(engine)

# api routes
def get_session():
    with Session (engine) as session:
        yield session