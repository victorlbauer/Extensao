# encoding: utf-8
from PyQt5.QtWidgets import *
    
class Label(QLabel):
    def __init__(self, text=""):
        super(Label, self).__init__()
        self.setText(text)

class LineBar(QLineEdit):
    def __init__(self):
        super(LineBar, self).__init__()

class PushButton(QPushButton):
    def __init__(self, name=""):
        super(PushButton, self).__init__()
        self.setText(name)
        self.clicked.connect(self.OnButtonPress)

    def OnButtonPress(self):
        print("button pressed")