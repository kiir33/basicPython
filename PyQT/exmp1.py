import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox, QLabel

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Addition_App'
        self.left = 400
        self.top = 100
        self.width = 300
        self.height = 300
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Create Label 1
        self.label1 = QLabel(self)
        self.label1.setText("First Num : ")
        self.label1.move(20,20)

        # Create textbox 1
        self.firstNum = QLineEdit(self)
        self.firstNum.move(100, 20)
        self.firstNum.resize(100, 20)

        # Create Label 2
        self.label2 = QLabel(self)
        self.label2.setText("Second Num : ")
        self.label2.move(20, 50)

        # Create textbox 2
        self.secNum = QLineEdit(self)
        self.secNum.move(100, 50)
        self.secNum.resize(100, 20)

        # Create a button in the window
        self.button = QPushButton('ADD', self)
        self.button.move(100, 100)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()


    #@pyqtSlot()
    def on_click(self):
        fNum = int(self.firstNum.text())
        sNum = int(self.secNum.text())
        sum =fNum + sNum
        QMessageBox.question(self, 'Results: ', "Sum of two numbers is :  " + str(sum), QMessageBox.Ok, QMessageBox.Ok)
        self.firstNum.setText("")
        self.secNum.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())