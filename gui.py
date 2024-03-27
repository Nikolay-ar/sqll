from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)
        self.new_text = QtWidgets.QLabel(self)

        self.mai_text = QtWidgets.QLabel(self)
        self.mai_text.setText("базовая надпись")
        self.mai_text.move(100, 100)
        self.mai_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("нажмт на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText("вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()
