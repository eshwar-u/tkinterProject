'''
This file stores the object for one shift.
Author: Eshwar Umarengan
Date: 12/7/2023
'''
from datetime import datetime, timedelta
class Shift:
    def __init__(self, startTime, endTime, day):
        self.startTime = startTime
        self.endTime = endTime
        #day must be sent in as a letter [m, t, w, th, f, s, sn]
        self.day = day


    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getDay(self):
        return self.day

    def setStartTime(self, startTime):
        self.startTime = startTime

    def setEndTime(self, endTime):
        self.endTime = endTime

    def setDay(self, day):
        self.day = day

    def getShift(self):
        return(self.startTime, self.endTime, self.day)

    def __str__(self):
        return f"({self.startTime}, {self.endTime}, {self.day})"

    def __eq__(self, other):
        return(self.startTime == other.startTime and self.endTime == other.endTime and self.day == other.day)
