import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText("First Name: ")
    l1.move(100, 20)
    f1 = QtWidgets.QLineEdit(w)
    f1.move(180, 20)

    l2 = QtWidgets.QLabel(w)
    l2.setText("Last Name: ")
    l2.move(100, 60)
    f2 = QtWidgets.QLineEdit(w)
    f2.move(180, 60)

    l3 = QtWidgets.QLabel(w)
    l3.setText("Age: \t")
    l3.move(100, 100)
    f3 = QtWidgets.QLineEdit(w)
    f3.move(180, 100)

    b1 = QtWidgets.QPushButton('OK',w)
    b1.move(180,140)

    w.setWindowTitle("Form")
    w.setGeometry(400, 100, 600, 400)

    w.show()
    sys.exit(app.exec_())

window()