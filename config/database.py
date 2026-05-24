from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#carga las variables del archivo .env
load_dotenv()

#lee las credenciales
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

#construye la URL de conexion
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#crea el motor de conexion
engine = create_engine(DATABASE_URL)

#crea la sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base para los modelos
Base = declarative_base()

#dependencia para obtener la sesion en cada endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

