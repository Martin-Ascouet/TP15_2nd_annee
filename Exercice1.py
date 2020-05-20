from PySide2.QtWidgets import QWidget,QDialog,QTableWidget,QHBoxLayout,QHeaderView,QVBoxLayout,QTextEdit, QLineEdit,  QGridLayout, QLabel, QPushButton, QProgressBar, QApplication

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('SQL client')
        self.setMinimumSize(600, 400)

        self.layout = QVBoxLayout()
        self.buttonsPanel = ButtonsPanel()
        self.notificationPanel = QTextEdit()
        self.resultTable = QTableWidget(5, 3)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonsPanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resultTable)

        self.setLayout(self.layout)

class  ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout2 = QHBoxLayout()
        self.button1 = QPushButton('Configure')
        self.button2 = QPushButton('Connect')
        self.button3 = QPushButton('Disconnect')

        self.layout2.addWidget(self.button1)
        self.layout2.addWidget(self.button2)
        self.layout2.addWidget(self.button3)

        self.setLayout(self.layout2)

class  LabeledTextField(QWidget):
    def __init__(self, txt):
        QWidget.__init__(self)
        self.setWindowTitle('Configuration')

        self.layout = QHBoxLayout()

        self.txt = QLabel(txt)
        self.textedit = QTextEdit()
        self.textedit.setMaximumHeight(30)

        self.layout.addWidget(self.txt)
        self.layout.addWidget(self.textedit)

        self.setLayout(self.layout)


class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()

        self.txtEdit1 = LabeledTextField('IP adresse')
        self.txtEdit2 = LabeledTextField('User')
        self.txtEdit3 = LabeledTextField('Password')

        self.layout.addWidget(self.txtEdit1)
        self.layout.addWidget(self.txtEdit2)
        self.layout.addWidget(self.txtEdit3)

        self.setLayout(self.layout)

        self.win = SQLClientWindow()
        self.win.show()
        self.show()

if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   app.exec_()
