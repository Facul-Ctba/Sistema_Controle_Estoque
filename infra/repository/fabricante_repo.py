from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Estoque, Fabricantes
from sqlalchemy.orm.exc import NoResultFound


class FabricantesRepo:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Fabricantes)\
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

    def select_one(self, variavel):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Fabricantes).filter(
                    Fabricantes.ID_FABR == variavel).one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, idfabr, nomefabr):
        with DBConnectionHandler() as db:
            try:
                data_insert = Fabricantes(ID_FABR=idfabr, NOMEFABR=nomefabr)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, idfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Fabricantes).filter(
                    Fabricantes.ID_FABR == idfabr).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, idfabr, nomefabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Fabricantes).filter(Fabricantes.ID_FABR == idfabr).update({
                    "ID_FABR": idfabr, "NOMEFABR": nomefabr})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
