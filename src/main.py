from window import *
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    app.exec()
