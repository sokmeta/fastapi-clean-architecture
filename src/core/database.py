import sqlalchemy
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

DB_DIALECT = 'mysql'
DB_DRIVER = 'pymysql'
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))

def tcp_socket_database_url():
    url = sqlalchemy.engine.url.URL.create(
        drivername=f"{DB_DIALECT}+{DB_DRIVER}",
        username=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    )
    
    return url

def create_engine(database_url: sqlalchemy.URL):
    return sqlalchemy.create_engine(
        database_url,
        pool_size=10,
        max_overflow=100,
        pool_pre_ping=True,
        pool_recycle=3600
    )

def check_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Connection successful")
    except Exception as e:
        print(f"Connection failed: {e}")

engine = create_engine(tcp_socket_database_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

