import sys
from datetime import datetime

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QMainWindow,
                               QTableWidgetItem, QWidget)
from qt_material import apply_stylesheet, list_themes

from infra.repository.entradas_repo import EntradasRepo
from infra.repository.estoque_repo import EstoqueRepo
from infra.repository.fabricante_repo import FabricantesRepo
from ui_mainwindow import Ui_MainWindow
from ui_wind_addforn import Ui_wind_add_forn
from ui_wind_addprod import Ui_wind_add_prod
from ui_wind_entraprod import Ui_wind_entr_prod


class TableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = columns

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

    def data(self, index, role):
        value = self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return "%.2f" % value
            # Default (anything not captured above: e.g. int)
            return value
        if role == Qt.TextAlignmentRole:
            if index.column() == 0:
                return Qt.AlignVCenter + Qt.AlignHCenter
            if isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight
            if isinstance(value, int):
                return Qt.AlignVCenter + Qt.AlignHCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class Jan_Entr_Prod(QWidget, Ui_wind_entr_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_entr.clicked.connect(self.confirma_entr_prod)
        self.pb_cancela_entr.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_entr.clicked.connect(self.close_jan_entrprod)

    def confirma_entr_prod(self):
        data = self.le_data.text()
        quantidade = self.le_quant.text()
        if not data or not quantidade:
            window.show_mensagem(
                '>> Data e/ou Quantidade não podem ser vazios!')
            return
        registro = window.indice
        df, conn = window.conectar("ESTOQUE")
        df1 = df.query('`PROD_ID` == @registro')

        saldo = df.loc[df1.index, 'SALDO']
        saldo = saldo + float(self.le_quant.text())
        df.loc[df1.index, 'SALDO'] = saldo
        df.to_sql('ESTOQUE', conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()

        data = pd.to_datetime(pd.Series(data), dayfirst=True)
        dtForm_usa = data.dt.strftime('%Y-%m-%d')
        dtForm_br = data.dt.strftime('%d-%m-%Y')

        data_usa = dtForm_usa.values
        data_br = dtForm_br.values

        for x in df1.values:
            lista = x
        lst_nova = []
        lst_nova.append(data_usa[0])
        lst_nova.append(float(quantidade))
        lst_nova.append(lista[1])
        lst_nova.append(lista[2])
        lst_nova.append(lista[3])
        df, conn = window.conectar("ENTRADAS")
        df.loc[len(df)] = lst_nova
        df.to_sql('ENTRADAS', conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        window.dados_entradas()
        window.dados_prod()
        window.show_mensagem('>> Entrada de produto efetuada com sucesso')
        self.close_jan_entrprod()

    def close_jan_entrprod(self):
        window.pb_entrada.setEnabled(True)
        self.close()


class Jan_Alt_Prod(QWidget, Ui_wind_add_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_prod.clicked.connect(self.confirma_alt_prod)
        self.pb_cancela_prod.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_prod.clicked.connect(self.close_jan_altprod)

    def confirma_alt_prod(self):
        codint = self.le_codint.text()
        codfabr = self.le_codforn.text()
        descprod = self.le_descprod.text()
        if not descprod or not codfabr:
            window.show_mensagem(
                '>> Descrição do Produto e/ou Código do Fabricante não podem ser vazios!')
            return
        codfabr_old = window.codfabr_old

        nomefabr = self.cb_fornec.currentText()
        id_fabr = FabricantesRepo.my_select_one(self, **{"NOMEFABR": nomefabr})
        saldo = EstoqueRepo.my_select_one(self, **{"COD_FABR": codfabr_old})
        EstoqueRepo.my_update(self, codfabr_old=codfabr_old,
                              codint=codint,
                              codfabr=codfabr,
                              produto=descprod,
                              idfabr=id_fabr.ID_FABR,
                              saldo=saldo.SALDO)

        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.show_mensagem('>> Produto alterado com sucesso!')
        self.close_jan_altprod()

    def close_jan_altprod(self):
        window.pb_alterar.setEnabled(True)
        self.close()


class Jan_Alt_Forn(QWidget, Ui_wind_add_forn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_forn.clicked.connect(self.confirma_alt_forn)
        self.pb_cancela_forn.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_forn.clicked.connect(self.close_jan_altforn)

    def confirma_alt_forn(self):
        altforn = []
        registro = window.indice

        df, conn = window.conectar("FABRICANTES")
        df1 = df.query('`FORN_ID` == @registro')

        altforn.append(registro)
        altforn.append(self.le_nomeforn.text())

        df.loc[df1.index] = altforn
        df.to_sql('FABRICANTES', conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        window.dados_forn()
        window.show_mensagem('>> Fornecedor alterado com sucesso!')
        self.close_jan_altforn()

    def close_jan_altforn(self):
        window.pb_alterar.setEnabled(True)
        self.close()


class Jan_Add_Prod(QWidget, Ui_wind_add_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_prod.clicked.connect(self.confirma_prod)
        self.pb_cancela_prod.clicked.connect(self.close_janprod)
        self.pb_cancela_prod.clicked.connect(window.show_mensagem(''))

    def confirma_prod(self):
        codint = self.le_codint.text()
        codfabr = self.le_codforn.text()
        descprod = self.le_descprod.text()
        if not descprod or not codfabr:
            window.show_mensagem(
                '>> Descrição do Produto e/ou Código do Fabricante não podem ser vazios!')
            return
        result = EstoqueRepo.my_select_one(self, **{"COD_FABR": codfabr})
        if result is not None:
            window.show_mensagem('>> Código do Fabricante já cadastrado!')
            return
        result = EstoqueRepo.my_select_one(self, **{"PRODUTO": descprod})
        if result is not None:
            window.show_mensagem('>> Descrição do Produto já cadastrada!')
            return
        result = EstoqueRepo.my_select_one(self, **{"COD_INT": codint})
        if result is not None:
            window.show_mensagem('>> Código Interno já cadastrado!')
            return

        nomefabr = self.cb_fornec.currentText()
        id_fabr = FabricantesRepo.my_select_one(self, **{"NOMEFABR": nomefabr})
        EstoqueRepo.my_insert(self,
                              codint=codint,
                              codfabr=codfabr,
                              produto=descprod,
                              idfabr=id_fabr.ID_FABR,
                              saldo=0.0)
        window.tw_prod.scrollToBottom()
        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.show_mensagem('>> Produto adicionado com sucesso!')
        self.close_janprod()

    def close_janprod(self):
        window.pb_adicionar.setEnabled(True)
        self.close()


class Jan_Add_Forn(QWidget, Ui_wind_add_forn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_forn.clicked.connect(self.confirma_forn)
        self.pb_cancela_forn.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_forn.clicked.connect(self.close_janforn)

    def confirma_forn(self):
        nomefabr = self.le_nomeforn.text()
        if not nomefabr:
            window.show_mensagem(
                '>> Nome do Fabricante não pode ser vazio!')
            return
        result = FabricantesRepo.my_select_one(self, **{"NOMEFABR": nomefabr})
        if result is not None:
            window.show_mensagem('>> Fabricante já cadastrado!')
            return

        FabricantesRepo.my_insert(self, nomefabr=nomefabr)
        window.tw_fornec.scrollToBottom()
        window.carrega_dados("FABRICANTES", window.tw_fornec)
        window.show_mensagem('>> Fornecedor adicionado com sucesso!')
        self.close_janforn()

    def close_janforn(self):
        window.pb_adicionar.setEnabled(True)
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow, Ui_wind_add_prod,
                 Ui_wind_add_forn):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        MainWindow.resize(self, 800, 600)
        self.setWindowTitle("Sistema de Controle de Estoque")

        self.tw_prod.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tw_fornec.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.tw_entradas.setColumnWidth(0, 150)
        self.tw_entradas.setColumnWidth(1, 150)
        self.tw_entradas.setColumnWidth(2, 150)
        self.tw_entradas.setColumnWidth(3, 300)

        self.tabWidget.setCurrentIndex(0)

        self.estilos()

        self.slots()

        self.carrega_dados("ESTOQUE", self.tw_prod)

        self.carrega_dados("FABRICANTES", self.tw_fornec)

        self.carrega_dados("ENTRADAS", self.tw_entradas)

# !=================== FUNÇÕES ============================

    def carrega_dados(self, tabela, tab_widget):
        if tabela == "ESTOQUE":
            self.registros = EstoqueRepo.my_select(self)
            self.colunas = ['Cód. Interno', 'Cód. Fabricante',
                            'Descrição do Produto', 'Fabricante', 'Saldo']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 150)
            tab_widget.setColumnWidth(1, 300)
            tab_widget.setColumnWidth(2, 700)
            tab_widget.setColumnWidth(3, 200)
            tab_widget.setColumnWidth(4, 100)
        elif tabela == "FABRICANTES":
            self.registros = FabricantesRepo.my_select(self)
            self.colunas = ['Fabricante ID', 'Nome do Fabricante']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 150)
            tab_widget.setColumnWidth(1, 700)
        elif tabela == "ENTRADAS":
            self.registros = EntradasRepo.my_select(self)
            self.colunas = ['Data de Entrada', 'Quantidade', 'Código do Fabricante']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 200)
            tab_widget.setColumnWidth(1, 200)
            tab_widget.setColumnWidth(2, 300)

    def adicionar(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:                                # !ADICIONAR PRODUTOS
            self.reg_fabr = FabricantesRepo.my_select(self)
            self.jan_add_prod = Jan_Add_Prod()
            self.jan_add_prod.cb_fornec.clear()
            for item in self.reg_fabr:
                self.jan_add_prod.cb_fornec.addItem(str(item[1]))
            self.pb_adicionar.setEnabled(False)
            self.jan_add_prod.show()
        elif aba == 1:                              # !ADICIONAR FABRICANTES
            self.jan_add_forn = Jan_Add_Forn()
            self.pb_adicionar.setEnabled(False)
            self.jan_add_forn.show()

    def excluir(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! EXCLUIR PRODUTOS
            registro = self.tw_prod.selectionModel().selectedRows(column=1)
            if len(registro) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para exclusão!')
                return
            codfabr = registro[0].data()
            EstoqueRepo.my_delete(self, codfabr)
            self.carrega_dados("ESTOQUE", self.tw_prod)
            self.show_mensagem('>> Produto excluído com sucesso!')
        elif aba == 1:      # ! EXCLUIR FORNECEDOR
            registro = self.tw_fornec.selectionModel().selectedRows(column=0)
            if len(registro) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para exclusão!')
                return
            idfabr = registro[0].data()
            FabricantesRepo.my_delete(self, idfabr)
            self.carrega_dados("FABRICANTES", self.tw_fornec)
            self.show_mensagem('>> Fornecedor excluído com sucesso!')

    def alterar(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:
            codint = self.tw_prod.selectionModel().selectedRows(column=0)
            codfabr = self.tw_prod.selectionModel().selectedRows(column=1)
            descprod = self.tw_prod.selectionModel().selectedRows(column=2)
            nomefabr = self.tw_prod.selectionModel().selectedRows(column=3)
            if len(codint) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para exclusão!')
                return
            self.codfabr_old = codfabr[0].data()
            self.reg_fabr = FabricantesRepo.my_select(self)
            self.jan_alt_prod = Jan_Alt_Prod()
            self.jan_alt_prod.cb_fornec.clear()
            for item in self.reg_fabr:
                self.jan_alt_prod.cb_fornec.addItem(str(item[1]))
            ind = self.jan_alt_prod.cb_fornec.findText(nomefabr[0].data())
            self.jan_alt_prod.cb_fornec.setCurrentIndex(ind)
            self.jan_alt_prod.le_codint.setText(codint[0].data())
            self.jan_alt_prod.le_codforn.setText(codfabr[0].data())
            self.jan_alt_prod.le_descprod.setText(descprod[0].data())
            self.pb_alterar.setEnabled(False)
            self.jan_alt_prod.show()
        elif aba == 1:
            row = self.tw_fornec.currentRow()
            if row == -1:
                self.show_mensagem(
                    '>> Favor selecionar um item para alteração!')
                return
            self.indice = int(QTableWidgetItem.text(
                self.tw_fornec.item(row, 0)))
            itens = self.tw_fornec.selectedItems()
            self.jan_alt_forn = Jan_Alt_Forn()
            self.jan_alt_forn.le_nomeforn.setText(itens[1].text())
            self.pb_alterar.setEnabled(False)
            self.jan_alt_forn.show()

    def entrada(self):
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! ENTRADA DE PRODUTOS
            row = self.tw_prod.currentRow()
            if row == -1:
                self.show_mensagem(
                    '>> Favor selecionar um item para efetuar a entrada!')
                return
            registro = QTableWidgetItem.text(self.tw_prod.item(row, 1))
            df, conn = self.conectar("ESTOQUE")
            df1 = df.query('`COD_FABR` == @registro')
            conn.close()
            for x in df1.values:
                lst_item = x
            self.janEntrProd = Jan_Entr_Prod()
            self.indice = lst_item[0]
            self.janEntrProd.cp_codint.setText(lst_item[0])
            self.janEntrProd.cp_codfabr.setText(lst_item[1])
            self.janEntrProd.cp_descprod.setText(lst_item[2])
            self.janEntrProd.cp_saldo.setText(str(lst_item[4]))
            self.pb_entrada.setEnabled(False)
            self.janEntrProd.show()
            self.dados_prod()
            self.show_mensagem('>> Entrada de produtos efetuada com sucesso!')

    def reindex(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:
            df, conn = self.conectar("ESTOQUE")
            novoindice = 0
            for itens in range(df.shape[0]):
                novoindice += 1
                df.iat[itens, 0] = novoindice
            df.to_sql("ESTOQUE", conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.tw_prod.scrollToBottom()
            self.dados_prod()
            self.show_mensagem(
                '>> Re-indexação dos Produtos concluída com sucesso!')
        elif aba == 1:
            df, conn = self.conectar("FABRICANTES")
            novoindice = 0
            for itens in range(df.shape[0]):
                novoindice += 1
                df.iat[itens, 0] = novoindice
            df.to_sql("FABRICANTES", conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.tw_fornec.scrollToBottom()
            self.dados_forn()
            self.show_mensagem(
                '>> Re-indexação dos Fornecedores concluída com sucesso!')

    def estilos(self):

        self.extra = {
            # Font
            'font_family': 'Arial',
            'font_size': '14px',
            'line_height': '14px',

            'pyside6': True,
        }

        self.temas = list_themes()
        self.cb_temas.clear()
        self.cb_temas.addItems(self.temas)
        self.cb_temas.setCurrentIndex(8)
        self.muda_tema('dark_teal.xml')

    def muda_tema(self, t):
        apply_stylesheet(app, theme=t, invert_secondary=False,
                         extra=self.extra)

    def left_menu(self):
        width = self.fr_esquerda.width()
        if width == 9:
            newWidth = 250
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(
            self.fr_esquerda, b"maximumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def Ativa_filtro(self):
        if self.rb_filtro.isChecked():
            self.tw_prod.setSortingEnabled(True)
            self.tw_fornec.setSortingEnabled(True)
        else:
            self.tw_prod.setSortingEnabled(False)
            self.tw_fornec.setSortingEnabled(False)
            self.carrega_dados("ESTOQUE", self.tw_prod)
            self.carrega_dados("FABRICANTES", self.tw_fornec)

    def Ativa_entr_filtro(self):
        if self.rb_entr_filtro.isChecked():
            self.tw_entradas.setSortingEnabled(True)
        else:
            self.tw_entradas.setSortingEnabled(False)
            self.dados_entradas()

    def pagina(self, x):
        self.lb_pagina.setText(x)
        self.lb_pagina.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def slots(self):
        self.cb_temas.currentTextChanged.connect(self.muda_tema)
        self.pb_menu.clicked.connect(self.left_menu)
        self.pb_cadastros.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.Cadastros))
        self.pb_cadastros.clicked.connect(lambda: self.pagina('CADASTROS'))
        self.pb_entradas.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_entradas.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.Entradas))
        self.pb_entradas.clicked.connect(lambda: self.pagina('ENTRADAS'))
        self.pb_saidas.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.Saidas))
        self.pb_saidas.clicked.connect(lambda: self.pagina('SAÍDAS'))
        self.pb_compra.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.PontoCompra))
        self.pb_compra.clicked.connect(lambda: self.pagina('PONTO DE COMPRAS'))

        self.pb_adicionar.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_adicionar.clicked.connect(lambda: self.adicionar())
        self.pb_excluir.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_excluir.clicked.connect(lambda: self.excluir())
        self.pb_alterar.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_alterar.clicked.connect(lambda: self.alterar())
        self.pb_entrada.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_entrada.clicked.connect(lambda: self.entrada())
        self.pb_reindex.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_reindex.clicked.connect(lambda: self.reindex())

        self.rb_filtro.toggled.connect(self.Ativa_filtro)
        self.rb_entr_filtro.toggled.connect(self.Ativa_entr_filtro)

    def show_mensagem(self, m):
        self.lb_mensagens.setText(m)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()

    extra = {
            # Font
            'font_family': 'Arial',
            'font_size': '14px',
            'line_height': '14px',

            'pyside6': True,
        }

    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=False, extra=extra)
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
