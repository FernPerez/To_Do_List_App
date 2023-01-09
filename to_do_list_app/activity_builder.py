"""
Authors: Fernando Perez & David Reynolds
Date of Creation: April 7, 2022
Builder class inherited by Task Builder and Event Builder
"""
from activity import Activity
from event_and_task import Event, Task

class ActivityBuilder():
    def __init__(self):
        """Attributes to assign to built object,
           
           Types was supposed to work as a sort of option select for what to build,
           but in reality the constructors are evaluated when added to the list,
           instead of when indexed into.
           A better implementation would be a switch statement, or if/else chain. 
        """
        self.title = ""
        self.description = ""
        self.date = ""
        self.priority = ""
        self.time = ""
        self.types = [Activity(self), Event(self), Task(self)]
        

    def setTitle(self, newTitle):
        self.title = newTitle
        return self

    def setDescription(self, newDescription):
        self.description = newDescription
        return self

    def setDate(self, newDate):
        self.date = newDate
        return self

    def setTime(self, newTime):
        self.time = newTime
        return self

    def setPriority(self, newPriority):
        self.priority = newPriority
        return self

    def build(self):
        activity = Activity(self)
        return activity


    def buildfromDict(self, inDict):
        """Builds an object from dumped dictionary, 
           object type is determined by the "type" field
           and the types[] list of the builder.

        :param inDict: input dictionary containing fields corresponding to activity attributes
        :type inDict: dict
        :return: Loaded activity object
        :rtype: activity or subclass of activity
        """
        if "type" in inDict.keys():
            #grabs preconstructed object depending on what type field containsm then load the attributes
            return self.types[inDict['type']].load(inDict)
        else:
            print("could not load, no typing data")

    