from PyQt5.QtWidgets import *
import main

def low0(self):

    self.potion2 = QListWidget()
    self.potion2.insertItem(0, '하급-수렵')
    self.potion2.insertItem(1, '중급-수렵')
    self.potion2.insertItem(2, '상급-수렵')
    return self.potion2




def low1(self):
    layout = QFormLayout()
    label1 = QLabel()
    label1.setText("low1")
    layout.addWidget(label1)

    self.low1.setLayout(layout)



def low2(self):
    layout = QFormLayout()

    label1 = QLabel()
    label1.setText("low2")

    layout.addWidget(label1)

    self.low2.setLayout(layout)