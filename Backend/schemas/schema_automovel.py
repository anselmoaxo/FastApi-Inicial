from pydantic import BaseModel
from typing import Optional


class Automovel(BaseModel):
    id: Optional[int] 
    nome: str
    marca: str
    modelo: str
    cor: str
    preco: float
    

    