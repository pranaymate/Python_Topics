# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Выравнивание по сетке")
window.resize(300, 50)
button1 = QtGui.QPushButton("1")
button2 = QtGui.QPushButton("2")
button4 = QtGui.QPushButton("4")
grid = QtGui.QGridLayout()
grid.addWidget(button1, 0, 0, 2, 1)
grid.addWidget(button2, 0, 1)
grid.addWidget(button4, 1, 1)
window.setLayout(grid)
window.show()
sys.exit(app.exec_())