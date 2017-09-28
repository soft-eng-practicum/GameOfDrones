from datetime import date
from time import sleep


class Logger:
    "Class to handle writing to the CSV file"

    def __init__(self):
        self.currently_logging = False
        self.file = "output.csv"
        with open(self.file, 'w') as f:
            f.write("Flight log {}\n".format(date.today()))
        self.writer(['time', 'x_vel', 'y_vel', 'z_vel', 'pitch', 'roll', 'yaw', 'altitude'])

    def writer(self, info):
        "Writes a single row to the CSV"
        with open(self.file, 'a') as f:
            f.write("{}\n".format(",".join(info)))

    def constant_write(self):
        "This won't be necessary when the navdata is working - just for testing purposes"
        for i in range(10):
            self.writer(['a', 'b', 'c'])
            sleep(1)
