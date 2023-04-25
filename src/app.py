# encoding: utf-8
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from core import *

class Application:
    def __init__(self):
        self._app = QApplication([])
        self._window = window.MainWindow()
        
    def Run(self):
        self._window.show()
        self._app.exec()

    def Shutdown(self):
        pass

if __name__ == "__main__":
    app = Application()
    app.Run()
    app.Shutdown()