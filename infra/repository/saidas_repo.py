from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Saidas, Estoque
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_


class SaidasRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Saidas)\
                    .select_from(Estoque)\
                    .join(Saidas, Saidas.OUT_IDPROD == Estoque.ID_PROD)\
                    .with_entities(
                    Saidas.OUT_DATA,
                    Saidas.OUT_QUANT,
                    Estoque.COD_FABR,
                    Estoque.PRODUTO,
                    Saidas.OUT_DESTINO
                    )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, outdata, outquant: float, outidprod: int):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Saidas).filter(and_(Saidas.OUT_DATA.like(outdata),
                                                            Saidas.OUT_QUANT.like(outquant),
                                                            Saidas.OUT_IDPROD.like(outidprod)))\
                                 .first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, outdata, outquant: float, outidprod: int, outdestino):
        with DBConnectionHandler() as db:
            try:
                data_insert = Saidas(OUT_DATA=outdata,
                                     OUT_QUANT=outquant,
                                     OUT_IDPROD=outidprod,
                                     OUT_DESTINO=outdestino)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, outid: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Saidas).filter(
                    Saidas.OUT_ID == outid).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, outdata, outquant: float, outidprod: int, outdestino):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Saidas).filter(Saidas.OUT_IDPROD == outidprod).update({
                    "OUT_DATA": outdata,
                    "OUT_QUANT": outquant,
                    "OUT_IDPROD": outidprod,
                    "OUT_DESTINO": outdestino})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_pesquisa(self, **kwargs):
        coluna = kwargs.pop('coluna', None)
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Saidas)\
                    .select_from(Estoque)\
                    .join(Saidas, Saidas.OUT_IDPROD == Estoque.ID_PROD)\
                    .with_entities(
                    Saidas.OUT_DATA,
                    Saidas.OUT_QUANT,
                    Estoque.COD_FABR,
                    Estoque.PRODUTO,
                    Saidas.OUT_DESTINO)\
                    .filter(or_(Saidas.OUT_DATA.like(coluna),
                                Saidas.OUT_QUANT.like(coluna),
                                Estoque.COD_FABR.like(coluna),
                                Estoque.PRODUTO.like(coluna),
                                Saidas.OUT_DESTINO.like(coluna)))\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
