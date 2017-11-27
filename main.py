import sys
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication

from src.QTGUI import Ui_Form

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())