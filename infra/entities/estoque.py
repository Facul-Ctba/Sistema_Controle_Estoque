from infra.configs.base import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Estoque(Base):
    __tablename__ = 'estoque'

    ID_PROD = Column(Integer, primary_key=True)
    COD_INT = Column(String)
    COD_FABR = Column(String, nullable=False)
    PRODUTO = Column(String, nullable=False)
    ID_FABR = Column(Integer, ForeignKey("fabricantes.ID_FABR"))
    SALDO = Column(Float, nullable=False)
    fabricante = relationship("Fabricantes", backref="fabricantes", lazy="subquery")

    def __repr__(self):
        return f'[{self.ID_PROD}, "{self.COD_INT}", "{self.COD_FABR}", \
"{self.PRODUTO}", "{self.fabricante.NOMEFABR}", {self.SALDO}]'


class Fabricantes(Base):
    __tablename__ = 'fabricantes'

    ID_FABR = Column(Integer, primary_key=True)
    NOMEFABR = Column(String, nullable=False)

    def __repr__(self):
        return f'[{self.ID_FABR}, "{self.NOMEFABR}"]'


class Entradas(Base):
    __tablename__ = 'entradas'

    IN_DATA = Column(String, nullable=False)
    IN_QUANT = Column(Float, nullable=False)
    IN_IDPROD = Column(Integer, ForeignKey("estoque.ID_PROD"), primary_key=True)
    fk_codfabr = relationship("Estoque", backref="estoque", lazy="subquery")

    def __repr__(self):
        return f'["{self.IN_DATA}", {self.IN_QUANT}, "{self.estoque.COD_FABR}"]'
