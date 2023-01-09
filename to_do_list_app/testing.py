from event_builder import EventBuilder
import event_and_task
event = EventBuilder().setTitle("dog").build()
print(type(event) is not event_and_task.Task)
