'''
This file stores the object for one shift.
Author: Eshwar Umarengan
Date: 12/7/2023
'''

class Shift:
    def __init__(self, startTime, endTime, day):
        self.startTime = startTime
        self.endTime = endTime
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
        return(self.startTime, self.endTime, self.day)
