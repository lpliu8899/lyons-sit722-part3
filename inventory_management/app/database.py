from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#SQLALCHEMY_DATABASE_URL = "postgresql://lyons_sit722_part3_user:zDHiWCqUrH5QFe5Geqg29YICMRzCpaci@dpg-cr6ptd5ds78s73c28o90-a.oregon-postgres.render.com/lyons_sit722_part3" #os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
