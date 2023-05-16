# from infra.repository.estoque_repo import EstoqueRepo
# from infra.repository.fabricante_repo import FabricantesRepo

# repo = EstoqueRepo()
# # resposta = repo.select_one(**{"ID_FABR": 3})
# # r = repo.my_select_one(**{"COD_FABR": "DER11B"})
# # # resposta = repo.my_select()
# # print(f"{r.COD_INT} - {r.COD_FABR} =>> {r.PRODUTO} | {r.ID_FABR} = {r.fabricantes.NOMEFABR} <<== Saldo {r.SALDO}")
# resp = repo.my_select()
# lst = []
# for r in resp:
#     lst.append(r)
# print(f"Lista = {lst}\n")
# print(f"lista [0] = {lst[0]}\n")
# print(f"lista[10] = {lst[10]}\n")
# print(f"resposta[10] = {resp[10]}\n")

# repo2 = FabricantesRepo()
# resp2 = repo2.my_select()
# for r in resp2:
#     print(r)

# import sys

# from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget


# class Window(QWidget):
#     def __init__(self):
#         super(Window, self).__init__()

#         icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
#         layout = QGridLayout()

#         for n, name in enumerate(icons):
#             btn = QPushButton(name)

#             pixmapi = getattr(QStyle, name)
#             icon = self.style().standardIcon(pixmapi)
#             btn.setIcon(icon)
#             layout.addWidget(btn, n / 4, n % 4)

#         self.setLayout(layout)


# app = QApplication(sys.argv)

# w = Window()
# w.show()

# app.exec()
from PySide6 import QtCore
from PySide6.QtPrintSupport import QPrintDialog, QPrintPreviewDialog
from PySide6.QtGui import QTextCursor, QTextDocument, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (QTableView, QPushButton, QGridLayout, QApplication,
                               QWidget)


class Window(QWidget):
    def __init__(self, rows, columns):
        QWidget.__init__(self)

        self.table = QTableView(self)
        model = QStandardItemModel(rows, columns, self.table)
        for row in range(rows):
            for column in range(columns):
                item = QStandardItem('(%d, %d)' % (row, column))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                model.setItem(row, column, item)
        self.table.setModel(model)
        self.buttonPrint = QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)

    def handlePrint(self):
        dialog = QPrintDialog()
        test = dialog.exec()
        print(test)
        if test == 1:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window(25, 2)
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec())
