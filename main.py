import sys
from PyQt5.QtWidgets import QApplication

from src.QTGUI import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form()

    sys.exit(app.exec_())