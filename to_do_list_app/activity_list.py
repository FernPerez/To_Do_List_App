"""
UNUSED, INCLUDED FOR HISTORICAL PURPOSES ONLY

Authors: Jacob Henry
Date of Creation: April 17, 2022
Intended main use is as holder for all events/activities, not using singleton in case of multi user scenario(?)
"""
from activity import Activity
import json

class ActivityList():
    def __init__(self):
        self.actlist = []

    def AddActivity(self, activity):
        """
        Checks for validity and appends to list if object is an activity
        """
        if isinstance(activity, Activity):
            self.actlist.append(activity)
        else:
            print(f"Failed to add {activity.type()} object, expected event or task")

        return self.actlist[-1]

    def getActivity(self, index):
        """
        Returns activity at index in list, works with - indexing
        """
        length = len(self.actlist)
        if (0 <= index < length or -length <= index <= -1):
            return self.actlist[index]
        else:
            print("tried to get activity not in range")
            return self.actlist[0]

    def rmActivity(self, activity):
        """
        removes activity from list
        """
        self.actlist.remove(activity)

    def replaceActivity(self, activity, replacement):
        if activity in self.actlist:
            index = self.actlist.index(activity)
            self.actlist[index] = replacement
        else:
            print("activity not present in list")
            return
        return replacement

    def modActivity(self, activity, props):
        """
        modify activity according to props dictionary
        Currently just an idea, actual implementation should probably
        be inside event/task classes.
        """
        if activity in self.actlist:
            index = self.actlist.index(activity)
        else:
            print("Activity not in list")
            return
        #self.actlist[index].edit(props)

        return self.actlist[index]
        
    def dumpActivities(self, output):
        data = []
        with open(output, "w+") as f:
            for activity in self.actlist:
                fields = activity.getFields()
                data.append(fields)
            
            out=json.dumps(data, indent=2)
            f.write(out)


