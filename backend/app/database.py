from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

#gets the database connection from env file
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_SERVER')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"

#create the engine which connects app and psql
engine = create_engine(DATABASE_URL)

# This creates new database sessions when needed
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#declerative base parent class
Base = declarative_base()

# Create GET_DB dependency
# FastAPI calls this to give endpoints a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()