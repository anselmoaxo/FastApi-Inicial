from sqlalchemy.orm import Session
from Backend.schemas import schema_automovel
from Backend.models import model_automovel


class AutomovelRepositorio():

    def __init__(self, db: Session):
        self.db = db

    def incluir_automovel(self, carro: schema_automovel.Automovel):
        bd_automovel = model_automovel.AutomovelModel(id=carro.id,
                                                      nome=carro.nome,
                                                      marca=carro.marca,
                                                      modelo=carro.modelo,
                                                      cor=carro.cor,
                                                      preco=carro.preco)
        self.db.add(bd_automovel)
        self.db.commit()
        self.db.refresh(bd_automovel)
        return bd_automovel