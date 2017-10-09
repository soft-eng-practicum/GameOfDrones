from threading import Thread
from time import sleep

import sys

from PyQt5.QtGui import QFont
from pyardrone import ARDrone, at

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
        self.width = 1024
        self.height = 768
        self.initUI()
        self.logger = Logger()
        self.drone = ARDrone(connect=True)
        self.drone.send(at.CONFIG('general:navdata_demo', True))
        font = QFont()
        font.setBold(True)
        font.setPixelSize(18)
        self.setFont(font)
        # self.drone.navdata_ready.wait()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.closer)

        forwards_btn = QPushButton('\u25b2', self)
        forwards_btn.setToolTip('Moves the drone forward')
        forwards_btn.move(100, 0)
        forwards_btn.clicked.connect(self.forward)

        backwards_btn = QPushButton('\u25bc', self)
        backwards_btn.setToolTip('Moves the drone backward')
        backwards_btn.move(100, 690)
        backwards_btn.clicked.connect(self.backward)

        right_btn = QPushButton('\u25b6', self)
        right_btn.setToolTip('Moves the drone right')
        right_btn.move(160, 660)
        right_btn.clicked.connect(self.right)

        left_btn = QPushButton('\u25c0', self)
        left_btn.setToolTip('Moves the drone move_left')
        left_btn.move(40, 660)
        left_btn.clicked.connect(self.move_left)

        cw_btn = QPushButton('\u27f3', self)
        cw_btn.setToolTip('Rotates the drone cw')
        cw_btn.move(160, 590)
        cw_btn.clicked.connect(self.cw)

        ccw_btn = QPushButton('\u27f2', self)
        ccw_btn.setToolTip('Rotates the drone ccw')
        ccw_btn.move(40, 590)
        ccw_btn.clicked.connect(self.ccw)

        increase_alt_btn = QPushButton('\u21a5', self)
        increase_alt_btn.setToolTip('Increase Altitude')
        increase_alt_btn.move(280, 550)
        increase_alt_btn.clicked.connect(self.increase_alt)

        decrease_alt_btn = QPushButton('\u21a7', self)
        decrease_alt_btn.setToolTip('Decrease Altitude')
        decrease_alt_btn.move(280, 580)
        decrease_alt_btn.clicked.connect(self.decrease_alt)

        takeoff_btn = QPushButton('\u21eb', self)
        takeoff_btn.setToolTip('Takeoff')
        takeoff_btn.move(280, 650)
        takeoff_btn.clicked.connect(self.takeoff)

        land_btn = QPushButton('\u2913', self)
        land_btn.setToolTip('Land')
        land_btn.move(280, 680)
        land_btn.clicked.connect(self.land)

        reset_btn = QPushButton('\u238C', self)
        reset_btn.setToolTip('Reset')
        reset_btn.move(280, 710)
        reset_btn.clicked.connect(self.reset)

        # close_btn = QPushButton('&X Close (use this not the window)', self)
        # close_btn.setToolTip('Reset')
        # close_btn.move(280, 10)
        # close_btn.clicked.connect(self.quit)

        self.show()

    @pyqtSlot(name="forward")
    def forward(self):
        self.drone.move(forward=1)
        print("moving drone forward")

    @pyqtSlot(name="backward")
    def backward(self):
        self.drone.move(backward=1)
        print("moving drone backward")

    @pyqtSlot(name="right")
    def right(self):
        self.drone.move(right=1)
        print("moving drone right")

    @pyqtSlot(name="move_left")
    def move_left(self):
        self.drone.move(left=1)
        print("moving drone left")

    @pyqtSlot(name="cw")
    def cw(self):
        self.drone.move(cw=1)
        print("rotating clockwise")

    @pyqtSlot(name="ccw")
    def ccw(self):
        self.drone.move(ccw=1)
        print("rotating counter-clockwise")

    @pyqtSlot(name="IncreaseAlt")
    def increase_alt(self):
        self.drone.move(up=1)
        print("increasing altitude")

    @pyqtSlot(name="DecreaseAlt")
    def decrease_alt(self):
        self.drone.move(down=1)
        print("decreasing altitude")

    @pyqtSlot(name="takeoff")
    def takeoff(self):
        self.logger = Logger()
        self.begin_log()
        while not self.drone.state.fly_mask:
            self.drone.takeoff()
        print("taking off")

    @pyqtSlot(name="land")
    def land(self):
        while self.drone.state.fly_mask:
            self.drone.land()
        self.logger.currently_logging = False
        print("landing")

    @pyqtSlot(name="Reset")
    def reset(self):
        if not self.drone.state.fly_mask:
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
            self.logger.writer([self.logger.time, self.drone.navdata.demo])
            sleep(.25)
            self.logger.time += .25

    def closer(self):
        self.close()
        sys.exit(self.exec_)
