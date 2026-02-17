from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_MainWindow
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    window.raise_()
    sys.exit(app.exec())

# egor