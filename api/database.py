from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DataBaseUrl='sqlite:///./test.db'

engine=create_engine(
    DataBaseUrl, connect_args={"check_same_thread": False}
)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()