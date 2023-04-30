from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Compras, Estoque
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_


class ComprasRepo:
    def my_select(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Compras)\
                    .select_from(Estoque)\
                    .join(Compras, Compras.PC_IDPROD == Estoque.ID_PROD)\
                    .with_entities(
                    Estoque.COD_FABR,
                    Estoque.PRODUTO,
                    Estoque.SALDO,
                    Compras.PC_LIM_MIN
                )\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_select_one(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Compras).filter_by(**kwargs).first()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_insert(self, pcidprod, pclimmin: float):
        with DBConnectionHandler() as db:
            try:
                data_insert = Compras(PC_IDPROD=pcidprod, PC_LIM_MIN=pclimmin)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_delete(self, pcidprod):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Compras).filter(
                    Compras.PC_IDPROD == pcidprod).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_update(self, pcidprod, pclimmin: float):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Compras).filter(
                    Compras.PC_IDPROD == pcidprod).update({
                        "PC_IDPROD": pcidprod,
                        "PC_LIM_MIN": pclimmin})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_pesquisa(self, **kwargs):
        coluna = kwargs.pop('coluna', None)
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Compras)\
                    .select_from(Estoque)\
                    .join(Compras, Compras.PC_IDPROD == Estoque.ID_PROD)\
                    .with_entities(
                    Estoque.COD_FABR,
                    Estoque.PRODUTO,
                    Estoque.SALDO,
                    Compras.PC_LIM_MIN)\
                    .filter(or_(Compras.PC_LIM_MIN.like(coluna),
                                Estoque.SALDO.like(coluna),
                                Estoque.COD_FABR.like(coluna),
                                Estoque.PRODUTO.like(coluna)))\
                    .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception
