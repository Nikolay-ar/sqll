import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
)

class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("riders")
        self.resize(1115, 200)
        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("riders")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "ФИО")
        self.model.setHeaderData(2, Qt.Horizontal, "Номер паспорта")
        self.model.setHeaderData(3, Qt.Horizontal, "Кем и когда выдан")
        self.model.setHeaderData(4, Qt.Horizontal, "Номер вод. уд.")
        self.model.setHeaderData(5, Qt.Horizontal, "Дата выдачи")
        self.model.setHeaderData(6, Qt.Horizontal, "В штате")
        self.model.select()
        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)

def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("db.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec_())