from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Entradas, Estoque, Fabricantes
from sqlalchemy.orm.exc import NoResultFound


class EntradasRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Entradas)\
                    .with_entities(
                    Entradas.IN_DATA,
                    Entradas.IN_QUANT,
                    Entradas.IN_CODFABR
                    )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, variavel):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Entradas).filter(
                    Entradas.IN_CODFABR == variavel).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, indata, inquant, incodfabr):
        with DBConnectionHandler() as db:
            try:
                data_insert = Entradas(IN_DATA=indata, IN_QUAT=inquant, IN_CODFABR=incodfabr)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, incodfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Entradas).filter(
                    Entradas.IN_CODFABR == incodfabr).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, indata, inquant, incodfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Entradas).filter(Entradas.IN_CODFABR == incodfabr).update({
                    "IN_DATA": indata, "IN_QUANT": inquant, "IN_CODFABR": incodfabr})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
