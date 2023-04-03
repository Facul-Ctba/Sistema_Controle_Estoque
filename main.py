import sqlite3 as sql
import sys

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QMainWindow,
                               QTableWidgetItem, QWidget)
from qt_material import apply_stylesheet, list_themes

from ui_mainwindow import Ui_MainWindow
from ui_wind_addforn import Ui_wind_add_forn
from ui_wind_addprod import Ui_wind_add_prod


class Jan_Alt_Prod(QWidget, Ui_wind_add_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_confirma_prod.clicked.connect(self.confirma_alt_prod)
        self.pb_cancela_prod.clicked.connect(self.close_jan_altprod)

    def confirma_alt_prod(self):
        altprod = []
        registro = window.indice

        df, conn = window.conectar("PRODUTOS")
        df1 = df.query('`PROD_ID` == @registro')

        altprod.append(registro)
        altprod.append(self.le_codint.text())
        altprod.append(self.le_codforn.text())
        altprod.append(self.le_descprod.text())
        altprod.append(self.cb_fornec.currentText())
        altprod.append(df1.at[registro-1, "SALDO"])

        df.loc[df1.index] = altprod
        df.to_sql('PRODUTOS', conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        window.dados_prod()
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
        self.pb_cancela_forn.clicked.connect(self.close_jan_altforn)

    def confirma_alt_forn(self):
        altforn = []
        registro = window.indice

        df, conn = window.conectar("FORNECEDORES")
        df1 = df.query('`FORN_ID` == @registro')

        altforn.append(registro)
        altforn.append(self.le_nomeforn.text())

        df.loc[df1.index] = altforn
        df.to_sql('FORNECEDORES', conn, if_exists="replace", index=False)
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

    def confirma_prod(self):
        teste1 = self.le_descprod.text()
        teste2 = self.le_codforn.text()
        if not teste1 or not teste2:
            window.show_mensagem(
                '>> Descrição do Produto e/ou Código do Fabricante não podem ser vazios!')
            return
        addprod = []
        dfprod, conn = window.conectar("PRODUTOS")
        lastrow = dfprod.shape[0]-1
        ultID = int(dfprod.at[lastrow, 'PROD_ID'])
        novoID = ultID+1

        serie = dfprod['COD_FORN'].squeeze()
        result = serie.str.match(teste2, case=False)
        for i in result.values:
            if i == True:
                window.show_mensagem('>> Produto já cadastrado!')
                return
        serie = dfprod['PRODUTO'].squeeze()
        result = serie.str.match(teste1, case=False)
        for i in result.values:
            if i == True:
                window.show_mensagem('>> Produto já cadastrado!')
                return

        addprod.append(novoID)
        addprod.append(self.le_codint.text())
        addprod.append(self.le_codforn.text())
        addprod.append(self.le_descprod.text())
        addprod.append(self.cb_fornec.currentText())
        addprod.append(0.0)      # ! Saldo

        dfprod.loc[novoID] = addprod
        dfprod.to_sql("PRODUTOS", conn, if_exists="replace", index=False)

        conn.commit()
        conn.close()
        window.tw_prod.scrollToBottom()
        window.dados_prod()
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
        self.pb_cancela_forn.clicked.connect(self.close_janforn)

    def confirma_forn(self):
        teste1 = self.le_nomeforn.text()
        if not teste1:
            window.show_mensagem(
                '>> Nome do Fabricante não pode ser vazio!')
            return
        addforn = []
        dfforn, conn = window.conectar("FORNECEDORES")
        lastrow = dfforn.shape[0]-1
        ultID = int(dfforn.at[lastrow, 'FORN_ID'])
        novoID = ultID+1

        serie = dfforn['FORN_NOME'].squeeze()
        result = serie.str.match(teste1, case=False)
        for i in result.values:
            if i == True:
                window.show_mensagem('>> Fabricante já cadastrado!')
                return

        addforn.append(novoID)
        addforn.append(self.le_nomeforn.text())

        dfforn.loc[novoID] = addforn
        dfforn.to_sql("FORNECEDORES", conn, if_exists="replace", index=False)

        conn.commit()
        conn.close()
        window.tw_fornec.scrollToBottom()
        window.dados_forn()
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
        # self.showMaximized()

        self.tw_prod.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tw_fornec.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.estilos()

        self.slots()

        self.dados_prod()

        self.dados_forn()

        self.tw_prod.setColumnWidth(0, 60)
        self.tw_prod.setColumnWidth(1, 150)
        self.tw_prod.setColumnWidth(2, 300)
        self.tw_prod.setColumnWidth(3, 700)
        self.tw_prod.setColumnWidth(4, 200)
        self.tw_prod.setColumnWidth(5, 100)

        self.tabWidget.setCurrentIndex(0)

# !=================== FUNÇÕES ============================

    def conectar(self, tabela):
        conn = sql.connect("bd_estoque.db")
        df = pd.read_sql(f"select * from {tabela}", conn)
        return df, conn

    def dados_prod(self):
        self.replace = {'COD_INT': '', 'COD_FORN': '', 'FORN_NOME': '',
                        'SALDO': 0.0}
        self.carrega_dados(tabela='PRODUTOS', replace=self.replace,
                           tab_widget=self.tw_prod)

    def dados_forn(self):
        self.replace = {'FORN_NOME': ''}
        self.carrega_dados(tabela='FORNECEDORES', replace=self.replace,
                           tab_widget=self.tw_fornec)

    def carrega_dados(self, tabela, replace, tab_widget):
        df, conn = self.conectar(tabela)

        df.fillna(value=replace, inplace=True)
        df.to_sql(tabela, conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()

        tab_widget.setRowCount(df.shape[0])
        tab_widget.setColumnCount(df.shape[1])
        for item in df.iterrows():     # ! Alimenta a Table Widget
            values = item[1]
            for col, valor in enumerate(values):
                item_tabela = QTableWidgetItem(str(valor))
                if tabela == 'PRODUTOS':
                    if col in [0, 1, 5]:
                        item_tabela.setTextAlignment(Qt.AlignHCenter)
                else:
                    if col == 0:
                        item_tabela.setTextAlignment(Qt.AlignHCenter)
                tab_widget.setItem(item[0], col, item_tabela)

    def adicionar(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:                                # !ADICIONAR PRODUTOS
            self.jan_add_prod = Jan_Add_Prod()
            self.enche_cbforn(self.jan_add_prod)
            self.pb_adicionar.setEnabled(False)
            self.jan_add_prod.show()
        elif aba == 1:                              # !ADICIONAR FABRICANTES
            self.jan_add_forn = Jan_Add_Forn()
            self.pb_adicionar.setEnabled(False)
            self.jan_add_forn.show()

    def enche_cbforn(self, janela):
        self.janela = janela
        df, conn = self.conectar("FORNECEDORES")
        self.janela.cb_fornec.clear()
        for item in df.itertuples(False, 'reg'):
            self.janela.cb_fornec.addItem(str(item[1]))
        conn.close()

    def excluir(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! EXCLUIR PRODUTOS
            row = self.tw_prod.currentRow()
            if row == -1:
                self.show_mensagem(
                    '>> Favor selecionar um item para exclusão!')
                return
            registro = int(QTableWidgetItem.text(self.tw_prod.item(row, 0)))
            dfprod, conn = self.conectar("PRODUTOS")
            df1 = dfprod.query('`PROD_ID` == @registro')
            dfprod.drop(df1.index, inplace=True)
            dfprod.to_sql('PRODUTOS', conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.dados_prod()
            self.show_mensagem('>> Produto excluído com sucesso!')
        elif aba == 1:      # ! EXCLUIR FORNECEDOR
            row = self.tw_fornec.currentRow()
            if row == -1:
                self.show_mensagem(
                    '>> Favor selecionar um item para exclusão!')
                return
            registro = int(QTableWidgetItem.text(self.tw_fornec.item(row, 0)))
            print(registro)
            dfforn, conn = self.conectar("FORNECEDORES")
            df1 = dfforn.query('`FORN_ID` == @registro')
            dfforn.drop(df1.index, inplace=True)
            dfforn.to_sql('FORNECEDORES', conn,
                          if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.dados_forn()
            self.show_mensagem('>> Fornecedor excluído com sucesso!')

    def alterar(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:
            row = self.tw_prod.currentRow()
            if row == -1:
                self.show_mensagem(
                    '>> Favor selecionar um item para alteração!')
                return
            self.indice = int(QTableWidgetItem.text(self.tw_prod.item(row, 0)))
            itens = self.tw_prod.selectedItems()
            self.jan_alt_prod = Jan_Alt_Prod()
            self.jan_alt_prod.le_codint.setText(itens[1].text())
            self.jan_alt_prod.le_codforn.setText(itens[2].text())
            self.jan_alt_prod.le_descprod.setText(itens[3].text())
            self.enche_cbforn(self.jan_alt_prod)
            ind = self.jan_alt_prod.cb_fornec.findText(itens[4].text())
            self.jan_alt_prod.cb_fornec.setCurrentIndex(ind)
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

    def reindex(self):
        self.show_mensagem('')
        aba = self.tabWidget.currentIndex()
        if aba == 0:
            df, conn = self.conectar("PRODUTOS")
            novoindice = 0
            for itens in range(df.shape[0]):
                novoindice += 1
                df.iat[itens, 0] = novoindice
            df.to_sql("PRODUTOS", conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.tw_prod.scrollToBottom()
            self.dados_prod()
            self.show_mensagem(
                '>> Re-indexação dos Produtos concluída com sucesso!')
        elif aba == 1:
            df, conn = self.conectar("FORNECEDORES")
            novoindice = 0
            for itens in range(df.shape[0]):
                novoindice += 1
                df.iat[itens, 0] = novoindice
            df.to_sql("FORNECEDORES", conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.tw_fornec.scrollToBottom()
            self.dados_forn()
            self.show_mensagem(
                '>> Re-indexação dos Fornecedores concluída com sucesso!')

    def estilos(self):

        self.extra = {
            # Button colors
            'danger': '#dc3545',
            'warning': '#ffc107',
            'success': '#17a2b8',
            # Font
            'font_family': 'Arial',
        }

        self.temas = list_themes()
        for x in self.temas:
            self.cb_temas.addItem(x)

    def muda_tema(self, t):
        apply_stylesheet(app, theme=t, invert_secondary=False,
                         extra=self.extra)

    def left_menu(self):
        width = self.fr_esquerda.width()
        if width == 9:
            newWidth = 200
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
            self.dados_prod()
            self.dados_forn()

    def slots(self):
        self.cb_temas.currentTextChanged.connect(self.muda_tema)
        self.pb_menu.clicked.connect(self.left_menu)
        self.pb_cadastros.clicked.connect(
            lambda: self.sw_paginas.setCurrentWidget(self.Cadastros))
        self.pb_entradas.clicked.connect(
            lambda: self.sw_paginas.setCurrentWidget(self.Entadas))
        self.pb_saidas.clicked.connect(
            lambda: self.sw_paginas.setCurrentWidget(self.Saidas))
        self.pb_compra.clicked.connect(
            lambda: self.sw_paginas.setCurrentWidget(self.PontoCompra))

        self.pb_adicionar.clicked.connect(lambda: self.adicionar())
        self.pb_excluir.clicked.connect(lambda: self.excluir())
        self.pb_alterar.clicked.connect(lambda: self.alterar())
        self.pb_reindex.clicked.connect(lambda: self.reindex())

        self.rb_filtro.toggled.connect(self.Ativa_filtro)

    def show_mensagem(self, m):
        self.lb_mensagens.setText(m)


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()

    app.setStyle('Fusion')
    apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=False)

    window.show()
    sys.exit(app.exec())
