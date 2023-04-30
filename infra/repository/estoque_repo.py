from infra.configs.connection import DBConnectionHandler
from infra.entities.estoque import Estoque, Fabricantes
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql import text
from sqlalchemy import asc, desc, or_


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
                        Estoque.SALDO,
                        Estoque.PC
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

    def my_insert(self, codint, codfabr, produto, idfabr: int, saldo: float, pc: int):
        with DBConnectionHandler() as db:
            try:
                data_insert = Estoque(COD_INT=codint, COD_FABR=codfabr, PRODUTO=produto,
                                      ID_FABR=idfabr, SALDO=saldo, PC=pc)
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

    def my_update(self, codfabr_old, codint, codfabr, produto, idfabr: int, saldo: float):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.COD_FABR == codfabr_old).update({
                    "COD_INT": codint, "COD_FABR": codfabr, "PRODUTO": produto,
                    "ID_FABR": idfabr, "SALDO": saldo})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_updsaldo(self, codfabr, saldo: float):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.COD_FABR == codfabr).update({
                    "SALDO": saldo})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_updpc(self, codfabr, pc: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Estoque).filter(Estoque.COD_FABR == codfabr).update({
                    "PC": pc})
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_count(self, **kwargs):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Estoque).filter_by(**kwargs).count()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_orderby(self, descendente=False, **kwargs):
        coluna = kwargs.pop('coluna', None)
        self.desc = descendente
        with DBConnectionHandler() as db:
            try:
                if self.desc is True:
                    data = db.session.query(Estoque)\
                        .select_from(Fabricantes)\
                        .join(Estoque, Fabricantes.ID_FABR == Estoque.ID_FABR)\
                        .with_entities(
                            Estoque.COD_INT,
                            Estoque.COD_FABR,
                            Estoque.PRODUTO,
                            Fabricantes.NOMEFABR,
                            Estoque.SALDO,
                            Estoque.PC)\
                        .order_by(desc(text(coluna)))\
                        .all()
                else:
                    data = db.session.query(Estoque)\
                        .select_from(Fabricantes)\
                        .join(Estoque, Fabricantes.ID_FABR == Estoque.ID_FABR)\
                        .with_entities(
                            Estoque.COD_INT,
                            Estoque.COD_FABR,
                            Estoque.PRODUTO,
                            Fabricantes.NOMEFABR,
                            Estoque.SALDO,
                            Estoque.PC)\
                        .order_by(asc(text(coluna)))\
                        .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_orderby_fabr(self, descendente=False):
        self.desc = descendente
        with DBConnectionHandler() as db:
            try:
                if self.desc is True:
                    data = db.session.query(Estoque)\
                        .select_from(Fabricantes)\
                        .join(Estoque, Fabricantes.ID_FABR == Estoque.ID_FABR)\
                        .with_entities(
                            Estoque.COD_INT,
                            Estoque.COD_FABR,
                            Estoque.PRODUTO,
                            Fabricantes.NOMEFABR,
                            Estoque.SALDO,
                            Estoque.PC)\
                        .order_by(desc(Fabricantes.NOMEFABR)).order_by(desc(Estoque.PRODUTO))\
                        .all()
                else:
                    data = db.session.query(Estoque)\
                        .select_from(Fabricantes)\
                        .join(Estoque, Fabricantes.ID_FABR == Estoque.ID_FABR)\
                        .with_entities(
                            Estoque.COD_INT,
                            Estoque.COD_FABR,
                            Estoque.PRODUTO,
                            Fabricantes.NOMEFABR,
                            Estoque.SALDO,
                            Estoque.PC)\
                        .order_by(asc(Fabricantes.NOMEFABR)).order_by(asc(Estoque.PRODUTO))\
                        .all()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def my_pesquisa(self, **kwargs):
        coluna = kwargs.pop('coluna', None)
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
                        Estoque.SALDO,
                        Estoque.PC)\
                    .filter(or_(Estoque.PRODUTO.like(coluna),
                                Estoque.COD_INT.like(coluna),
                                Fabricantes.NOMEFABR.like(coluna),
                                Estoque.COD_FABR.like(coluna)))\
                    .all()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
