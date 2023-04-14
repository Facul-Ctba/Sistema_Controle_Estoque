from infra.configs.base import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Estoque(Base):
    __tablename__ = 'estoque'

    COD_INT = Column(String)
    COD_FABR = Column(String, primary_key=True)
    PRODUTO = Column(String, nullable=False)
    ID_FABR = Column(String, ForeignKey("fabricantes.ID_FABR"))
    SALDO = Column(Float, nullable=False)
    fabricantes = relationship("Fabricantes", backref="fabricantes", lazy="subquery")

    def __repr__(self):
        return f'[Cód. Int. = {self.COD_INT} | Cód. Fabr. = {self.COD_FABR} | \
Produto = {self.PRODUTO} | Fabric. = {self.fabricantes.NOMEFABR} | Saldo = {self.SALDO}]\n'


class Fabricantes(Base):
    __tablename__ = 'fabricantes'

    ID_FABR = Column(Integer, primary_key=True)
    NOMEFABR = Column(String, nullable=False)

    def __repr__(self):
        return f'[ID Fabr. = {self.ID_FABR} | Nome Fabr. = {self.NOMEFABR}]\n'
