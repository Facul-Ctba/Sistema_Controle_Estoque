from datetime import datetime
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QIcon


class Edit_TableModel(QAbstractTableModel):
    def __init__(self, data, columns):
        super(Edit_TableModel, self).__init__()
        self._data = data
        self.columns = columns

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

    def data(self, index, role):
        value = self._data[index.row()][index.column()]

        if role == Qt.UserRole:
            if index.column() == 5:
                if str(value) == "1":
                    return "T"
                else:
                    return ""
            return value

        if role == Qt.DisplayRole:
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return "%.2f" % value
            else:
                return str(value)

        if role == Qt.EditRole:
            if isinstance(value, float):
                return "%.2f" % value
            else:
                return str(self._data[index.row()][index.column()])

        if role == Qt.TextAlignmentRole:
            if index.column() == 0:
                return Qt.AlignVCenter + Qt.AlignHCenter
            if isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight
            if isinstance(value, int):
                return Qt.AlignVCenter + Qt.AlignHCenter

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            try:
                return value
            except TypeError:
                return False
        return False

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        except IndexError:
            return 0


class TableModel(QAbstractTableModel):
    def __init__(self, data, columns, _icon_wrn=None, _icon_ok=None):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = columns
        self._icon_wrn = _icon_wrn
        self._icon_ok = _icon_ok

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

    def data(self, index, role):
        value = self._data[index.row()][index.column()]

        if role == Qt.UserRole:
            if index.column() == 5:
                if str(value) == "1":
                    return "T"
                else:
                    return ""
            return value

        if role == Qt.DisplayRole:
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return "%.2f" % value
            if index.column() == 5:
                return ''
            else:
                return value

        if role == Qt.TextAlignmentRole:
            if index.column() == 0:
                return Qt.AlignVCenter + Qt.AlignHCenter
            if index.column() == 5:
                return Qt.AlignVCenter + Qt.AlignHCenter
            if isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight
            if isinstance(value, int):
                return Qt.AlignVCenter + Qt.AlignHCenter

        if role == Qt.DecorationRole:
            if index.column() == 5:
                if value == 1:
                    return QIcon(self._icon_wrn)
                elif value == 0:
                    return QIcon(self._icon_ok)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        except IndexError:
            return 0
