"""
Authors: Fernando Perez & David Reynolds
Date of Creation: April 7, 2022
Event Builder for building events for program
"""
from activity_builder import ActivityBuilder
from event_and_task import Event

class EventBuilder(ActivityBuilder):
    #Override
    def build(self):
        event = Event(self)
        return event
