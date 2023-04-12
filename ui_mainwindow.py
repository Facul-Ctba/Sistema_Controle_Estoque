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
    QLayout, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1268, 717)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.actionSelect = QAction(MainWindow)
        self.actionSelect.setObjectName(u"actionSelect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.centralwidget.setFont(font1)
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
        self.fr_esquerda.setMaximumSize(QSize(250, 16777215))
        self.fr_esquerda.setFrameShape(QFrame.StyledPanel)
        self.fr_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_esquerda)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_funcoes = QFrame(self.fr_esquerda)
        self.fr_funcoes.setObjectName(u"fr_funcoes")
        self.fr_funcoes.setFrameShape(QFrame.StyledPanel)
        self.fr_funcoes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fr_funcoes)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 0)
        self.pb_cadastros = QPushButton(self.fr_funcoes)
        self.pb_cadastros.setObjectName(u"pb_cadastros")
        self.pb_cadastros.setMinimumSize(QSize(0, 56))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.pb_cadastros.setFont(font2)
        self.pb_cadastros.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cadastros.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 20px\n"
"}")
        icon = QIcon()
        icon.addFile(u"Icons/icons8-folder-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_cadastros.setIcon(icon)
        self.pb_cadastros.setIconSize(QSize(48, 48))

        self.verticalLayout_8.addWidget(self.pb_cadastros)

        self.pb_entradas = QPushButton(self.fr_funcoes)
        self.pb_entradas.setObjectName(u"pb_entradas")
        self.pb_entradas.setMinimumSize(QSize(0, 56))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.pb_entradas.setFont(font3)
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
        self.pb_saidas.setMinimumSize(QSize(0, 56))
        self.pb_saidas.setFont(font3)
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
        self.pb_compra.setMinimumSize(QSize(0, 56))
        self.pb_compra.setFont(font3)
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
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.fr_top = QFrame(self.fr_direita)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 52))
        self.fr_top.setMaximumSize(QSize(16777215, 48))
        self.fr_top.setFont(font1)
        self.fr_top.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_top)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.pb_menu = QPushButton(self.fr_top)
        self.pb_menu.setObjectName(u"pb_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_menu.sizePolicy().hasHeightForWidth())
        self.pb_menu.setSizePolicy(sizePolicy1)
        self.pb_menu.setMinimumSize(QSize(120, 46))
        self.pb_menu.setMaximumSize(QSize(16777215, 46))
        self.pb_menu.setFont(font1)
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

        self.cb_temas = QComboBox(self.fr_top)
        self.cb_temas.setObjectName(u"cb_temas")
        sizePolicy.setHeightForWidth(self.cb_temas.sizePolicy().hasHeightForWidth())
        self.cb_temas.setSizePolicy(sizePolicy)
        self.cb_temas.setMinimumSize(QSize(200, 0))
        self.cb_temas.setFont(font3)
        self.cb_temas.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_temas.setStyleSheet(u"QComboBox:{\n"
"	font: 12pt \"Arial\";\n"
"	color: rgb(0, 0, 255);\n"
"	background-color: rgb(187, 255, 193);\n"
"	selection-color: rgb(255, 0, 0);\n"
"	alternate-background-color: rgb(255, 0, 0);\n"
"}")
        self.cb_temas.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cb_temas.setMinimumContentsLength(1)
        self.cb_temas.setIconSize(QSize(32, 32))
        self.cb_temas.setFrame(False)

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
        self.lb_logo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_logo.setMargin(3)

        self.horizontalLayout_4.addWidget(self.lb_logo)

        self.frame = QFrame(self.fr_cabecalho)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_titulo = QLabel(self.frame)
        self.lb_titulo.setObjectName(u"lb_titulo")

        self.verticalLayout_9.addWidget(self.lb_titulo)

        self.lb_pagina = QLabel(self.frame)
        self.lb_pagina.setObjectName(u"lb_pagina")
        self.lb_pagina.setMinimumSize(QSize(0, 40))
        self.lb_pagina.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(True)
        self.lb_pagina.setFont(font4)
        self.lb_pagina.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lb_pagina)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.fr_cabecalho)

        self.fr_paginas = QFrame(self.fr_main)
        self.fr_paginas.setObjectName(u"fr_paginas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fr_paginas.sizePolicy().hasHeightForWidth())
        self.fr_paginas.setSizePolicy(sizePolicy2)
        self.fr_paginas.setFrameShape(QFrame.StyledPanel)
        self.fr_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_paginas)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.sw_paginas = QStackedWidget(self.fr_paginas)
        self.sw_paginas.setObjectName(u"sw_paginas")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sw_paginas.sizePolicy().hasHeightForWidth())
        self.sw_paginas.setSizePolicy(sizePolicy3)
        self.Cadastros = QWidget()
        self.Cadastros.setObjectName(u"Cadastros")
        self.verticalLayout_5 = QVBoxLayout(self.Cadastros)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 10, 9, 0)
        self.fr_comm_ctrl = QFrame(self.Cadastros)
        self.fr_comm_ctrl.setObjectName(u"fr_comm_ctrl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fr_comm_ctrl.sizePolicy().hasHeightForWidth())
        self.fr_comm_ctrl.setSizePolicy(sizePolicy4)
        self.fr_comm_ctrl.setMinimumSize(QSize(0, 45))
        self.fr_comm_ctrl.setMaximumSize(QSize(16777215, 16777215))
        self.fr_comm_ctrl.setFrameShape(QFrame.StyledPanel)
        self.fr_comm_ctrl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_comm_ctrl)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pb_adicionar = QPushButton(self.fr_comm_ctrl)
        self.pb_adicionar.setObjectName(u"pb_adicionar")
        self.pb_adicionar.setMinimumSize(QSize(150, 30))
        self.pb_adicionar.setMaximumSize(QSize(16777215, 30))
        self.pb_adicionar.setFont(font1)
        self.pb_adicionar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_adicionar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_adicionar)

        self.pb_excluir = QPushButton(self.fr_comm_ctrl)
        self.pb_excluir.setObjectName(u"pb_excluir")
        self.pb_excluir.setMinimumSize(QSize(150, 30))
        self.pb_excluir.setMaximumSize(QSize(16777215, 30))
        self.pb_excluir.setFont(font1)
        self.pb_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_excluir)

        self.pb_alterar = QPushButton(self.fr_comm_ctrl)
        self.pb_alterar.setObjectName(u"pb_alterar")
        self.pb_alterar.setMinimumSize(QSize(150, 30))
        self.pb_alterar.setMaximumSize(QSize(16777215, 30))
        self.pb_alterar.setFont(font1)
        self.pb_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_alterar)

        self.pb_pesquisar = QPushButton(self.fr_comm_ctrl)
        self.pb_pesquisar.setObjectName(u"pb_pesquisar")
        self.pb_pesquisar.setMinimumSize(QSize(150, 30))
        self.pb_pesquisar.setMaximumSize(QSize(16777215, 30))
        self.pb_pesquisar.setFont(font1)
        self.pb_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_pesquisar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 153, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_pesquisar)

        self.pb_entrada = QPushButton(self.fr_comm_ctrl)
        self.pb_entrada.setObjectName(u"pb_entrada")
        self.pb_entrada.setMinimumSize(QSize(150, 30))
        self.pb_entrada.setMaximumSize(QSize(16777215, 30))
        self.pb_entrada.setFont(font1)
        self.pb_entrada.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entrada.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.pb_entrada)

        self.pb_reindex = QPushButton(self.fr_comm_ctrl)
        self.pb_reindex.setObjectName(u"pb_reindex")
        self.pb_reindex.setMinimumSize(QSize(150, 30))
        self.pb_reindex.setMaximumSize(QSize(16777215, 30))
        self.pb_reindex.setFont(font1)
        self.pb_reindex.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_reindex.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 255);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
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
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_prod = QWidget()
        self.tab_prod.setObjectName(u"tab_prod")
        self.tab_prod.setFont(font1)
        self.tab_prod.setStyleSheet(u"background-color: rgb(86, 101, 115);")
        self.verticalLayout_7 = QVBoxLayout(self.tab_prod)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 9)
        self.tw_prod = QTableWidget(self.tab_prod)
        if (self.tw_prod.columnCount() < 6):
            self.tw_prod.setColumnCount(6)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        font5.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tw_prod.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tw_prod.setObjectName(u"tw_prod")
        self.tw_prod.setEnabled(True)
        self.tw_prod.setFont(font1)
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
        self.tab_forn.setFont(font1)
        self.tab_forn.setStyleSheet(u"background-color: rgb(86, 101, 115);")
        self.verticalLayout_6 = QVBoxLayout(self.tab_forn)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, 9, 0, 9)
        self.tw_fornec = QTableWidget(self.tab_forn)
        if (self.tw_fornec.columnCount() < 2):
            self.tw_fornec.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tw_fornec.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tw_fornec.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.tw_fornec.setObjectName(u"tw_fornec")
        self.tw_fornec.setFont(font1)
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
        self.Entradas = QWidget()
        self.Entradas.setObjectName(u"Entradas")
        self.verticalLayout_10 = QVBoxLayout(self.Entradas)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 10, 9, 0)
        self.fr_entr_cabec = QFrame(self.Entradas)
        self.fr_entr_cabec.setObjectName(u"fr_entr_cabec")
        sizePolicy4.setHeightForWidth(self.fr_entr_cabec.sizePolicy().hasHeightForWidth())
        self.fr_entr_cabec.setSizePolicy(sizePolicy4)
        self.fr_entr_cabec.setMinimumSize(QSize(0, 45))
        self.fr_entr_cabec.setMaximumSize(QSize(16777215, 16777215))
        self.fr_entr_cabec.setFrameShape(QFrame.StyledPanel)
        self.fr_entr_cabec.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fr_entr_cabec)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 5, 10, 10)
        self.pb_entr_add = QPushButton(self.fr_entr_cabec)
        self.pb_entr_add.setObjectName(u"pb_entr_add")
        self.pb_entr_add.setMinimumSize(QSize(150, 30))
        self.pb_entr_add.setMaximumSize(QSize(16777215, 30))
        self.pb_entr_add.setFont(font1)
        self.pb_entr_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entr_add.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pb_entr_add)

        self.pb_entr_excl = QPushButton(self.fr_entr_cabec)
        self.pb_entr_excl.setObjectName(u"pb_entr_excl")
        self.pb_entr_excl.setMinimumSize(QSize(150, 30))
        self.pb_entr_excl.setMaximumSize(QSize(16777215, 30))
        self.pb_entr_excl.setFont(font1)
        self.pb_entr_excl.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entr_excl.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pb_entr_excl)

        self.pb_entr_alt = QPushButton(self.fr_entr_cabec)
        self.pb_entr_alt.setObjectName(u"pb_entr_alt")
        self.pb_entr_alt.setMinimumSize(QSize(150, 30))
        self.pb_entr_alt.setMaximumSize(QSize(16777215, 30))
        self.pb_entr_alt.setFont(font1)
        self.pb_entr_alt.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entr_alt.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pb_entr_alt)

        self.pb_entr_pesq = QPushButton(self.fr_entr_cabec)
        self.pb_entr_pesq.setObjectName(u"pb_entr_pesq")
        self.pb_entr_pesq.setMinimumSize(QSize(150, 30))
        self.pb_entr_pesq.setMaximumSize(QSize(16777215, 30))
        self.pb_entr_pesq.setFont(font1)
        self.pb_entr_pesq.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_entr_pesq.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 153, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pb_entr_pesq)

        self.rb_entr_filtro = QRadioButton(self.fr_entr_cabec)
        self.rb_entr_filtro.setObjectName(u"rb_entr_filtro")
        self.rb_entr_filtro.setCursor(QCursor(Qt.PointingHandCursor))
        self.rb_entr_filtro.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_6.addWidget(self.rb_entr_filtro)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addWidget(self.fr_entr_cabec)

        self.tw_entradas = QTableWidget(self.Entradas)
        if (self.tw_entradas.columnCount() < 5):
            self.tw_entradas.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.tw_entradas.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.tw_entradas.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tw_entradas.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.tw_entradas.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tw_entradas.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.tw_entradas.setObjectName(u"tw_entradas")
        self.tw_entradas.setFont(font1)
        self.tw_entradas.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tw_entradas.setStyleSheet(u"background-color: rgb(86, 101, 115);")
        self.tw_entradas.setFrameShape(QFrame.WinPanel)
        self.tw_entradas.setLineWidth(2)
        self.tw_entradas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tw_entradas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_entradas.setAlternatingRowColors(True)
        self.tw_entradas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_entradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tw_entradas.setWordWrap(False)
        self.tw_entradas.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.tw_entradas)

        self.sw_paginas.addWidget(self.Entradas)
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
        self.fr_bottom.setMinimumSize(QSize(0, 40))
        self.fr_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.fr_bottom.setFrameShape(QFrame.StyledPanel)
        self.fr_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_bottom)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 9, 0)
        self.lb_mensagens = QLabel(self.fr_bottom)
        self.lb_mensagens.setObjectName(u"lb_mensagens")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_mensagens.sizePolicy().hasHeightForWidth())
        self.lb_mensagens.setSizePolicy(sizePolicy5)
        self.lb_mensagens.setMinimumSize(QSize(750, 40))
        self.lb_mensagens.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setItalic(False)
        self.lb_mensagens.setFont(font6)
        self.lb_mensagens.setMargin(10)

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
        self.lb_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Icons/Icons/Avitech_m.png\"/></p></body></html>", None))
        self.lb_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">Sistema de Controle de Estoque</span></p></body></html>", None))
        self.lb_pagina.setText(QCoreApplication.translate("MainWindow", u"CADASTROS", None))
        self.pb_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pb_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pb_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pb_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.pb_entrada.setText(QCoreApplication.translate("MainWindow", u"Entrada", None))
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
        self.pb_entr_add.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.pb_entr_excl.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.pb_entr_alt.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pb_entr_pesq.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.rb_entr_filtro.setText(QCoreApplication.translate("MainWindow", u"Ativar Filtro", None))
        ___qtablewidgetitem8 = self.tw_entradas.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem9 = self.tw_entradas.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem10 = self.tw_entradas.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Interno", None));
        ___qtablewidgetitem11 = self.tw_entradas.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"C\u00f3d. Fabricante", None));
        ___qtablewidgetitem12 = self.tw_entradas.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sa\u00eddas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ponto de compra", None))
        self.lb_mensagens.setText(QCoreApplication.translate("MainWindow", u"Mensagens", None))
    # retranslateUi

