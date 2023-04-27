import sys
from datetime import datetime

from PySide6 import QtCore
from PySide6.QtCore import QAbstractTableModel, QEvent, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QMainWindow,
                               QMessageBox, QStyle, QWidget)
from qt_material import apply_stylesheet, list_themes

from infra.repository.compras_repo import ComprasRepo
from infra.repository.entradas_repo import EntradasRepo
from infra.repository.estoque_repo import EstoqueRepo
from infra.repository.fabricante_repo import FabricantesRepo
from infra.repository.saidas_repo import SaidasRepo
from ui_mainwindow import Ui_MainWindow
from ui_wind_addcompra import Ui_wind_add_compra
from ui_wind_addforn import Ui_wind_add_forn
from ui_wind_addprod import Ui_wind_add_prod
from ui_wind_entraprod import Ui_wind_entr_prod
from ui_wind_saidaprod import Ui_wind_saida_prod


class TableModel(QAbstractTableModel):
    def __init__(self, data, columns, icon=None):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = columns
        self.icon = icon

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
            if index.column() == 5:
                return None
            else:
                return value

        if role == Qt.TextAlignmentRole:
            if index.column() == 0:
                return Qt.AlignVCenter + Qt.AlignHCenter
            if isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight
            if isinstance(value, int):
                return Qt.AlignVCenter + Qt.AlignHCenter

        if role == Qt.DecorationRole:
            if index.column() == 5:
                if value == 1:
                    if self.icon:
                        return QIcon(self.icon)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class Jan_Compra_Prod(QWidget, Ui_wind_add_compra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.pb_confirma_compra.clicked.connect(self.confirma_compra_prod)
        self.pb_cancela_compra.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_compra.clicked.connect(self.close_jan_compraprod)

    def confirma_compra_prod(self):
        quantidade = self.le_compra_quant.text()
        if not quantidade:
            window.show_mensagem('>> Quantidade não pode ser vazia!')
            return
        idprod = EstoqueRepo.my_select_one(self, **{"COD_FABR": self.cp_codfabr.text()})
        if window.lim_min is None:
            ComprasRepo.my_insert(self, pcidprod=idprod.ID_PROD, pclimmin=float(quantidade))
        else:
            ComprasRepo.my_update(self, pcidprod=idprod.ID_PROD, pclimmin=float(quantidade))
        window.carrega_dados("COMPRAS", window.tw_compras)
        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.show_mensagem('>> Ponto de Compra adicionado com sucesso')
        self.close_jan_compraprod()

    def close_jan_compraprod(self):
        window.pb_compra.setEnabled(True)
        self.close()


class Jan_Entr_Prod(QWidget, Ui_wind_entr_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.pb_confirma_entr.clicked.connect(self.confirma_entr_prod)
        self.pb_cancela_entr.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_entr.clicked.connect(self.close_jan_entrprod)

        self.le_data.returnPressed.connect(self.le_quant.setFocus)
        self.le_quant.returnPressed.connect(self.le_data.setFocus)

    def confirma_entr_prod(self):
        data = self.le_data.text()
        quantidade = self.le_quant.text()
        if not data or not quantidade:
            window.show_mensagem(
                '>> Data e/ou Quantidade não podem ser vazios!')
            return
        saldo = float(self.cp_saldo.text())
        saldo = saldo + float(quantidade)
        idprod = EstoqueRepo.my_select_one(self, **{"COD_FABR": self.cp_codfabr.text()})
        EntradasRepo.my_insert(self, indata=data, inquant=float(quantidade), inidprod=idprod.ID_PROD)
        EstoqueRepo.my_updsaldo(self, codfabr=self.cp_codfabr.text(), saldo=saldo)
        window.carrega_dados("ENTRADAS", window.tw_entradas)
        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.carrega_dados("COMPRAS", window.tw_compras)
        window.show_mensagem('>> Entrada de produto efetuada com sucesso')
        self.close_jan_entrprod()

    def close_jan_entrprod(self):
        window.pb_entrada.setEnabled(True)
        self.close()


class Jan_Saida_Prod(QWidget, Ui_wind_saida_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.pb_confirma_entr.clicked.connect(self.confirma_saida_prod)
        self.pb_cancela_entr.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_entr.clicked.connect(self.close_jan_saidaprod)

        self.le_data.returnPressed.connect(self.le_quant.setFocus)
        self.le_quant.returnPressed.connect(self.le_destino.setFocus)
        self.le_destino.returnPressed.connect(self.le_data.setFocus)

    def confirma_saida_prod(self):
        data = self.le_data.text()
        quantidade = self.le_quant.text()
        destino = self.le_destino.text()
        if not data or not quantidade or not destino:
            window.show_mensagem(
                '>> Todos os campos devem ser preenchidos!')
            return
        saldo = float(self.cp_saldo.text())
        if float(quantidade) > saldo:
            window.show_mensagem('>> Quantidado de Saída maior que o Saldo não permitida!')
            return
        saldo = saldo - float(quantidade)
        idprod = EstoqueRepo.my_select_one(self, **{"COD_FABR": self.cp_codfabr.text()})
        SaidasRepo.my_insert(self, outdata=data, outquant=float(quantidade),
                             outidprod=idprod.ID_PROD, outdestino=destino)
        EstoqueRepo.my_updsaldo(self, codfabr=self.cp_codfabr.text(), saldo=saldo)
        window.carrega_dados("SAIDAS", window.tw_saidas)
        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.show_mensagem('>> Saída de produto efetuada com sucesso')
        self.close_jan_saidaprod()

    def close_jan_saidaprod(self):
        window.pb_saida.setEnabled(True)
        self.close()


class Jan_Alt_Prod(QWidget, Ui_wind_add_prod):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)
        self.setWindowTitle('Alteração de Produto Cadastrado')

        self.pb_confirma_prod.clicked.connect(self.confirma_alt_prod)
        self.pb_cancela_prod.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_prod.clicked.connect(self.close_jan_altprod)

        self.le_codint.returnPressed.connect(self.le_codforn.setFocus)
        self.le_codforn.returnPressed.connect(self.le_descprod.setFocus)
        self.le_descprod.returnPressed.connect(self.le_codint.setFocus)

    def confirma_alt_prod(self):
        codint = self.le_codint.text()
        codfabr = self.le_codforn.text()
        descprod = self.le_descprod.text()
        if not descprod or not codfabr:
            window.show_mensagem(
                '>> Descrição do Produto e/ou Código do Fabricante não podem ser vazios!')
            return
        codint_old = window.codint_old
        codfabr_old = window.codfabr_old
        if codint != codint_old:        # !Alterado Codigo Interno
            result = EstoqueRepo.my_count(self, **{"COD_INT": codint})
            if result > 0:
                window.show_mensagem(">> Código Interno já cadastrado!")
                return
        if codfabr != codfabr_old:        # !Alterado Codigo fabricante
            result = EstoqueRepo.my_count(self, **{"COD_FABR": codfabr})
            if result > 0:
                window.show_mensagem(">> Código do Fabricante já cadastrado!")
                return
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
        window.carrega_dados("ENTRADAS", window.tw_entradas)
        window.show_mensagem('>> Produto alterado com sucesso!')
        self.close_jan_altprod()

    def close_jan_altprod(self):
        window.pb_alterar.setEnabled(True)
        self.close()


class Jan_Alt_Forn(QWidget, Ui_wind_add_forn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.setWindowTitle("Alteração de Fabricante Cadastrado")
        self.pb_confirma_forn.clicked.connect(self.confirma_alt_forn)
        self.pb_cancela_forn.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_forn.clicked.connect(self.close_jan_altforn)

    def confirma_alt_forn(self):
        nomefabr = self.le_nomeforn.text()
        if not nomefabr:
            window.show_mensagem('>> Nome do Fronecedor não pode ser vazio!')
            return
        nomefabr_old = window.nomefabr_old
        FabricantesRepo.my_update(self, nomefabr_old=nomefabr_old, nomefabr=nomefabr)
        window.carrega_dados("FABRICANTES", window.tw_fornec)
        window.carrega_dados("ESTOQUE", window.tw_prod)
        window.show_mensagem('>> Fornecedor alterado com sucesso!')
        self.close_jan_altforn()

    def close_jan_altforn(self):
        window.pb_alterar.setEnabled(True)
        self.close()


class Jan_Add_Prod(QWidget, Ui_wind_add_prod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

        self.pb_confirma_prod.clicked.connect(self.confirma_prod)
        self.pb_cancela_prod.clicked.connect(window.show_mensagem(''))
        self.pb_cancela_prod.clicked.connect(self.close_janprod)

        self.le_codint.returnPressed.connect(self.le_codforn.setFocus)
        self.le_codforn.returnPressed.connect(self.le_descprod.setFocus)
        self.le_descprod.returnPressed.connect(self.le_codint.setFocus)

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
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, on=False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, on=False)

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
        self.tw_entradas.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tw_saidas.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tabWidget.setCurrentIndex(0)

        self.estilos()

        self.slots()

        self.carrega_dados("ESTOQUE", self.tw_prod)

        self.carrega_dados("FABRICANTES", self.tw_fornec)

        self.carrega_dados("ENTRADAS", self.tw_entradas)

        self.carrega_dados("SAIDAS", self.tw_saidas)

        self.carrega_dados("COMPRAS", self.tw_compras)

# !=================== FUNÇÕES ============================

    def carrega_dados(self, tabela, tab_widget, ordem=None):
        if tabela == "ESTOQUE":
            self.pixmapi = getattr(QStyle, "SP_MessageBoxWarning")
            self.pontocompra = ComprasRepo.my_select(self)
            for i, reg in enumerate(self.pontocompra):
                if reg[2] < reg[3]:
                    EstoqueRepo.my_updpc(self, codfabr=reg[0], pc=1)
                if reg[2] >= reg[3]:
                    EstoqueRepo.my_updpc(self, codfabr=reg[0], pc=0)
            if ordem is None:
                self.registros = EstoqueRepo.my_select(self)
            else:
                self.registros = ordem
            self.colunas = ['Cód. Interno', 'Cód. Fabricante',
                            'Descrição do Produto', 'Fabricante', 'Saldo', 'PC']
            for i, reg in enumerate(self.registros):
                if reg[5] is None:
                    self.icon = None
                    self.model = TableModel(self.registros, columns=self.colunas,
                                            icon=self.icon)
                else:
                    self.icon = self.style().standardIcon(self.pixmapi)
                    self.model = TableModel(self.registros, columns=self.colunas,
                                            icon=self.icon)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 150)
            tab_widget.setColumnWidth(1, 400)
            tab_widget.setColumnWidth(2, 600)
            tab_widget.setColumnWidth(3, 200)
            tab_widget.setColumnWidth(4, 150)
            tab_widget.setColumnWidth(5, 30)
            self.model.layoutChanged.emit()
        elif tabela == "FABRICANTES":
            if ordem is None:
                self.registros = FabricantesRepo.my_select(self)
            else:
                self.registros = ordem
            self.colunas = ['Fabricante ID', 'Nome do Fabricante']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 150)
            tab_widget.setColumnWidth(1, 500)
        elif tabela == "ENTRADAS":
            self.registros = EntradasRepo.my_select(self)
            self.colunas = ['Data Entrada', 'Quantidade', 'Código do Fabricante',
                            'Descrição do Produto']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 170)
            tab_widget.setColumnWidth(1, 150)
            tab_widget.setColumnWidth(2, 400)
            tab_widget.setColumnWidth(3, 550)
        elif tabela == "SAIDAS":
            self.registros = SaidasRepo.my_select(self)
            self.colunas = ['Data de Saída', 'Quantidade', 'Código do Fabricante',
                            'Descrição do Produto', 'Destino do Produto']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 150)
            tab_widget.setColumnWidth(1, 150)
            tab_widget.setColumnWidth(2, 350)
            tab_widget.setColumnWidth(3, 600)
            tab_widget.setColumnWidth(4, 150)
        elif tabela == "COMPRAS":
            self.registros = ComprasRepo.my_select(self)
            self.colunas = ['Código do Fabricante', 'Descrição do Produto',
                            'Saldo', 'Limite Mínimo']
            self.model = TableModel(self.registros, columns=self.colunas)
            tab_widget.setModel(self.model)
            tab_widget.setColumnWidth(0, 350)
            tab_widget.setColumnWidth(1, 600)
            tab_widget.setColumnWidth(2, 150)
            tab_widget.setColumnWidth(3, 150)

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
            msg, sim, nao = self.msg_Box("Exclusão de Produtos",
                                         "Confirma exclusão do Produto?")
            if msg.clickedButton() == nao:
                return
            if msg.clickedButton() == sim:
                pass
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
            msg, sim, nao = self.msg_Box("Exclusão de Fabricante",
                                         "Confirma exclusão do fabricante?")
            if msg.clickedButton() == nao:
                return
            if msg.clickedButton() == sim:
                pass
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
                    '>> Favor selecionar um item para alteração!')
                return
            self.codint_old = codint[0].data()
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
            nomefabr = self.tw_fornec.selectionModel().selectedRows(column=1)
            if len(nomefabr) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para alteração!')
                return
            self.nomefabr_old = nomefabr[0].data()
            self.jan_alt_forn = Jan_Alt_Forn()
            self.jan_alt_forn.le_nomeforn.setText(self.nomefabr_old)
            self.pb_alterar.setEnabled(False)
            self.jan_alt_forn.show()

    def entrada(self):
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! ENTRADA DE PRODUTOS
            codint = self.tw_prod.selectionModel().selectedRows(column=0)
            codfabr = self.tw_prod.selectionModel().selectedRows(column=1)
            descprod = self.tw_prod.selectionModel().selectedRows(column=2)
            saldo = self.tw_prod.selectionModel().selectedRows(column=4)
            if len(codint) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para efetuar a entrada!')
                return
            self.janEntrProd = Jan_Entr_Prod()
            self.janEntrProd.cp_codint.setText(codint[0].data())
            self.janEntrProd.cp_codfabr.setText(codfabr[0].data())
            self.janEntrProd.cp_descprod.setText(descprod[0].data())
            self.janEntrProd.cp_saldo.setText(saldo[0].data())
            self.pb_entrada.setEnabled(False)
            self.janEntrProd.show()

    def saida(self):
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! SAÍDA DE PRODUTOS
            codint = self.tw_prod.selectionModel().selectedRows(column=0)
            codfabr = self.tw_prod.selectionModel().selectedRows(column=1)
            descprod = self.tw_prod.selectionModel().selectedRows(column=2)
            saldo = self.tw_prod.selectionModel().selectedRows(column=4)
            if len(codint) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para efetuar a saída!')
                return
            self.janSaidaProd = Jan_Saida_Prod()
            self.janSaidaProd.cp_codint.setText(codint[0].data())
            self.janSaidaProd.cp_codfabr.setText(codfabr[0].data())
            self.janSaidaProd.cp_descprod.setText(descprod[0].data())
            self.janSaidaProd.cp_saldo.setText(saldo[0].data())
            self.pb_saida.setEnabled(False)
            self.janSaidaProd.show()

    def compras(self):
        aba = self.tabWidget.currentIndex()
        if aba == 0:        # ! PONTO DE COMPRAS
            codfabr = self.tw_prod.selectionModel().selectedRows(column=1)
            descprod = self.tw_prod.selectionModel().selectedRows(column=2)
            saldo = self.tw_prod.selectionModel().selectedRows(column=4)
            if len(codfabr) <= 0:
                self.show_mensagem(
                    '>> Favor selecionar um item para definir um ponto de compra!')
                return
            idprod = EstoqueRepo.my_select_one(self, **{"COD_FABR": codfabr[0].data()})
            self.lim_min = ComprasRepo.my_select_one(self, **{"PC_IDPROD": idprod.ID_PROD})
            self.janCompraProd = Jan_Compra_Prod()
            self.janCompraProd.cp_codfabr.setText(codfabr[0].data())
            self.janCompraProd.cp_descprod.setText(descprod[0].data())
            self.janCompraProd.cp_saldo.setText(saldo[0].data())
            if self.lim_min is not None:
                self.janCompraProd.cp_lim_min.setText(str(self.lim_min.PC_LIM_MIN))
            else:
                self.janCompraProd.cp_lim_min.setText('0.0')
            self.pb_compra.setEnabled(False)
            self.janCompraProd.show()

    def classificacao(self, b):
        if self.cb_classif.isChecked():
            aba = self.tabWidget.currentIndex()
            txtBotao = b.text()
            if aba == 0:
                if txtBotao == 'Cód. Interno' and b.isChecked() is True:
                    comando = self.selecao()
                elif txtBotao == 'Cód. Fabricante' and b.isChecked() is True:
                    comando = self.selecao()
                elif txtBotao == 'Descr. Produto' and b.isChecked() is True:
                    comando = self.selecao()
                elif txtBotao == 'Fabricante' and b.isChecked() is True:
                    comando = self.selecao()
                elif txtBotao == 'Saldo' and b.isChecked() is True:
                    comando = self.selecao()
                elif txtBotao == "Decrescente":
                    comando = self.selecao()
                elif txtBotao == 'Classificar':
                    comando = self.selecao()
                if comando == "ID_FABR":
                    if self.cb_decresc.isChecked():
                        self.ordem = EstoqueRepo.my_orderby_fabr(self, descendente=True)
                    else:
                        self.ordem = EstoqueRepo.my_orderby_fabr(self)
                else:
                    if self.cb_decresc.isChecked():
                        self.ordem = EstoqueRepo.my_orderby(self, descendente=True, **{"coluna": comando})
                    else:
                        self.ordem = EstoqueRepo.my_orderby(self, **{"coluna": comando})
                self.carrega_dados("ESTOQUE", self.tw_prod, self.ordem)
            if aba == 1:
                if txtBotao == 'Fabricante' and b.isChecked() is True:
                    comando = 'NOMEFABR'
                else:
                    if self.rb_fabr.isChecked() is True:
                        comando = 'NOMEFABR'
                    else:
                        comando = 'ID_FABR'
                if self.cb_decresc.isChecked():
                    self.ordem = FabricantesRepo.my_orderby(self, descendente=True, **{"coluna": comando})
                else:
                    self.ordem = FabricantesRepo.my_orderby(self, **{"coluna": comando})
                self.carrega_dados("FABRICANTES", self.tw_fornec, self.ordem)
        else:
            self.carrega_dados("ESTOQUE", self.tw_prod)
            self.carrega_dados("FABRICANTES", self.tw_fornec)

    def categoria(self, b):
        self.rb = b
        if self.rb.isChecked():
            self.classificacao(self.rb)

    def selecao(self):
        if self.rb_codint.isChecked():
            return 'COD_INT'
        if self.rb_codfabr.isChecked():
            return 'COD_FABR'
        if self.rb_prod.isChecked():
            return 'PRODUTO'
        if self.rb_fabr.isChecked():
            return 'ID_FABR'
        if self.rb_saldo.isChecked():
            return 'SALDO'
# !================= FUNÇÕES AUXILIARES ===================

    def reindex(self):
        return
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
            self.carrega_dados("ENTRADAS", self.tw_entradas)

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
        self.pb_saidas.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_saidas.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.Saidas))
        self.pb_saidas.clicked.connect(lambda: self.pagina('SAÍDAS'))
        self.pb_compras.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_compras.clicked.connect(lambda: self.sw_paginas.setCurrentWidget(self.PontoCompra))
        self.pb_compras.clicked.connect(lambda: self.pagina('PONTO DE COMPRAS'))

        self.pb_adicionar.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_adicionar.clicked.connect(lambda: self.adicionar())
        self.pb_excluir.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_excluir.clicked.connect(lambda: self.excluir())
        self.pb_alterar.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_alterar.clicked.connect(lambda: self.alterar())
        self.pb_entrada.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_entrada.clicked.connect(lambda: self.entrada())
        self.pb_saida.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_saida.clicked.connect(lambda: self.saida())
        self.pb_compra.clicked.connect(lambda: self.show_mensagem(''))
        self.pb_compra.clicked.connect(lambda: self.compras())

        self.cb_classif.stateChanged.connect(lambda: self.classificacao(self.cb_classif))
        self.cb_decresc.stateChanged.connect(lambda: self.classificacao(self.cb_decresc))
        self.rb_codint.toggled.connect(lambda: self.categoria(self.rb_codint))
        self.rb_codfabr.toggled.connect(lambda: self.categoria(self.rb_codfabr))
        self.rb_prod.toggled.connect(lambda: self.categoria(self.rb_prod))
        self.rb_fabr.toggled.connect(lambda: self.categoria(self.rb_fabr))
        self.rb_saldo.toggled.connect(lambda: self.categoria(self.rb_saldo))

        self.tabWidget.currentChanged.connect(lambda x: self.disablebuttons(x))

    def disablebuttons(self, index):
        if index == 1:
            self.pb_entrada.setHidden(True)
            self.pb_saida.setHidden(True)
            self.pb_compra.setHidden(True)
        else:
            self.pb_entrada.setHidden(False)
            self.pb_saida.setHidden(False)
            self.pb_compra.setHidden(False)

    def show_mensagem(self, m):
        self.lb_mensagens.setText(m)

    def msg_Box(self, titulo, mensagem):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        sim = msg.addButton("Sim", QMessageBox.AcceptRole)
        nao = msg.addButton("Não", QMessageBox.RejectRole)
        msg.setText(mensagem)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()
        return msg, sim, nao

# !================== PROGRAMA PRINCIPAL ======================


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
