from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Saidas, Estoque
from sqlalchemy.orm.exc import NoResultFound


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

    def my_select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Saidas).filter_by(**kwargs).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, outdata, outquant, outidprod, outdestino):
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

    def my_delete(self, outidprod):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Saidas).filter(
                    Saidas.OUT_IDPROD == outidprod).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, outdata, outquant, outidprod, outdestino):
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
