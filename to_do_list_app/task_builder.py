"""
Authors: Fernando Perez & David Reynolds
Date of Creation: April 7, 2022
Task Builder for building tasks for program
"""
from activity_builder import ActivityBuilder
from event_and_task import Task

class TaskBuilder(ActivityBuilder):
    #Override
    def build(self):
        task = Task(self)
        return task
