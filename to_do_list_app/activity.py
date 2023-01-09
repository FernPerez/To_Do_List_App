"""
Authors: Fernando Perez & David Reynolds
Date of Creation: April 7, 2022
Base Activity Class to be inherited by Event and Task
"""

from datetime import time

class Activity():
    """
    Base Activity Class to be inherited by Event and Task
    """
    def __init__(self, builder):
        self.title = builder.title
        self.description = builder.description
        self.priority = builder.priority
        self.date = builder.date
        self.time = builder.time
        self.index = 0


    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getPriority(self):
        return self.priority

    def getFields(self, type=0):
        """_summary_

        :param type: Type index of what this activity should be saved as. defaults to 0 (Activity)
        :type type: int, optional
        :return: Dictionary containing the attributes of Activity, and an additional key/value contianing its type index
        :rtype: dict
        """
        fields = {}
    
        fields['index'] = self.index
        fields['title'] = self.title
        fields['description'] = self.description
        fields['priority'] = self.priority
        fields['date'] = self.date
        fields['time'] = self.time.isoformat()
        fields['type'] = type

        return fields

    def setPriority(self, newPriority):
        self.priority = newPriority

    def getDate(self):
        return self.date

    def setDate(self, newDate):
        self.date = newDate

    def setTime(self, newTime):
        self.time = newTime

    def getTime(self):
        return self.time

    def getIndex(self):
        return self.index
    
    def setIndex(self, newIndex):
        self.index = newIndex

    def load(self, inDict):
        """_summary_

        :param inDict: Dictionary to load data from
        :type inDict: dict
        :return: activity object with attributes equal to the values of indict
        :rtype: activity
        """
        self.title = inDict['title']
        self.description = inDict['description']
        self.priority = inDict['priority']
        self.date = inDict['date']
        self.index = inDict['index']
        self.time = time.fromisoformat(inDict['time'])
        self.type = inDict['type']

        return self