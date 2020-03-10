____ __.__ ______ _
____ __.__ ______ _
____ w..______ p_UIs __ ui
____ w.. ______ pLW..

______ cPD.. sD.. tE.. s..

class projectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(projectManagerClass, self).__init__()
        self.setupUi(self)

        # widgets

        self.projectList_lwd = projectListWidget.projectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)

        # connects

        self.create_btn.clicked.connect(self.createProject)
        self.settings_btn.clicked.connect(self.openSettingsDialog)
        self.templateEditor_btn.clicked.connect(self.openTemplateEditorDialog)

        # start

        self.updateList()

    def updateList(self):
        if not self.projectList_lwd.updateProjectList():
            self.create_btn.setEnabled(0)
        else:
            self.create_btn.setEnabled(1)

    def openSettingsDialog(self):
        self.dial = settingsDialog.settingsDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getTableOrder()
            settings.settingsClass().save(data)
        self.updateList()

    def openTemplateEditorDialog(self):
        self.dial = templateEditor.templateEditorClass()
        self.dial.show()

    def createProject(self):
        self.dial = createProjectDialog.projectManagerClass(self)
        if self.dial.exec_():
            print 'CREATE'

    def showInfo(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = projectManagerClass()
    w.show()
    app.exec_()