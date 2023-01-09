from event_and_task import Event, Task
from event_builder import EventBuilder
from task_builder import TaskBuilder

class CLIActivityBuilder():

    activityList = []

    def main():
        print("Welcome to the To Do List App!")
        response = ''
        
        while response.upper() != 'X':
            response = input("Would you like to create a [T]ask or [E]vent? ")
            if response.upper() == 'T':
                CLIActivityBuilder.createActivity("task")
            elif response.upper() == 'E':
                CLIActivityBuilder.createActivity("event")
            elif response.upper() == 'X':
                break
            else:
                print("Not valid option")
        
    def createActivity(activity):
        name = input("Give " + activity + " name: ")
        description = input("Description: ")
        importance = input("Importance ([U]rgent, [I]mportant, [N]onimportant: ")
        date = input("Date (MM/DD/YYYY): ")
        if activity == "task":
            activity = TaskBuilder().setTitle(name).setDescription(description).setPriority(importance).setDate(date).build()
        elif activity == "event":
            activity = EventBuilder().setTitle(name).setDescription(description).setPriority(importance).setDate(date).build()
        CLIActivityBuilder.addActivity(activity)
    
    def addActivity(activity):
        print(activity.getTitle())
        print(activity.getDescription())
        print(activity.getPriority())
        print(activity.getDate())

        response = input("Add this " + str(type(activity)) + "to list? ")
        CLIActivityBuilder.activityList.append(activity)


if __name__ == "__main__":
    CLIActivityBuilder.main()