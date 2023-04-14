from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Estoque
from sqlalchemy.orm.exc import NoResultFound


class EstoqueRepo:
    def select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Estoque).all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                coluna = str(kwargs.keys())
                valor = kwargs.values()
                temp = coluna, valor 
                data = db.session.query(Estoque).filter_by(
                    **kwargs).all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, codint, codfabr, produto, idfabr, saldo):
        with DBConnectionHandler() as db:
            try:
                data_insert = Estoque(COD_INT=codint, COD_FABR=codfabr, PRODUTO=produto,
                                      ID_FABR=idfabr, SALDO=saldo)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, codfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(
                    Estoque.COD_FABR == codfabr).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, codint, codfabr, produto, idfabr, saldo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.COD_FABR == codfabr).update({
                    "COD_INT": codint, "COD_FABR": codfabr, "PRODUTO": produto,
                    "ID_FABR": idfabr, "SALDO": saldo})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
