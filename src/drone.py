# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Drone.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class App(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(776, 567)
        Form.setMouseTracking(False)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setEnabled(False)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 2, 0, 1, 1)
        self.takeoffButton = QtWidgets.QPushButton(Form)
        self.takeoffButton.setEnabled(False)
        self.takeoffButton.setObjectName("takeoffButton")
        self.gridLayout.addWidget(self.takeoffButton, 0, 0, 1, 1)
        self.landButton = QtWidgets.QPushButton(Form)
        self.landButton.setEnabled(True)
        self.landButton.setObjectName("landButton")
        self.gridLayout.addWidget(self.landButton, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 2, 5, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.xVelLabel = QtWidgets.QLabel(Form)
        self.xVelLabel.setObjectName("xVelLabel")
        self.gridLayout_6.addWidget(self.xVelLabel, 1, 1, 1, 1)
        self.yVelLabel = QtWidgets.QLabel(Form)
        self.yVelLabel.setObjectName("yVelLabel")
        self.gridLayout_6.addWidget(self.yVelLabel, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)
        self.zVelLabel = QtWidgets.QLabel(Form)
        self.zVelLabel.setObjectName("zVelLabel")
        self.gridLayout_6.addWidget(self.zVelLabel, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cwButton = QtWidgets.QPushButton(Form)
        self.cwButton.setObjectName("cwButton")
        self.gridLayout_2.addWidget(self.cwButton, 0, 2, 1, 1)
        self.leftButton = QtWidgets.QPushButton(Form)
        self.leftButton.setObjectName("leftButton")
        self.gridLayout_2.addWidget(self.leftButton, 2, 0, 1, 1)
        self.rightButton = QtWidgets.QPushButton(Form)
        self.rightButton.setObjectName("rightButton")
        self.gridLayout_2.addWidget(self.rightButton, 2, 2, 1, 1)
        self.backwardButton = QtWidgets.QPushButton(Form)
        self.backwardButton.setObjectName("backwardButton")
        self.gridLayout_2.addWidget(self.backwardButton, 3, 1, 1, 1)
        self.ccwButton = QtWidgets.QPushButton(Form)
        self.ccwButton.setObjectName("ccwButton")
        self.gridLayout_2.addWidget(self.ccwButton, 0, 0, 1, 1)
        self.forwardButton = QtWidgets.QPushButton(Form)
        self.forwardButton.setObjectName("forwardButton")
        self.gridLayout_2.addWidget(self.forwardButton, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.decreaseAltButton = QtWidgets.QPushButton(Form)
        self.decreaseAltButton.setObjectName("decreaseAltButton")
        self.gridLayout_3.addWidget(self.decreaseAltButton, 2, 0, 1, 1)
        self.increaseAltButton = QtWidgets.QPushButton(Form)
        self.increaseAltButton.setObjectName("increaseAltButton")
        self.gridLayout_3.addWidget(self.increaseAltButton, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 0, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 2, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 2, 8, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 2, 4, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_5.addWidget(self.saveButton, 2, 7, 1, 1)
        self.batteryLabel = QtWidgets.QLabel(Form)
        self.batteryLabel.setObjectName("batteryLabel")
        self.gridLayout_5.addWidget(self.batteryLabel, 0, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem7, 1, 7, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def toggleEnabled(self):
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.resetButton.setToolTip(_translate("Form", "<html><head/><body><p>Reset (P)</p></body></html>"))
        self.resetButton.setText(_translate("Form", "Reset"))
        self.resetButton.setShortcut(_translate("Form", "P"))
        self.takeoffButton.setToolTip(_translate("Form", "<html><head/><body><p>Take off (T)</p></body></html>"))
        self.takeoffButton.setText(_translate("Form", "Takeoff"))
        self.takeoffButton.setShortcut(_translate("Form", "T"))
        self.landButton.setToolTip(_translate("Form", "<html><head/><body><p>Land (L)</p></body></html>"))
        self.landButton.setText(_translate("Form", "Land"))
        self.landButton.setShortcut(_translate("Form", "L"))
        self.label.setText(_translate("Form", "X Velocity:"))
        self.xVelLabel.setText(_translate("Form", "TextLabel"))
        self.yVelLabel.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Y Velocity:"))
        self.zVelLabel.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "Z Velocity:"))
        self.cwButton.setToolTip(_translate("Form", "<html><head/><body><p>Rotate the drone clockwise (E)</p></body></html>"))
        self.cwButton.setText(_translate("Form", "Clockwise"))
        self.cwButton.setShortcut(_translate("Form", "E"))
        self.leftButton.setToolTip(_translate("Form", "<html><head/><body><p>Move the drone left (A)</p></body></html>"))
        self.leftButton.setText(_translate("Form", "Left"))
        self.leftButton.setShortcut(_translate("Form", "A"))
        self.rightButton.setToolTip(_translate("Form", "<html><head/><body><p>Move the drone right (D)</p></body></html>"))
        self.rightButton.setText(_translate("Form", "Right"))
        self.rightButton.setShortcut(_translate("Form", "D"))
        self.backwardButton.setToolTip(_translate("Form", "<html><head/><body><p>Move the drone backward (S)</p></body></html>"))
        self.backwardButton.setText(_translate("Form", "Backward"))
        self.backwardButton.setShortcut(_translate("Form", "S"))
        self.ccwButton.setToolTip(_translate("Form", "<html><head/><body><p>Rotate the drone counter clockwise (Q)</p></body></html>"))
        self.ccwButton.setText(_translate("Form", "AntiClockwise"))
        self.ccwButton.setShortcut(_translate("Form", "Q"))
        self.forwardButton.setToolTip(_translate("Form", "<html><head/><body><p>Move the drone forward (W)</p></body></html>"))
        self.forwardButton.setText(_translate("Form", "Forward"))
        self.forwardButton.setShortcut(_translate("Form", "W"))
        self.decreaseAltButton.setToolTip(_translate("Form", "<html><head/><body><p>Decrease the drone\'s altitude (C)</p></body></html>"))
        self.decreaseAltButton.setText(_translate("Form", "Decrease Altitude"))
        self.decreaseAltButton.setShortcut(_translate("Form", "C"))
        self.increaseAltButton.setToolTip(_translate("Form", "<html><head/><body><p>Increase the drone\'s altitude (space)</p></body></html>"))
        self.increaseAltButton.setText(_translate("Form", "Increase Altitude"))
        self.increaseAltButton.setShortcut(_translate("Form", "Space"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.batteryLabel.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Battery:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = App()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

