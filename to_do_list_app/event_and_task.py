"""
Authors: Fernando Perez & David Reynolds
Date of Creation: April 7, 2022
Event and Task Classes that both inherit Activity
"""
from activity import Activity

class Event(Activity):
    def getFields(self):
        """Calls the getFields method that belongs to activity.py,
           but gives argument corresponding to Event typeindex (1)

        :return: "saved" dictionary of existing event object
        :rtype: dict
        """
        return super().getFields(1)


class Task(Activity):
    def getFields(self):
        """Calls the getFields method that belongs to activity.py,
           but gives argument corresponding to Task typeindex (2)

        :return: "saved" dictionary of existing Task object
        :rtype: dict
        """
        return super().getFields(2)