from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Estoque, Fabricantes
from sqlalchemy.orm.exc import NoResultFound


class EstoqueRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Estoque)\
                    .select_from(Fabricantes)\
                    .join(Estoque, Fabricantes.ID_FABR == Estoque.ID_FABR)\
                    .with_entities(
                        Estoque.COD_INT,
                        Estoque.COD_FABR,
                        Estoque.PRODUTO,
                        Fabricantes.NOMEFABR,
                        Estoque.SALDO
                    )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Estoque).filter_by(**kwargs).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, codint, codfabr, produto, idfabr, saldo):
        with DBConnectionHandler() as db:
            try:
                data_insert = Estoque(COD_INT=codint, COD_FABR=codfabr, PRODUTO=produto,
                                      ID_FABR=idfabr, SALDO=saldo)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, codfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(
                    Estoque.COD_FABR == codfabr).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, codfabr_old, codint, codfabr, produto, idfabr, saldo):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.COD_FABR == codfabr_old).update({
                    "COD_INT": codint, "COD_FABR": codfabr, "PRODUTO": produto,
                    "ID_FABR": idfabr, "SALDO": saldo})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
