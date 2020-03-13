______ ___
____ _5._W.. ______ _
____ _5._G.. ______  QF..

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Message Boxes")
        self.setGeometry(250, 150, 500, 500)
        self.ui()

    def ui(self):
        button = QPushButton("Click ME!", self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.message_box)

        self.show()

    def message_box(self):
        # mbox=QMessageBox.question(self,"Warning!!!","Are you sure to exit?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
        # if mbox==QMessageBox.Yes:
        #     sys.exit()
        # elif mbox==QMessageBox.No:
        #     print("You Clicked No Button")
        mbox = QMessageBox.information(self, "Information", "You Logged Out!")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()