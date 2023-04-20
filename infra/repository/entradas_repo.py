from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Entradas, Estoque
from sqlalchemy.orm.exc import NoResultFound


class EntradasRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Entradas)\
                    .select_from(Estoque)\
                    .join(Entradas, Entradas.IN_IDPROD == Estoque.ID_PROD)\
                    .with_entities(
                    Entradas.IN_DATA,
                    Entradas.IN_QUANT,
                    Estoque.COD_FABR,
                    Estoque.PRODUTO
                    )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Entradas).filter_by(**kwargs).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, indata, inquant, inidprod):
        with DBConnectionHandler() as db:
            try:
                data_insert = Entradas(IN_DATA=indata,
                                       IN_QUANT=inquant,
                                       IN_IDPROD=inidprod)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, inidprod):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Entradas).filter(
                    Entradas.IN_IDPROD == inidprod).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, indata, inquant, inidprod):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Entradas).filter(Entradas.IN_IDPROD == inidprod).update({
                    "IN_DATA": indata,
                    "IN_QUANT": inquant,
                    "IN_IDPROD": inidprod})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
