"""
Authors: Jacob Henry
Date of Creation: April 17, 2022
Conflict detector for event/tasks

"""
from activity import Activity

class conflict_detector():
    """
    Class used to detect scheduling conflicts between new activity and existing list of activities.
    """
    def __init__(self):
        pass

    def detect(self, event, activities):
        pass


    def __gendict(self, activities):
        """
        generates disctionary with dates as keys,
        currently unfinished since there's no time attribute for activities yet
        """
        timeframes = {}
        for activity in activities:
            timeframes[activity.getDate] = 0
        return timeframes