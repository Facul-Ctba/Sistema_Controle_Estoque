# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wind_addforn.ui'
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

class Ui_wind_add_forn(object):
    def setupUi(self, wind_add_forn):
        if not wind_add_forn.objectName():
            wind_add_forn.setObjectName(u"wind_add_forn")
        wind_add_forn.resize(827, 175)
        wind_add_forn.setMinimumSize(QSize(827, 175))
        wind_add_forn.setMaximumSize(QSize(827, 175))
        self.verticalLayout = QVBoxLayout(wind_add_forn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fr_top = QFrame(wind_add_forn)
        self.fr_top.setObjectName(u"fr_top")
        self.fr_top.setMinimumSize(QSize(0, 100))
        self.fr_top.setMaximumSize(QSize(16777215, 100))
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
        self.lb_nomeforn = QLabel(self.fr_top)
        self.lb_nomeforn.setObjectName(u"lb_nomeforn")
        self.lb_nomeforn.setMinimumSize(QSize(0, 30))
        self.lb_nomeforn.setMaximumSize(QSize(16777215, 30))
        self.lb_nomeforn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lb_nomeforn)

        self.le_nomeforn = QLineEdit(self.fr_top)
        self.le_nomeforn.setObjectName(u"le_nomeforn")
        self.le_nomeforn.setMinimumSize(QSize(0, 30))
        self.le_nomeforn.setMaximumSize(QSize(16777215, 30))
        self.le_nomeforn.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_nomeforn)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.fr_top, 0, Qt.AlignVCenter)

        self.fr_bot = QFrame(wind_add_forn)
        self.fr_bot.setObjectName(u"fr_bot")
        self.fr_bot.setFrameShape(QFrame.StyledPanel)
        self.fr_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bot)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_confirma_forn = QPushButton(self.fr_bot)
        self.pb_confirma_forn.setObjectName(u"pb_confirma_forn")
        self.pb_confirma_forn.setMinimumSize(QSize(200, 30))
        self.pb_confirma_forn.setMaximumSize(QSize(200, 30))
        self.pb_confirma_forn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_confirma_forn.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(85, 255, 127);	\n"
"	color: rgb(255, 0, 0);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_confirma_forn)

        self.pb_cancela_forn = QPushButton(self.fr_bot)
        self.pb_cancela_forn.setObjectName(u"pb_cancela_forn")
        self.pb_cancela_forn.setMinimumSize(QSize(200, 30))
        self.pb_cancela_forn.setMaximumSize(QSize(200, 30))
        self.pb_cancela_forn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_cancela_forn.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: rgb(0, 0, 255);\n"
"	border-radius: 10px\n"
"}")

        self.horizontalLayout.addWidget(self.pb_cancela_forn)


        self.verticalLayout.addWidget(self.fr_bot, 0, Qt.AlignTop)


        self.retranslateUi(wind_add_forn)

        QMetaObject.connectSlotsByName(wind_add_forn)
    # setupUi

    def retranslateUi(self, wind_add_forn):
        wind_add_forn.setWindowTitle(QCoreApplication.translate("wind_add_forn", u"Adicionar Novo Fabricante", None))
        self.lb_nomeforn.setText(QCoreApplication.translate("wind_add_forn", u"<html><head/><body><p align=\"right\">Nome Fabricante</p></body></html>", None))
        self.pb_confirma_forn.setText(QCoreApplication.translate("wind_add_forn", u"Confirmar", None))
        self.pb_cancela_forn.setText(QCoreApplication.translate("wind_add_forn", u"Cancelar", None))
    # retranslateUi

