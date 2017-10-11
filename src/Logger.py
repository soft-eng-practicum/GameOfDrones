import shutil
from datetime import datetime

import os


class Logger:
    "Class to handle writing to the CSV file"
    def __init__(self):
        self.currently_logging = False
        self.file = "output.csv"
        with open(self.file, 'w') as f:
            f.write("Flight log {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.writer(['time', 'x_vel', 'y_vel', 'z_vel', 'pitch', 'roll', 'yaw', 'altitude'])
        self.time = 0

    def writer(self, info):
        "Writes a single row to the CSV"
        with open(self.file, 'a') as f:
            info = [str(i) for i in info]
            f.write("{}\n".format(",".join(info)))

    def saveFile(self):
        print("Save initiated")
        if os.path.isfile("output.csv"):
            shutil.copy("output.csv", "Flight log {}.csv".format(datetime.now().strftime('%Y-%m-%d %H-%M')))
            os.remove("output.csv")
            print("Save successful")
        else:
            print("No data to save - fly the drone again")