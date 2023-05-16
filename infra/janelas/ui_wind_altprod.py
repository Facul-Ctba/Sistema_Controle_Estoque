# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_altprod.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_wind_alt_prod(object):
    def setupUi(self, wind_alt_prod):
        if not wind_alt_prod.objectName():
            wind_alt_prod.setObjectName(u"wind_alt_prod")
        wind_alt_prod.resize(827, 306)
        wind_alt_prod.setMinimumSize(QSize(827, 306))
        wind_alt_prod.setMaximumSize(QSize(827, 306))
        self.verticalLayout = QVBoxLayout(wind_alt_prod)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_top = QFrame(wind_alt_prod)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 230))
        self.fr_top.setMaximumSize(QSize(16777215, 230))
        self.fr_top.setFrameShape(QFrame.StyledPanel)
        self.fr_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_top)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.lb_codint = QLabel(self.fr_top)
        self.lb_codint.setObjectName(u"lb_codint")
        self.lb_codint.setMinimumSize(QSize(0, 30))
        self.lb_codint.setMaximumSize(QSize(16777215, 30))
        self.lb_codint.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_codint)

        self.le_codint = QLineEdit(self.fr_top)
        self.le_codint.setObjectName(u"le_codint")
        self.le_codint.setMinimumSize(QSize(0, 30))
        self.le_codint.setMaximumSize(QSize(16777215, 30))
        self.le_codint.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_codint)

        self.lb_codforn = QLabel(self.fr_top)
        self.lb_codforn.setObjectName(u"lb_codforn")
        self.lb_codforn.setMinimumSize(QSize(0, 30))
        self.lb_codforn.setMaximumSize(QSize(16777215, 30))
        self.lb_codforn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_codforn)

        self.le_codforn = QLineEdit(self.fr_top)
        self.le_codforn.setObjectName(u"le_codforn")
        self.le_codforn.setMinimumSize(QSize(0, 30))
        self.le_codforn.setMaximumSize(QSize(16777215, 30))
        self.le_codforn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_codforn)

        self.lb_descprod = QLabel(self.fr_top)
        self.lb_descprod.setObjectName(u"lb_descprod")
        self.lb_descprod.setMinimumSize(QSize(0, 30))
        self.lb_descprod.setMaximumSize(QSize(16777215, 30))
        self.lb_descprod.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lb_descprod)

        self.le_descprod = QLineEdit(self.fr_top)
        self.le_descprod.setObjectName(u"le_descprod")
        self.le_descprod.setMinimumSize(QSize(0, 30))
        self.le_descprod.setMaximumSize(QSize(16777215, 30))
        self.le_descprod.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_descprod)

        self.lb_saldo = QLabel(self.fr_top)
        self.lb_saldo.setObjectName(u"lb_saldo")
        self.lb_saldo.setMinimumSize(QSize(0, 30))
        self.lb_saldo.setMaximumSize(QSize(16777215, 30))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_saldo)

        self.le_saldo = QLineEdit(self.fr_top)
        self.le_saldo.setObjectName(u"le_saldo")
        self.le_saldo.setMinimumSize(QSize(0, 30))
        self.le_saldo.setMaximumSize(QSize(16777215, 30))
        self.le_saldo.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_saldo)

        self.lb_forn = QLabel(self.fr_top)
        self.lb_forn.setObjectName(u"lb_forn")
        self.lb_forn.setMinimumSize(QSize(0, 30))
        self.lb_forn.setMaximumSize(QSize(16777215, 30))
        self.lb_forn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lb_forn)

        self.cb_fornec = QComboBox(self.fr_top)
        self.cb_fornec.setObjectName(u"cb_fornec")
        self.cb_fornec.setMinimumSize(QSize(0, 30))
        self.cb_fornec.setMaximumSize(QSize(16777215, 30))
        self.cb_fornec.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_fornec.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.cb_fornec.setMaxVisibleItems(5)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cb_fornec)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.fr_top, 0, Qt.AlignVCenter)

        self.fr_bot = QFrame(wind_alt_prod)
        self.fr_bot.setObjectName(u"fr_bot")
        self.fr_bot.setFrameShape(QFrame.StyledPanel)
        self.fr_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_confirma_prod = QPushButton(self.fr_bot)
        self.pb_confirma_prod.setObjectName(u"pb_confirma_prod")
        self.pb_confirma_prod.setMinimumSize(QSize(200, 30))
        self.pb_confirma_prod.setMaximumSize(QSize(200, 30))
        self.pb_confirma_prod.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_confirma_prod.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_confirma_prod)

        self.pb_cancela_prod = QPushButton(self.fr_bot)
        self.pb_cancela_prod.setObjectName(u"pb_cancela_prod")
        self.pb_cancela_prod.setMinimumSize(QSize(200, 30))
        self.pb_cancela_prod.setMaximumSize(QSize(200, 30))
        self.pb_cancela_prod.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cancela_prod.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_cancela_prod)


        self.verticalLayout.addWidget(self.fr_bot, 0, Qt.AlignTop)


        self.retranslateUi(wind_alt_prod)

        QMetaObject.connectSlotsByName(wind_alt_prod)
    # setupUi

    def retranslateUi(self, wind_alt_prod):
        wind_alt_prod.setWindowTitle(QCoreApplication.translate("wind_alt_prod", u"Altera\u00e7\u00e3o de Produto Cadastrado", None))
        self.lb_codint.setText(QCoreApplication.translate("wind_alt_prod", u"<html><head/><body><p align=\"right\">C\u00f3digo Interno</p></body></html>", None))
        self.lb_codforn.setText(QCoreApplication.translate("wind_alt_prod", u"<html><head/><body><p align=\"right\">C\u00f3digo Fabricante</p></body></html>", None))
        self.lb_descprod.setText(QCoreApplication.translate("wind_alt_prod", u"<html><head/><body><p align=\"right\">Descri\u00e7\u00e3o do Produto</p></body></html>", None))
        self.lb_saldo.setText(QCoreApplication.translate("wind_alt_prod", u"Saldo", None))
        self.lb_forn.setText(QCoreApplication.translate("wind_alt_prod", u"<html><head/><body><p align=\"right\">Fabricante</p></body></html>", None))
        self.pb_confirma_prod.setText(QCoreApplication.translate("wind_alt_prod", u"Confirmar", None))
        self.pb_cancela_prod.setText(QCoreApplication.translate("wind_alt_prod", u"Cancelar", None))
    # retranslateUi

