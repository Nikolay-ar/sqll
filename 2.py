import base64
import platform
import sqlite3
import sys
import tempfile
import webbrowser
from os import system
from pathlib import Path

from PyQt5 import QeWi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QWidget

from doc import open_base, delete_from_base, encode_b64, \
    save_to_base, create_base, save_doc_from_base, decode_b64, vacuum_base, update_data, select_tag
from doc_b import *

class MyWin(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.base_name = None
        self.data = None