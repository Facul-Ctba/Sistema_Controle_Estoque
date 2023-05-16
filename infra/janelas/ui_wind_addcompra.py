# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_addcompra.ui'
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

class Ui_wind_add_compra(object):
    def setupUi(self, wind_add_compra):
        if not wind_add_compra.objectName():
            wind_add_compra.setObjectName(u"wind_add_compra")
        wind_add_compra.resize(827, 350)
        wind_add_compra.setMinimumSize(QSize(827, 0))
        wind_add_compra.setMaximumSize(QSize(827, 400))
        self.verticalLayout = QVBoxLayout(wind_add_compra)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_top = QFrame(wind_add_compra)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 170))
        self.fr_top.setMaximumSize(QSize(16777215, 170))
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_top)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(15)
        self.formLayout_2.setContentsMargins(10, -1, 10, 6)
        self.lb_codforn = QLabel(self.fr_top)
        self.lb_codforn.setObjectName(u"lb_codforn")
        self.lb_codforn.setMinimumSize(QSize(0, 30))
        self.lb_codforn.setMaximumSize(QSize(16777215, 30))
        self.lb_codforn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lb_codforn)

        self.cp_codfabr = QLabel(self.fr_top)
        self.cp_codfabr.setObjectName(u"cp_codfabr")
        self.cp_codfabr.setMinimumSize(QSize(0, 30))
        self.cp_codfabr.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cp_codfabr)

        self.lb_descprod = QLabel(self.fr_top)
        self.lb_descprod.setObjectName(u"lb_descprod")
        self.lb_descprod.setMinimumSize(QSize(0, 30))
        self.lb_descprod.setMaximumSize(QSize(16777215, 30))
        self.lb_descprod.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lb_descprod)

        self.cp_descprod = QLabel(self.fr_top)
        self.cp_descprod.setObjectName(u"cp_descprod")
        self.cp_descprod.setMinimumSize(QSize(0, 30))
        self.cp_descprod.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cp_descprod)

        self.lb_saldo = QLabel(self.fr_top)
        self.lb_saldo.setObjectName(u"lb_saldo")
        self.lb_saldo.setMinimumSize(QSize(0, 30))
        self.lb_saldo.setMaximumSize(QSize(16777215, 30))
        self.lb_saldo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lb_saldo)

        self.cp_saldo = QLabel(self.fr_top)
        self.cp_saldo.setObjectName(u"cp_saldo")
        self.cp_saldo.setMinimumSize(QSize(0, 30))
        self.cp_saldo.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.cp_saldo)

        self.lb_pontocompra = QLabel(self.fr_top)
        self.lb_pontocompra.setObjectName(u"lb_pontocompra")
        self.lb_pontocompra.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lb_pontocompra)

        self.cp_lim_min = QLabel(self.fr_top)
        self.cp_lim_min.setObjectName(u"cp_lim_min")
        self.cp_lim_min.setMinimumSize(QSize(0, 30))
        self.cp_lim_min.setMaximumSize(QSize(16777215, 30))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cp_lim_min)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.verticalLayout.addWidget(self.fr_top)

        self.frame = QFrame(wind_add_compra)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.lb_compra_quant = QLabel(self.frame)
        self.lb_compra_quant.setObjectName(u"lb_compra_quant")
        self.lb_compra_quant.setMinimumSize(QSize(0, 30))
        self.lb_compra_quant.setMaximumSize(QSize(16777215, 30))
        self.lb_compra_quant.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_compra_quant)

        self.le_compra_quant = QLineEdit(self.frame)
        self.le_compra_quant.setObjectName(u"le_compra_quant")
        self.le_compra_quant.setMinimumSize(QSize(0, 30))
        self.le_compra_quant.setMaximumSize(QSize(16777215, 30))
        self.le_compra_quant.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_compra_quant)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.frame)

        self.fr_bot = QFrame(wind_add_compra)
        self.fr_bot.setObjectName(u"fr_bot")
        self.fr_bot.setFrameShape(QFrame.StyledPanel)
        self.fr_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_confirma_compra = QPushButton(self.fr_bot)
        self.pb_confirma_compra.setObjectName(u"pb_confirma_compra")
        self.pb_confirma_compra.setMinimumSize(QSize(200, 30))
        self.pb_confirma_compra.setMaximumSize(QSize(200, 30))
        self.pb_confirma_compra.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_confirma_compra.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_confirma_compra)

        self.pb_cancela_compra = QPushButton(self.fr_bot)
        self.pb_cancela_compra.setObjectName(u"pb_cancela_compra")
        self.pb_cancela_compra.setMinimumSize(QSize(200, 30))
        self.pb_cancela_compra.setMaximumSize(QSize(200, 30))
        self.pb_cancela_compra.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cancela_compra.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_cancela_compra)


        self.verticalLayout.addWidget(self.fr_bot)


        self.retranslateUi(wind_add_compra)

        QMetaObject.connectSlotsByName(wind_add_compra)
    # setupUi

    def retranslateUi(self, wind_add_compra):
        wind_add_compra.setWindowTitle(QCoreApplication.translate("wind_add_compra", u"Adicionar Ponto de Compra", None))
        self.lb_codforn.setText(QCoreApplication.translate("wind_add_compra", u"<html><head/><body><p align=\"right\">C\u00f3digo Fabricante</p></body></html>", None))
        self.cp_codfabr.setText(QCoreApplication.translate("wind_add_compra", u"TextLabel", None))
        self.lb_descprod.setText(QCoreApplication.translate("wind_add_compra", u"<html><head/><body><p align=\"right\">Descri\u00e7\u00e3o do Produto</p></body></html>", None))
        self.cp_descprod.setText(QCoreApplication.translate("wind_add_compra", u"TextLabel", None))
        self.lb_saldo.setText(QCoreApplication.translate("wind_add_compra", u"<html><head/><body><p align=\"right\">Saldo</p></body></html>", None))
        self.cp_saldo.setText(QCoreApplication.translate("wind_add_compra", u"TextLabel", None))
        self.lb_pontocompra.setText(QCoreApplication.translate("wind_add_compra", u"Ponto de Compra", None))
        self.cp_lim_min.setText(QCoreApplication.translate("wind_add_compra", u"TextLabel", None))
        self.lb_compra_quant.setText(QCoreApplication.translate("wind_add_compra", u"<html><head/><body><p align=\"right\">Quantidade M\u00ednima</p></body></html>", None))
        self.pb_confirma_compra.setText(QCoreApplication.translate("wind_add_compra", u"Confirmar", None))
        self.pb_cancela_compra.setText(QCoreApplication.translate("wind_add_compra", u"Cancelar", None))
    # retranslateUi

