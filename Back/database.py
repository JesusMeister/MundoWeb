from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read dot env file
from dotenv import load_dotenv
load_dotenv()

# Get env variables
import os
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
URI_CONNECTION = os.getenv("URI_CONNECTION")
DB_NAME = os.getenv("DB_NAME")
SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{URI_CONNECTION}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()