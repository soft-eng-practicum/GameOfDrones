from datetime import date


class Logger:
    "Class to handle writing to the CSV file"
    def __init__(self):
        self.currently_logging = False
        self.file = "output.csv"
        with open(self.file, 'w') as f:
            f.write("Flight log {}\n".format(date.today()))
        self.writer(['time', 'x_vel', 'y_vel', 'z_vel', 'pitch', 'roll', 'yaw', 'altitude'])
        self.time = 0

    def writer(self, info):
        "Writes a single row to the CSV"
        with open(self.file, 'a') as f:
            info = [str(i) for i in info]
            f.write("{}\n".format(",".join(info)))
