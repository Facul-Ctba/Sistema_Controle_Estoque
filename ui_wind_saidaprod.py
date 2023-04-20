# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_saidaprod.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_wind_saida_prod(object):
    def setupUi(self, wind_saida_prod):
        if not wind_saida_prod.objectName():
            wind_saida_prod.setObjectName(u"wind_saida_prod")
        wind_saida_prod.resize(827, 393)
        wind_saida_prod.setMinimumSize(QSize(827, 0))
        wind_saida_prod.setMaximumSize(QSize(827, 500))
        self.verticalLayout = QVBoxLayout(wind_saida_prod)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_top = QFrame(wind_saida_prod)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 200))
        self.fr_top.setMaximumSize(QSize(16777215, 200))
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_top)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.lb_codint = QLabel(self.fr_top)
        self.lb_codint.setObjectName(u"lb_codint")
        self.lb_codint.setMinimumSize(QSize(0, 30))
        self.lb_codint.setMaximumSize(QSize(16777215, 30))
        self.lb_codint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_codint)

        self.lb_codforn = QLabel(self.fr_top)
        self.lb_codforn.setObjectName(u"lb_codforn")
        self.lb_codforn.setMinimumSize(QSize(0, 30))
        self.lb_codforn.setMaximumSize(QSize(16777215, 30))
        self.lb_codforn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_codforn)

        self.lb_descprod = QLabel(self.fr_top)
        self.lb_descprod.setObjectName(u"lb_descprod")
        self.lb_descprod.setMinimumSize(QSize(0, 30))
        self.lb_descprod.setMaximumSize(QSize(16777215, 30))
        self.lb_descprod.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_descprod)

        self.lb_forn = QLabel(self.fr_top)
        self.lb_forn.setObjectName(u"lb_forn")
        self.lb_forn.setMinimumSize(QSize(0, 30))
        self.lb_forn.setMaximumSize(QSize(16777215, 30))
        self.lb_forn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_forn)

        self.cp_codint = QLabel(self.fr_top)
        self.cp_codint.setObjectName(u"cp_codint")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cp_codint)

        self.cp_codfabr = QLabel(self.fr_top)
        self.cp_codfabr.setObjectName(u"cp_codfabr")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cp_codfabr)

        self.cp_descprod = QLabel(self.fr_top)
        self.cp_descprod.setObjectName(u"cp_descprod")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cp_descprod)

        self.cp_saldo = QLabel(self.fr_top)
        self.cp_saldo.setObjectName(u"cp_saldo")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cp_saldo)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.fr_top, 0, Qt.AlignVCenter)

        self.frame = QFrame(wind_saida_prod)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lb_data = QLabel(self.frame)
        self.lb_data.setObjectName(u"lb_data")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_data)

        self.le_data = QLineEdit(self.frame)
        self.le_data.setObjectName(u"le_data")
        self.le_data.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.le_data)

        self.lb_quant = QLabel(self.frame)
        self.lb_quant.setObjectName(u"lb_quant")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_quant)

        self.lb_destino = QLabel(self.frame)
        self.lb_destino.setObjectName(u"lb_destino")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_destino)

        self.le_quant = QLineEdit(self.frame)
        self.le_quant.setObjectName(u"le_quant")
        self.le_quant.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.le_quant)

        self.le_destino = QLineEdit(self.frame)
        self.le_destino.setObjectName(u"le_destino")
        self.le_destino.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.le_destino)


        self.verticalLayout.addWidget(self.frame)

        self.fr_bot = QFrame(wind_saida_prod)
        self.fr_bot.setObjectName(u"fr_bot")
        self.fr_bot.setFrameShape(QFrame.StyledPanel)
        self.fr_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_confirma_entr = QPushButton(self.fr_bot)
        self.pb_confirma_entr.setObjectName(u"pb_confirma_entr")
        self.pb_confirma_entr.setMinimumSize(QSize(200, 30))
        self.pb_confirma_entr.setMaximumSize(QSize(200, 30))
        self.pb_confirma_entr.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_confirma_entr.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_confirma_entr)

        self.pb_cancela_entr = QPushButton(self.fr_bot)
        self.pb_cancela_entr.setObjectName(u"pb_cancela_entr")
        self.pb_cancela_entr.setMinimumSize(QSize(200, 30))
        self.pb_cancela_entr.setMaximumSize(QSize(200, 30))
        self.pb_cancela_entr.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cancela_entr.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_cancela_entr)


        self.verticalLayout.addWidget(self.fr_bot, 0, Qt.AlignTop)


        self.retranslateUi(wind_saida_prod)

        QMetaObject.connectSlotsByName(wind_saida_prod)
    # setupUi

    def retranslateUi(self, wind_saida_prod):
        wind_saida_prod.setWindowTitle(QCoreApplication.translate("wind_saida_prod", u"Sa\u00edda de Produtos do Estoque", None))
        self.lb_codint.setText(QCoreApplication.translate("wind_saida_prod", u"<html><head/><body><p align=\"right\">C\u00f3digo Interno</p></body></html>", None))
        self.lb_codforn.setText(QCoreApplication.translate("wind_saida_prod", u"<html><head/><body><p align=\"right\">C\u00f3digo Fabricante</p></body></html>", None))
        self.lb_descprod.setText(QCoreApplication.translate("wind_saida_prod", u"<html><head/><body><p align=\"right\">Descri\u00e7\u00e3o do Produto</p></body></html>", None))
        self.lb_forn.setText(QCoreApplication.translate("wind_saida_prod", u"<html><head/><body><p align=\"right\">Saldo</p></body></html>", None))
        self.cp_codint.setText(QCoreApplication.translate("wind_saida_prod", u"TextLabel", None))
        self.cp_codfabr.setText(QCoreApplication.translate("wind_saida_prod", u"TextLabel", None))
        self.cp_descprod.setText(QCoreApplication.translate("wind_saida_prod", u"TextLabel", None))
        self.cp_saldo.setText(QCoreApplication.translate("wind_saida_prod", u"TextLabel", None))
        self.lb_data.setText(QCoreApplication.translate("wind_saida_prod", u"Data", None))
        self.le_data.setPlaceholderText(QCoreApplication.translate("wind_saida_prod", u"dd/mm/aaaa", None))
        self.lb_quant.setText(QCoreApplication.translate("wind_saida_prod", u"Quantidade", None))
        self.lb_destino.setText(QCoreApplication.translate("wind_saida_prod", u"Destino", None))
        self.le_quant.setPlaceholderText(QCoreApplication.translate("wind_saida_prod", u"0,0", None))
        self.pb_confirma_entr.setText(QCoreApplication.translate("wind_saida_prod", u"Confirmar", None))
        self.pb_cancela_entr.setText(QCoreApplication.translate("wind_saida_prod", u"Cancelar", None))
    # retranslateUi

