# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys

class MyItem(QtGui.QGraphicsItem):
    pen_width = 1
    def boundingRect(self):
        return QtCore.QRectF(-200 - MyItem.pen_width, -100 - MyItem.pen_width,
                             400 + MyItem.pen_width*2, 200 + MyItem.pen_width*2)

    def paint(self, painter, option, widget):
        painter.save()
        painter.setPen(QtGui.QPen(QtCore.Qt.red, MyItem.pen_width))
        painter.setBrush(QtCore.Qt.darkGreen)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.drawEllipse(-200, -100, 400, 200)
        painter.restore()

    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(-200, -100, 400, 200)
        return path

def on_clicked():
    view.setFocus()
    my_item.resetMatrix()

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle("Класс QGraphicsItem")
window.resize(600, 600)

scene = QtGui.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0),
                     pen=QtGui.QPen(QtCore.Qt.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)

my_item = MyItem()
my_item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
my_item.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
my_item.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
my_item.setPos(250, 380)
my_item.translate(0, 0)
my_item.rotate(90.0)
my_item.scale(0.5, 0.5)
my_item.shear(0.3, 0.3)
scene.addItem(my_item)
view = QtGui.QGraphicsView(scene)

button = QtGui.QPushButton("Сбросить трансформацию")
button.clicked.connect(on_clicked)

box = QtGui.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())