import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window.move(300,200)
window.setWindowTitle("My First GUI App")
window.show()
status = app.exec_()
sys.exit(status)