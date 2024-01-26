from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Depends, HTTPException, status
from Backend.schemas.schema_automovel import Automovel
from Backend.models.model_automovel import AutomovelModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from Backend.database.config import get_db, criar_bd
from Backend.repositorio.automovel_repositorio import AutomovelRepositorio


app = FastAPI(title='API Loja de Automoveis')

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
criar_bd()
# realiza o cadastro dos carros no lista
@app.post('/carros', response_model=Automovel, status_code=201)
def criar_produtos(carro: Automovel, db: Session = Depends(get_db)):
    try:
        carro_criado = AutomovelRepositorio(db).incluir_automovel(carro)
        return carro_criado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

