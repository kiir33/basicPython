import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,300)
window.move(400,200)
window.setWindowTitle("My First GUI App")
window.show()
sys.exit(app.exec_())