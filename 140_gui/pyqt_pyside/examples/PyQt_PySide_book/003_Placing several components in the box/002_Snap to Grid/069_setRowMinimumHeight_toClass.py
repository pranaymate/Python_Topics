from PySide import QtCore, QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.setWindowTitle("setRowMinimumHeight")
        self.resize(300, 50)
        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")
        button4 = QtGui.QPushButton("4")
        grid = QtGui.QGridLayout()
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 1, 0)
        grid.addWidget(button4, 1, 1)
        grid.setRowMinimumHeight(1, 100)
        self.setLayout(grid)
