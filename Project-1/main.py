from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Automovel(BaseModel):
    id: Optional[str]
    nome: str
    marca: str
    modelo: str
    cor: str
    preco: float


# tipagem da lista Carros
carros: List[Automovel] = []

# lista todos so carros cadastrados
@app.get('/carros')
def listar_carros():
    return carros


# obtem o carro filtrado pelo ID
@app.get('/carros/{id_carro}')
def obter_carro(id_carro: str):
    for carro in carros:
        if id_carro == carro.id:
            return carro
    return {'mensagem': 'Carro não foi localizado'}


# realiza o cadastro dos carros no lista
@app.post('/carros')
def cadastrar_carros(carro: Automovel):
    carro.id = str(uuid4())
    carros.append(carro)
    return {'mensagem': 'Carro cadastrado com sucesso'}


# realiza o delete da Lista carros pelo filtro do ID e Pela possição
@app.delete('/carros/{id_carro}')
def remover_carro(id_carro: str):
    posicao = -1
    for index, carro in enumerate(carros):
        if carro.id == id_carro:
            posicao = index
            break
    if posicao != -1:
        carros.pop(posicao)
    else:
        return {'mensagem': 'Carro não foi localizado'}


@app.put("/carros/{id_carro}")
def atualizar_carro(id_carro: str, carro_atualizado: Automovel):
    index = next((i for i, carro in enumerate(carros) if carro.id == id_carro), None)
    if index is not None:
        carros[index] = carro_atualizado
        return {'mensagem': 'Carro atualizado com sucesso'}
    else:
        raise HTTPException(status_code=404, detail='Carro não encontrado')