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
    PC = Column(Integer)
    fabricante = relationship("Fabricantes", backref="estoque", lazy="subquery")

    def __repr__(self):
        return f'[{self.ID_PROD}, "{self.COD_INT}", "{self.COD_FABR}", \
"{self.PRODUTO}", "{self.fabricante.NOMEFABR}", {self.SALDO}, {self.PC}]'


class Fabricantes(Base):
    __tablename__ = 'fabricantes'

    ID_FABR = Column(Integer, primary_key=True)
    NOMEFABR = Column(String, nullable=False)

    def __repr__(self):
        return f'[{self.ID_FABR}, "{self.NOMEFABR}"]'


class Entradas(Base):
    __tablename__ = 'entradas'

    IN_ID = Column(Integer, primary_key=True)
    IN_DATA = Column(String, nullable=False)
    IN_QUANT = Column(Float, nullable=False)
    IN_IDPROD = Column(Integer, ForeignKey("estoque.ID_PROD"))
    in_codfabr_rs = relationship("Estoque", backref="entradas", lazy="subquery")

    def __repr__(self):
        return f'["{self.IN_DATA}", {self.IN_QUANT}, "{self.estoque.COD_FABR}"]'


class Saidas(Base):
    __tablename__ = 'saidas'

    OUT_ID = Column(Integer, primary_key=True)
    OUT_DATA = Column(String, nullable=False)
    OUT_QUANT = Column(Float, nullable=False)
    OUT_IDPROD = Column(Integer, ForeignKey("estoque.ID_PROD"))
    OUT_DESTINO = Column(String, nullable=False)
    out_codfabr_rs = relationship("Estoque", backref="saidas", lazy="subquery")

    def __repr__(self):
        return f'["{self.OUT_DATA}", {self.OUT_QUANT}, "{self.estoque.COD_FABR}", "{self.OUT_DESTINO}"]'


class Compras(Base):
    __tablename__ = 'compras'

    PC_ID = Column(Integer, primary_key=True)
    PC_IDPROD = Column(Integer, ForeignKey("estoque.ID_PROD"))
    PC_LIM_MIN = Column(Integer, nullable=False)
    pc_codfabr_rs = relationship("Estoque", backref="compras", lazy="subquery")

    def __repr__(self):
        return f'[{self.PC_IDPROD}, "{self.estoque.COD_FABR}", {self.PC_LIM_MIN}"]'
