from pyardrone import ARDrone

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

drone = ARDrone()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GameOfDrones Test GUI'
        self.left = 100
        self.top = 100
        self.width = 420
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        forwards_btn = QPushButton('^', self)
        forwards_btn.setToolTip('Moves the drone forward')
        forwards_btn.move(100, 80)
        forwards_btn.clicked.connect(self.forward)

        backwards_btn = QPushButton('v', self)
        backwards_btn.setToolTip('Moves the drone backward')
        backwards_btn.move(100, 140)
        backwards_btn.clicked.connect(self.backward)

        right_btn = QPushButton('>', self)
        right_btn.setToolTip('Moves the drone right')
        right_btn.move(160, 110)
        right_btn.clicked.connect(self.right)

        left_btn = QPushButton('<', self)
        left_btn.setToolTip('Moves the drone move_left')
        left_btn.move(40, 110)
        left_btn.clicked.connect(self.move_left)

        cw_btn = QPushButton('CW->', self)
        cw_btn.setToolTip('Rotates the drone cw')
        cw_btn.move(160, 40)
        cw_btn.clicked.connect(self.cw)

        ccw_btn = QPushButton('<-CCW', self)
        ccw_btn.setToolTip('Rotates the drone ccw')
        ccw_btn.move(40, 40)
        ccw_btn.clicked.connect(self.ccw)

        increase_alt_btn = QPushButton('IncreaseAlt', self)
        increase_alt_btn.setToolTip('Increase Altitude')
        increase_alt_btn.move(280, 50)
        increase_alt_btn.clicked.connect(self.increase_alt)

        decrease_alt_btn = QPushButton('DecreaseAlt', self)
        decrease_alt_btn.setToolTip('Decrease Altitude')
        decrease_alt_btn.move(280, 80)
        decrease_alt_btn.clicked.connect(self.decrease_alt)

        takeoff_btn = QPushButton('Takeoff', self)
        takeoff_btn.setToolTip('Takeoff')
        takeoff_btn.move(280, 150)
        takeoff_btn.clicked.connect(self.takeoff)

        land_btn = QPushButton('Land', self)
        land_btn.setToolTip('Land')
        land_btn.move(280, 180)
        land_btn.clicked.connect(self.land)

        self.show()

    @pyqtSlot(name="forward")
    def forward(self):
        # print(drone.navdata)
        drone.move(forward=1)
        print("moving drone forward")

    @pyqtSlot(name="backward")
    def backward(self):
        # print(drone.navdata)
        drone.move(backward=1)
        print("moving drone backward")

    @pyqtSlot(name="right")
    def right(self):
        # print(drone.navdata)
        drone.move(right=1)
        print("moving drone right")

    @pyqtSlot(name="move_left")
    def move_left(self):
        # print(drone.navdata)
        drone.move(left=1)
        print("moving drone left")

    @pyqtSlot(name="cw")
    def cw(self):
        # print(drone.navdata)
        drone.move(cw=1)
        print("rotating clockwise")

    @pyqtSlot(name="ccw")
    def ccw(self):
        # print(drone.navdata)
        drone.move(ccw=1)
        print("rotating counter-clockwise")

    @pyqtSlot(name="IncreaseAlt")
    def increase_alt(self):
        # print(drone.navdata)
        drone.move(up=1)
        print("increasing altitude")

    @pyqtSlot(name="DecreaseAlt")
    def decrease_alt(self):
        # print(drone.navdata)
        drone.move(down=1)
        print("decreasing altitude")

    @pyqtSlot(name="takeoff")
    def takeoff(self):
        # print(drone.navdata)
        while not drone.state.fly_mask:
            drone.takeoff()
        print("taking off")

    @pyqtSlot(name="land")
    def land(self):
        # print(drone.navdata)
        while drone.state.fly_mask:
            drone.land()
        print("landing")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
