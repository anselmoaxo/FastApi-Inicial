from sqlalchemy import Column, Float, String, Integer
from Backend.database.config import Base


class AutomovelModel(Base):
    
    __tablename__ = 'automoveis'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    marca = Column(String)
    modelo = Column(String)
    cor = Column(String)
    preco = Column(Float)
    