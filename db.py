import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView,
    QPushButton,
)
bt_style = ("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 24px;}"
                           "QPushButton:pressed {background-color:rgb(31,101,163) ; }")

class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("riders")
        self.resize(1115, 200)
     
        pybutton = QPushButton('Click me', self)
        # pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(950, 50)


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


    def _addRow(self):
        self.model.insertRow(-1)

    def addRecord(self):
        row = self.model.rowCount()
        self.model.insertRow(row)
        index = self.model.index(row, 1)
        self.view.setCurrentIndex(index)
        self.view.edit(index)
    
    def _removeRow(self):
        self.model.removeRow()
    def _copyRow(self):
        pass


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