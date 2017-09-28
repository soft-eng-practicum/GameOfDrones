from random import randint
from threading import Thread
from time import sleep

import sys
from pyardrone import ARDrone

from src.Logger import Logger
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction
from PyQt5.QtCore import pyqtSlot


# import cv2

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GameOfDrones Test GUI'
        self.left = 100
        self.top = 100
        self.width = 420
        self.height = 260
        self.initUI()
        self.logger = Logger()
        self.drone = ARDrone()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.closer)

        forwards_btn = QPushButton('&w', self)
        forwards_btn.setToolTip('Moves the drone forward')
        forwards_btn.move(100, 80)
        forwards_btn.clicked.connect(self.forward)

        backwards_btn = QPushButton('&s', self)
        backwards_btn.setToolTip('Moves the drone backward')
        backwards_btn.move(100, 140)
        backwards_btn.clicked.connect(self.backward)

        right_btn = QPushButton('&d', self)
        right_btn.setToolTip('Moves the drone right')
        right_btn.move(160, 110)
        right_btn.clicked.connect(self.right)

        left_btn = QPushButton('&a', self)
        left_btn.setToolTip('Moves the drone move_left')
        left_btn.move(40, 110)
        left_btn.clicked.connect(self.move_left)

        cw_btn = QPushButton('&e', self)
        cw_btn.setToolTip('Rotates the drone cw')
        cw_btn.move(160, 40)
        cw_btn.clicked.connect(self.cw)

        ccw_btn = QPushButton('&q', self)
        ccw_btn.setToolTip('Rotates the drone ccw')
        ccw_btn.move(40, 40)
        ccw_btn.clicked.connect(self.ccw)

        increase_alt_btn = QPushButton('&IncreaseAlt', self)
        increase_alt_btn.setToolTip('Increase Altitude')
        increase_alt_btn.move(280, 50)
        increase_alt_btn.clicked.connect(self.increase_alt)

        decrease_alt_btn = QPushButton('De&creaseAlt', self)
        decrease_alt_btn.setToolTip('Decrease Altitude')
        decrease_alt_btn.move(280, 80)
        decrease_alt_btn.clicked.connect(self.decrease_alt)

        takeoff_btn = QPushButton('&Takeoff', self)
        takeoff_btn.setToolTip('Takeoff')
        takeoff_btn.move(280, 150)
        takeoff_btn.clicked.connect(self.takeoff)

        land_btn = QPushButton('&Land', self)
        land_btn.setToolTip('Land')
        land_btn.move(280, 180)
        land_btn.clicked.connect(self.land)

        reset_btn = QPushButton('&Reset', self)
        reset_btn.setToolTip('Reset')
        reset_btn.move(280, 210)
        reset_btn.clicked.connect(self.reset)

        # close_btn = QPushButton('&X Close (use this not the window)', self)
        # close_btn.setToolTip('Reset')
        # close_btn.move(280, 10)
        # close_btn.clicked.connect(self.quit)

        self.show()

    @pyqtSlot(name="forward")
    def forward(self):
        # print(self.drone.navdata)
        self.drone.move(forward=1)
        print("moving drone forward")

    @pyqtSlot(name="backward")
    def backward(self):
        # print(self.drone.navdata)
        self.drone.move(backward=1)
        print("moving drone backward")

    @pyqtSlot(name="right")
    def right(self):
        # print(self.drone.navdata)
        self.drone.move(right=1)
        print("moving drone right")

    @pyqtSlot(name="move_left")
    def move_left(self):
        # print(self.drone.navdata)
        self.drone.move(left=1)
        print("moving drone left")

    @pyqtSlot(name="cw")
    def cw(self):
        # print(self.drone.navdata)
        self.drone.move(cw=1)
        print("rotating clockwise")

    @pyqtSlot(name="ccw")
    def ccw(self):
        # print(self.drone.navdata)
        self.drone.move(ccw=1)
        print("rotating counter-clockwise")

    @pyqtSlot(name="IncreaseAlt")
    def increase_alt(self):
        # print(self.drone.navdata)
        self.drone.move(up=1)
        print("increasing altitude")

    @pyqtSlot(name="DecreaseAlt")
    def decrease_alt(self):
        # print(self.drone.navdata)
        self.drone.move(down=1)
        print("decreasing altitude")

    @pyqtSlot(name="takeoff")
    def takeoff(self):
        # print(self.drone.navdata)
        self.logger = Logger()
        self.begin_log()
        # while not self.drone.state.fly_mask:
        #     self.drone.takeoff()
        print("taking off")

    @pyqtSlot(name="land")
    def land(self):
        # print(self.drone.navdata)
        # while self.drone.state.fly_mask:
        #     self.drone.land()
        self.logger.currently_logging = False
        print("landing")

    @pyqtSlot(name="Reset")
    def reset(self):
        while not self.drone.state.fly_mask:
            self.drone.state.emergency_mask = False
        print("drone reset")

    def begin_log(self):
        "Starts the thread and runs log_data below"
        self.logger.currently_logging = True
        log_thread = Thread(target=self.log_data)
        log_thread.start()

    def log_data(self):
        "Writes data to the CSV every .25 seconds"
        while self.logger.currently_logging:
            self.logger.writer([str(randint(1, 10)) for i in range(8)])
            sleep(.25)

    def closer(self):
        self.close()
        sys.exit(self.exec_)
