import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Addition_App'
        self.left = 400
        self.top = 100
        self.width = 400
        self.height = 300
        self.sum = 0
        self.dif = 0
        self.mul = 0
        self.div = 0
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)



        #Create Label 1
        self.label1 = QLabel("First Num : ")

        # Create textbox 1
        self.firstNum = QLineEdit(self)

        # Create Label 2
        self.label2 = QLabel("Second Num : ")

        # Create textbox 2
        self.secNum = QLineEdit(self)

        # Create a button in the window
        self.button = QPushButton('CALCULATE', self)

        # Create ResultLabel add
        self.add_result = QLabel("Sum")

        # Create ResultLabel difference
        self.dif_result = QLabel("Difference")

        # Create ResultLabel product
        self.mul_result = QLabel("Product")

        # Create ResultLabel division
        self.div_result = QLabel("Quotient")

        self.add_result1 = QLabel(str(self.sum))
        self.dif_result1 = QLabel(str(self.dif))
        self.mul_result1 = QLabel(str(self.mul))
        self.div_result1 = QLabel(str(self.div))

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        l1 = QGridLayout()

        l1.addWidget(self.label1,0,0)
        l1.addWidget(self.label2,1,0)
        l1.addWidget(self.firstNum,0,1)
        l1.addWidget(self.secNum,1,1)
        l1.addWidget(self.button,2,1)

        l1.addWidget(self.add_result,3,0)
        l1.addWidget(self.dif_result,4,0)
        l1.addWidget(self.mul_result,5,0)
        l1.addWidget(self.div_result,6,0)

        l1.addWidget(self.add_result1,3,1)
        l1.addWidget(self.dif_result1,4,1)
        l1.addWidget(self.mul_result1,5,1)
        l1.addWidget(self.div_result1,6,1)
        self.setLayout(l1)
        self.show()


    #@pyqtSlot()
    def on_click(self):
        if  (self.firstNum.text() and self.secNum.text()):
            fNum = float(self.firstNum.text())
            sNum = float(self.secNum.text())
            self.sum = fNum + sNum
            self.dif = fNum - sNum
            self.mul = fNum * sNum
            self.div = fNum / sNum
            self.add_result1.setText(str(self.sum))
            self.dif_result1.setText(str(self.dif))
            self.mul_result1.setText(str(self.mul))
            self.div_result1.setText("%.2f"%self.div)

        else:
            QMessageBox.question(self, 'Error!', "Please, Enter the numbers first!!!" , QMessageBox.Ok,QMessageBox.Ok)


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
