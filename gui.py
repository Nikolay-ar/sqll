from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Простая программа")
    window.setGeometry(300, 250, 350, 200)

    mai_text = QtWidgets.QLabel(window)
    mai_text.setText("базовая надпись")
    mai_text.move(100, 100)
    mai_text.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("нажмт на меня")
    btn.setFixedWidth(200)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()
