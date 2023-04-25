# encoding: utf-8
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from dataclasses import dataclass

from .widgets import *

@dataclass
class MainWindowInfo:
    title: str = "Unnamed"
    minWidth: int = 400
    minHeight: int = 300

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
      
        # Main window
        info = MainWindowInfo()
        self.setWindowTitle(info.title)
        self.setMinimumSize(QSize(info.minWidth, info.minHeight))
        self.InitWidgets()

    def InitWidgets(self):
        # Button
        pushButton = PushButton("Gerar")

        # Labels & line bars
        widthLabel = Label("Largura")
        lengthLabel = Label("Comprimento")

        self._widthBar = LineBar()
        self._lengthBar = LineBar()

        widthLabel.setBuddy(self._widthBar)
        widthLabel.setBuddy(self._lengthBar)

        barContainer = QWidget()
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(lengthLabel, 0, 1)
        layout.addWidget(self._widthBar, 1, 0)
        layout.addWidget(self._lengthBar, 1, 1)
        barContainer.setLayout(layout)

        # Empty container for the main layout
        self._container = QWidget()
        self._containerLayout = QHBoxLayout()
        self._containerLayout.addWidget(barContainer)
        self._containerLayout.addWidget(pushButton)
        self._container.setLayout(self._containerLayout)

        self.setCentralWidget(self._container)

    def OnButtonPress(self):
        print("Projeto sendo gerado...")
        print("Valor da largura: " + self._widthBar.text())
        print("Valor do comprimento: " + self._lengthBar.text())