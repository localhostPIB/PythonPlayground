from src.ms.sp.APIPoint import APIPoint
import schedule
import time


# https://schedule.readthedocs.io/en/stable/examples.html#run-a-job-every-x-minute
class FileScheduler:
    __apiTest = None

    def __init__(self):
        self.__apiTest = APIPoint()
        self.__apiTest.login()
        self.__apiTest.init()

    def scheduleFile(self):
        schedule.every(2).seconds.do(self.__apiTest.iterateJSON)
        schedule.every(5).seconds.do(self.__apiTest.countFiles)
        while True:
            schedule.run_pending()
            time.sleep(1)


fs = FileScheduler()
fs.scheduleFile()
