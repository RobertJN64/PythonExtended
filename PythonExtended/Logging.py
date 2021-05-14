import time

class LogLevel:
    NONE = 0
    Pretty = 1
    All = 2

class Logger:
    def __init__(self, logLevel, fileLogLevel = None):
        self.logLevel = logLevel

        if fileLogLevel is None:
            self.fileLogLevel = logLevel
        else:
            self.fileLogLevel = fileLogLevel

        self.log = []
        self.starttime = time.time()

    def print(self, text, logLevel):
        if logLevel <= self.logLevel:
            print(text)

        if logLevel <= self.fileLogLevel:
            self.log.append(text + '\n')

    def save(self, fname):
        with open(fname, "w") as f:
            f.writelines(self.log)

    def printTimestamp(self, note=""):
        print(note + str(round(time.time()-self.starttime ,2)) + " seconds.")
