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

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
        layout = QGridLayout()

        for n, name in enumerate(icons):
            btn = QPushButton(name)

            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, n / 4, n % 4)

        self.setLayout(layout)


app = QApplication(sys.argv)

w = Window()
w.show()

app.exec()
