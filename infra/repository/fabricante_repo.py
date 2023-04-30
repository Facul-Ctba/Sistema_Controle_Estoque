from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Fabricantes
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import text
from sqlalchemy import asc, desc


class FabricantesRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Fabricantes)\
                    .with_entities(
                    Fabricantes.ID_FABR,
                    Fabricantes.NOMEFABR
                )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(
                    Fabricantes).filter_by(**kwargs).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, nomefabr):
        with DBConnectionHandler() as db:
            try:
                data_insert = Fabricantes(NOMEFABR=nomefabr)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, idfabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Fabricantes).filter(
                    Fabricantes.ID_FABR == idfabr).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, nomefabr_old, nomefabr):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Fabricantes).filter(Fabricantes.NOMEFABR == nomefabr_old).update(
                    {"NOMEFABR": nomefabr})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_orderby(self, descendente=False, **kwargs):
        coluna = kwargs.pop('coluna', None)
        self.desc = descendente
        with DBConnectionHandler() as db:
            try:
                if self.desc is True:
                    data = db.session.query(Fabricantes)\
                        .with_entities(
                        Fabricantes.ID_FABR,
                        Fabricantes.NOMEFABR)\
                        .order_by(desc(text(coluna)))\
                        .all()
                else:
                    data = db.session.query(Fabricantes)\
                        .with_entities(
                        Fabricantes.ID_FABR,
                        Fabricantes.NOMEFABR)\
                        .order_by(asc(text(coluna)))\
                        .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_pesquisa(self, **kwargs):
        coluna = kwargs.pop('coluna', None)
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Fabricantes)\
                    .with_entities(
                        Fabricantes.ID_FABR,
                        Fabricantes.NOMEFABR)\
                    .filter(Fabricantes.NOMEFABR.like(coluna))\
                    .all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
