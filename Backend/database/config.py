from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/concessonaria"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def criar_bd():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Erro ao criar tabelas do banco de dados: {e}")
    
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()