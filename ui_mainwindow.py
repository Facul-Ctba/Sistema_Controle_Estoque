# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 671)
        self.actionSelect = QAction(MainWindow)
        self.actionSelect.setObjectName(u"actionSelect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: 10pt \"Arial\";")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_esquerda = QFrame(self.centralwidget)
        self.fr_esquerda.setObjectName(u"fr_esquerda")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_esquerda.sizePolicy().hasHeightForWidth())
        self.fr_esquerda.setSizePolicy(sizePolicy)
        self.fr_esquerda.setMinimumSize(QSize(0, 0))
        self.fr_esquerda.setMaximumSize(QSize(9, 16777215))
        self.fr_esquerda.setFrameShape(QFrame.StyledPanel)
        self.fr_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_esquerda)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.fr_funcoes = QFrame(self.fr_esquerda)
        self.fr_funcoes.setObjectName(u"fr_funcoes")
        self.fr_funcoes.setFrameShape(QFrame.StyledPanel)
        self.fr_funcoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fr_funcoes)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pb_cadastros = QPushButton(self.fr_funcoes)
        self.pb_cadastros.setObjectName(u"pb_cadastros")
        self.pb_cadastros.setMinimumSize(QSize(0, 48))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pb_cadastros.setFont(font)
        self.pb_cadastros.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cadastros.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 20px\n"
"}")
        icon = QIcon()
        icon.addFile(u"Icons/icons8-folder-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_cadastros.setIcon(icon)
        self.pb_cadastros.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pb_cadastros)

        self.pb_entradas = QPushButton(self.fr_funcoes)
        self.pb_entradas.setObjectName(u"pb_entradas")
        self.pb_entradas.setMinimumSize(QSize(0, 48))
        self.pb_entradas.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entradas.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 20px\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Icons/icons8-new-window-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_entradas.setIcon(icon1)
        self.pb_entradas.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pb_entradas)

        self.pb_saidas = QPushButton(self.fr_funcoes)
        self.pb_saidas.setObjectName(u"pb_saidas")
        self.pb_saidas.setMinimumSize(QSize(0, 48))
        self.pb_saidas.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_saidas.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 20px\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Icons/icons8-open-view-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_saidas.setIcon(icon2)
        self.pb_saidas.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pb_saidas)

        self.pb_compra = QPushButton(self.fr_funcoes)
        self.pb_compra.setObjectName(u"pb_compra")
        self.pb_compra.setMinimumSize(QSize(0, 48))
        self.pb_compra.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_compra.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 20px\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"Icons/icons8-choose-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_compra.setIcon(icon3)
        self.pb_compra.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pb_compra)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.fr_funcoes)


        self.horizontalLayout.addWidget(self.fr_esquerda)

        self.fr_direita = QFrame(self.centralwidget)
        self.fr_direita.setObjectName(u"fr_direita")
        self.fr_direita.setFrameShape(QFrame.StyledPanel)
        self.fr_direita.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_direita)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 5, 5)
        self.fr_top = QFrame(self.fr_direita)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 48))
        self.fr_top.setMaximumSize(QSize(16777215, 48))
        self.fr_top.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_menu = QPushButton(self.fr_top)
        self.pb_menu.setObjectName(u"pb_menu")
        self.pb_menu.setMinimumSize(QSize(45, 45))
        self.pb_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_menu.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255,255,0);\n"
"	color: rgb(0, 0, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Icons/icons8-view-headline-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_menu.setIcon(icon4)
        self.pb_menu.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.pb_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.fr_top)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.cb_temas = QComboBox(self.fr_top)
        self.cb_temas.setObjectName(u"cb_temas")
        self.cb_temas.setMinimumSize(QSize(200, 40))
        self.cb_temas.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_temas.setStyleSheet(u"QComboBox:{\n"
"	font: 700 10pt \"Arial\";\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgb(187, 255, 193);\n"
"	selection-color: rgb(255, 0, 0);\n"
"	alternate-background-color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.cb_temas)


        self.verticalLayout_2.addWidget(self.fr_top)

        self.fr_main = QFrame(self.fr_direita)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_main)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fr_cabecalho = QFrame(self.fr_main)
        self.fr_cabecalho.setObjectName(u"fr_cabecalho")
        self.fr_cabecalho.setMinimumSize(QSize(0, 150))
        self.fr_cabecalho.setMaximumSize(QSize(16777215, 150))
        self.fr_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.fr_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_cabecalho)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_logo = QLabel(self.fr_cabecalho)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(212, 133))
        self.lb_logo.setMaximumSize(QSize(212, 133))

        self.horizontalLayout_4.addWidget(self.lb_logo)

        self.lb_titulo = QLabel(self.fr_cabecalho)
        self.lb_titulo.setObjectName(u"lb_titulo")

        self.horizontalLayout_4.addWidget(self.lb_titulo)


        self.verticalLayout_3.addWidget(self.fr_cabecalho)

        self.fr_paginas = QFrame(self.fr_main)
        self.fr_paginas.setObjectName(u"fr_paginas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_paginas.sizePolicy().hasHeightForWidth())
        self.fr_paginas.setSizePolicy(sizePolicy1)
        self.fr_paginas.setFrameShape(QFrame.StyledPanel)
        self.fr_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sw_paginas = QStackedWidget(self.fr_paginas)
        self.sw_paginas.setObjectName(u"sw_paginas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sw_paginas.sizePolicy().hasHeightForWidth())
        self.sw_paginas.setSizePolicy(sizePolicy2)
        self.Cadastros = QWidget()
        self.Cadastros.setObjectName(u"Cadastros")
        self.verticalLayout_5 = QVBoxLayout(self.Cadastros)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.fr_comm_ctrl = QFrame(self.Cadastros)
        self.fr_comm_ctrl.setObjectName(u"fr_comm_ctrl")
        self.fr_comm_ctrl.setMinimumSize(QSize(0, 35))
        self.fr_comm_ctrl.setMaximumSize(QSize(16777215, 35))
        self.fr_comm_ctrl.setFrameShape(QFrame.StyledPanel)
        self.fr_comm_ctrl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_comm_ctrl)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 3)
        self.pb_adicionar = QPushButton(self.fr_comm_ctrl)
        self.pb_adicionar.setObjectName(u"pb_adicionar")
        self.pb_adicionar.setMinimumSize(QSize(150, 30))
        self.pb_adicionar.setMaximumSize(QSize(16777215, 30))
        self.pb_adicionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_adicionar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_adicionar)

        self.pb_excluir = QPushButton(self.fr_comm_ctrl)
        self.pb_excluir.setObjectName(u"pb_excluir")
        self.pb_excluir.setMinimumSize(QSize(150, 30))
        self.pb_excluir.setMaximumSize(QSize(16777215, 30))
        self.pb_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_excluir)

        self.pb_alterar = QPushButton(self.fr_comm_ctrl)
        self.pb_alterar.setObjectName(u"pb_alterar")
        self.pb_alterar.setMinimumSize(QSize(150, 30))
        self.pb_alterar.setMaximumSize(QSize(16777215, 30))
        self.pb_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_alterar)

        self.pb_reindex = QPushButton(self.fr_comm_ctrl)
        self.pb_reindex.setObjectName(u"pb_reindex")
        self.pb_reindex.setMinimumSize(QSize(150, 30))
        self.pb_reindex.setMaximumSize(QSize(16777215, 30))
        self.pb_reindex.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_reindex.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 20px\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_reindex)

        self.rb_filtro = QRadioButton(self.fr_comm_ctrl)
        self.rb_filtro.setObjectName(u"rb_filtro")
        self.rb_filtro.setCursor(QCursor(Qt.PointingHandCursor))
        self.rb_filtro.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_5.addWidget(self.rb_filtro)

        self.horizontalSpacer_2 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.fr_comm_ctrl)

        self.tabWidget = QTabWidget(self.Cadastros)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet(u"")
        self.tab_prod = QWidget()
        self.tab_prod.setObjectName(u"tab_prod")
        self.tab_prod.setStyleSheet(u"background-color: rgb(86, 101, 115);")
        self.verticalLayout_7 = QVBoxLayout(self.tab_prod)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tw_prod = QTableWidget(self.tab_prod)
        if (self.tw_prod.columnCount() < 6):
            self.tw_prod.setColumnCount(6)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tw_prod.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_prod.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_prod.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_prod.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_prod.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_prod.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tw_prod.setObjectName(u"tw_prod")
        self.tw_prod.setEnabled(True)
        self.tw_prod.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tw_prod.setFrameShape(QFrame.WinPanel)
        self.tw_prod.setFrameShadow(QFrame.Sunken)
        self.tw_prod.setLineWidth(2)
        self.tw_prod.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_prod.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_prod.setAlternatingRowColors(True)
        self.tw_prod.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_prod.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_prod.setSortingEnabled(False)
        self.tw_prod.setWordWrap(False)
        self.tw_prod.horizontalHeader().setStretchLastSection(True)
        self.tw_prod.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.tw_prod)

        self.tabWidget.addTab(self.tab_prod, "")
        self.tab_forn = QWidget()
        self.tab_forn.setObjectName(u"tab_forn")
        self.tab_forn.setStyleSheet(u"background-color: rgb(86, 101, 115);")
        self.verticalLayout_6 = QVBoxLayout(self.tab_forn)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tw_fornec = QTableWidget(self.tab_forn)
        if (self.tw_fornec.columnCount() < 2):
            self.tw_fornec.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tw_fornec.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tw_fornec.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.tw_fornec.setObjectName(u"tw_fornec")
        self.tw_fornec.setFrameShape(QFrame.WinPanel)
        self.tw_fornec.setLineWidth(2)
        self.tw_fornec.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_fornec.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_fornec.setAlternatingRowColors(True)
        self.tw_fornec.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_fornec.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_fornec.setSortingEnabled(False)
        self.tw_fornec.setWordWrap(False)
        self.tw_fornec.horizontalHeader().setStretchLastSection(True)
        self.tw_fornec.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.tw_fornec)

        self.tabWidget.addTab(self.tab_forn, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.sw_paginas.addWidget(self.Cadastros)
        self.Entadas = QWidget()
        self.Entadas.setObjectName(u"Entadas")
        self.verticalLayout_10 = QVBoxLayout(self.Entadas)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.Entadas)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_10.addWidget(self.label_4)

        self.sw_paginas.addWidget(self.Entadas)
        self.Saidas = QWidget()
        self.Saidas.setObjectName(u"Saidas")
        self.verticalLayout_11 = QVBoxLayout(self.Saidas)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.Saidas)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)

        self.sw_paginas.addWidget(self.Saidas)
        self.PontoCompra = QWidget()
        self.PontoCompra.setObjectName(u"PontoCompra")
        self.verticalLayout_12 = QVBoxLayout(self.PontoCompra)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.PontoCompra)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.sw_paginas.addWidget(self.PontoCompra)

        self.verticalLayout_4.addWidget(self.sw_paginas)


        self.verticalLayout_3.addWidget(self.fr_paginas)


        self.verticalLayout_2.addWidget(self.fr_main)

        self.fr_bottom = QFrame(self.fr_direita)
        self.fr_bottom.setObjectName(u"fr_bottom")
        self.fr_bottom.setMinimumSize(QSize(0, 30))
        self.fr_bottom.setMaximumSize(QSize(16777215, 30))
        self.fr_bottom.setFrameShape(QFrame.StyledPanel)
        self.fr_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_bottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.lb_mensagens = QLabel(self.fr_bottom)
        self.lb_mensagens.setObjectName(u"lb_mensagens")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_mensagens.sizePolicy().hasHeightForWidth())
        self.lb_mensagens.setSizePolicy(sizePolicy3)
        self.lb_mensagens.setMinimumSize(QSize(750, 30))
        self.lb_mensagens.setMaximumSize(QSize(16777215, 30))
        self.lb_mensagens.setFont(font)

        self.horizontalLayout_3.addWidget(self.lb_mensagens, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.fr_bottom)


        self.horizontalLayout.addWidget(self.fr_direita)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sw_paginas.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSelect.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pb_cadastros.setText(QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.pb_entradas.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.pb_saidas.setText(QCoreApplication.translate("MainWindow", u"Sa\u00eddas", None))
        self.pb_compra.setText(QCoreApplication.translate("MainWindow", u"\u00c0 Comprar", None))
        self.pb_menu.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.label.setText("")
        self.lb_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Icons/Icons/Avitech_m.png\"/></p></body></html>", None))
        self.lb_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Sistema de Controle de Estoque</span></p></body></html>", None))
        self.pb_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pb_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pb_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pb_reindex.setText(QCoreApplication.translate("MainWindow", u"Re-indexar ID", None))
        self.rb_filtro.setText(QCoreApplication.translate("MainWindow", u"Ativar Filtro", None))
        ___qtablewidgetitem = self.tw_prod.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tw_prod.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Interno", None));
        ___qtablewidgetitem2 = self.tw_prod.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Fabricante", None));
        ___qtablewidgetitem3 = self.tw_prod.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o do Produto", None));
        ___qtablewidgetitem4 = self.tw_prod.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem5 = self.tw_prod.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Saldo", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prod), QCoreApplication.translate("MainWindow", u"Produtos", None))
        ___qtablewidgetitem6 = self.tw_fornec.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tw_fornec.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_forn), QCoreApplication.translate("MainWindow", u"Fabricantes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Entradas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sa\u00eddas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ponto de compra", None))
        self.lb_mensagens.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
    # retranslateUi

