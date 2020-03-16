from PyQt4 import QtGui
import sys

class SampleWindow(QtGui.QWidget):
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Class QTextCursor")
        self.resize(500, 250)
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setPlainText("Block 1\nBlock 2\nBlock 3\nBlock 4\nBlock 5 jjkh hkjhkjh khk hkh khk jhkh hkh khk hk hkh hkj hk hkhk k kjh kh jh kh khk hkh khk hkjh kh kh kjh kjhkj h kh kh kjh khk hk kh kh k")
        self.button = QtGui.QPushButton("Check the cursor position", self)
        self.button.clicked.connect(self.on_clicked)
        box = QtGui.QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(self.button)
        self.setLayout(box)
        self.show()

    def on_clicked(self):
        self.textEdit.setFocus()
        cur = self.textEdit.textCursor()
        print("atStart", cur.atStart())
        print("atEnd", cur.atEnd())
        print("atBlockStart", cur.atBlockStart())
        print("atBlockEnd", cur.atBlockEnd())
        print("-" * 20)



if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QtGui.QApplication(sys.argv)
    main = SampleWindow()
    main.show()

    if app is not None:
        app.exec_()