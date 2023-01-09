from activity_builder import ActivityBuilder
from event_builder import EventBuilder
from task_builder import TaskBuilder 
from event_and_task import Event, Task
from sort_search import makeOrder
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar
from tktimepicker import SpinTimePickerModern, SpinTimePickerOld, constants
import threading
import json
from os.path import exists


class MainWindow():
    def __init__(self):
        """
        Sets up window specifications such as size and key bindings,
        loads saved activity_list
        """
        self.save_path = "output.txt"
        self.window = tk.Tk()
        self.window.title("To-Do List App")
        self.window.attributes("-fullscreen", False)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))

        self.activity_list = []
        self.loadActivities(self.save_path)
        self.setUp()
        self.updateList(self.activity_list)

    def toggleFullScreen(self, event):
        """
        Called to enable fullscreen
        """
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        """
        Called to disable fullscreen
        """
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def testDisplay(self):
        """
        Called to display text on window
        """
        for i in range(4):
            self.window.columnconfigure(i, weight=1, minsize=75)
            self.window.rowconfigure(i, weight=1, minsize=50)

            for j in range(0, 3):
                frame = tk.Frame(
                    master=self.window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack(padx=5, pady=5)

    def setUp(self):
        """
        Sets up all labels, buttons, and other tkinter widgets in the window
        """
        self.window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=50)
        self.window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)

        # Title
        titleframe = tk.Frame(master=self.window, borderwidth=1)
        titleframe.grid(row=0, column=0, columnspan=2,  sticky="ew", padx=5, pady=5)
        titleLabel = tk.Label(master=titleframe, text="To Do List App", fg="black")
        titleLabel.config(font=("Arial", 36, "bold"))
        titleLabel.pack()

        #Create Instruction
        createInstrFrame = tk.Frame(master=self.window, borderwidth=1)
        createInstrFrame.place(x=20, y = 80)
        createInstrLabel = tk.Label(master=createInstrFrame, text="Create an Activity", fg="black")
        createInstrLabel.config(font=("Arial", 16))
        createInstrLabel.pack()

        #Event or Task Selector
        OPTIONS = ["Event", "Task"]
        
        eventTaskFrame = tk.Frame(master=self.window, borderwidth=1)
        eventTaskFrame.grid(padx=5, pady=5)
        eventTaskFrame.place(x=20, y=120)

        self.eventTaskVariable = tk.StringVar(eventTaskFrame)
        self.eventTaskVariable.set(OPTIONS[0])

        self.eventTaskMenu = tk.OptionMenu(eventTaskFrame, self.eventTaskVariable, *OPTIONS)
        self.eventTaskMenu.config(bg="RoyalBlue1")
        self.eventTaskMenu.pack()

        #Name Text Field 
        instrLabel1 = tk.Label(self.window, text="*Activity Title", fg="black")
        instrLabel1.place(x=20, y=150)
        nameFrame = tk.Frame(master=self.window, borderwidth=1)
        nameFrame.place(x=20, y=170)
        
        self.nameField = tk.Text(nameFrame, height=1, width=40) 
        self.nameField.pack()

        # Description Field
        instrLabel2 = tk.Label(self.window, text="Description", fg="black")
        instrLabel2.place(x=20, y=200)
        desFrame = tk.Frame(master=self.window, borderwidth=1)
        desFrame.place(x=20, y=220)

        self.desField = tk.Text(desFrame, height=9, width=40)
        self.desField.pack()

        # Importance Selector
        instrLabel3 = tk.Label(self.window, text="Importance", fg="black")
        instrLabel3.place(x=375, y=150)
        IMPORTANCE_OPTIONS = ["Urgent", "Important", "Should do", "Unimportant"]

        importanceFrame = tk.Frame(master=self.window, borderwidth=1)
        #importanceFrame.grid(padx=5, pady= 5)
        importanceFrame.place(x=375, y=170)

        self.impvariable = tk.StringVar(importanceFrame)
        self.impvariable.set(IMPORTANCE_OPTIONS[3])

        self.importanceMenu = tk.OptionMenu(importanceFrame, self.impvariable, *IMPORTANCE_OPTIONS)
        self.importanceMenu.config(bg="RoyalBlue1")
        self.importanceMenu.pack()

        # Time Selector
        instrLabel4 = tk.Label(self.window, text="Time", fg="black")
        instrLabel4.place(x=850, y=150)
        timeFrame = tk.Frame(self.window, borderwidth=1)
        timeFrame.place(x=850, y=175)

        self.time_picker = SpinTimePickerOld(timeFrame)
        self.time_picker.addAll(constants.HOURS24)
        self.time_picker.pack(expand=True, fill="both")

        # Date Selector
        instrLabel5 = tk.Label(self.window, text="Date", fg="black")
        instrLabel5.place(x=550, y=150)
        calendarFrame = tk.Frame(self.window, borderwidth=1)
        calendarFrame.place(x=550, y=170)
        self.cal = Calendar(calendarFrame, selectmode= 'day', year=2022, month= 4, day=15)
        self.cal.pack()

        # Console Label
        consoleFrame = tk.Frame(self.window, borderwidth=1)
        consoleFrame.place(x=950, y=450)
        self.console = tk.Label(consoleFrame, text="", bg="gray80", width=50, anchor="w")
        self.console.pack()

        # Add Button
        self.addFrame = tk.Frame(self.window, borderwidth=1)
        self.addFrame.place(x=1000, y=500)
        self.addButton = tk.Button(self.addFrame, text="Add", bg="spring green", fg="black", width=15, height=2, command=self.addActivity, state='normal')
        self.addButton.pack()

        # Remove Button
        rmFrame = tk.Frame(self.window, borderwidth=1)
        rmFrame.place(x=1150, y=500)
        self.removeButton = tk.Button(rmFrame, text="Remove", bg="red3", fg="black", width=15, height=2, state="disabled")
        self.removeButton.pack()

        # Clear Button
        clearFrame = tk.Frame(self.window, borderwidth=1)
        clearFrame.place(x=1000, y=600)
        self.clearButton = tk.Button(clearFrame, text="Clear Selection", bg="deep sky blue", fg="black", width=15, height=2, state="normal", command= lambda:self.clearAct())
        self.clearButton.pack()

        # Update Button
        updateFrame = tk.Frame(self.window, borderwidth=1)
        updateFrame.place(x=1150, y=600)
        self.updateButton = tk.Button(updateFrame, text="Update", bg="yellow2", fg="black", width=15, height=2, state="disabled")
        self.updateButton.pack()

        # Search Bar
        instrLabel6 = tk.Label(self.window, text="Search", fg="black")
        instrLabel6.place(x=20, y=380)
        searchFrame = tk.Frame(self.window, borderwidth=1)
        searchFrame.place(x=20, y=400)      
        self.searchField = tk.Text(searchFrame, height=1, width=40)
        self.searchField.pack()

        # Search Button
        searchButtonFrame = tk.Frame(self.window, borderwidth=1)
        searchButtonFrame.place(x=350, y=400)   
        self.searchButton = tk.Button(searchButtonFrame, text="Search", bg="RoyalBlue1", fg="black", width=15, height=1, command= lambda: self.searchAct(self.searchField.get("1.0", "end")))
        self.searchButton.pack()
        self.searching = False # Used to determine if sorting should use a title that is being searched for.

        # Sort Menu
        OPTIONS = ["None", "Title", "Date", "Time", "Priority"]
        
        instrLabel7 = tk.Label(self.window, text="Sort", fg="black")
        instrLabel7.place(x=490, y=380)
        SortFrame = tk.Frame(master=self.window, borderwidth=1)
        SortFrame.grid(padx=5, pady=5)
        SortFrame.place(x=490, y=398)

        self.SortVar = tk.StringVar(SortFrame)
        self.SortVar.set(OPTIONS[0])

        self.SortMenu = tk.OptionMenu(SortFrame, self.SortVar, *OPTIONS)
        self.SortMenu.config(bg="RoyalBlue1")
        self.SortMenu.pack()

        # Sort Order Menu
        OPTIONS = ["Ascending", "Descending"]
        
        instrLabel8 = tk.Label(self.window, text="Order", fg="black")
        instrLabel8.place(x=575, y=380)
        OrderFrame = tk.Frame(master=self.window, borderwidth=1)
        OrderFrame.grid(padx=5, pady=5)
        OrderFrame.place(x=575, y=398)

        self.OrderVar = tk.StringVar(OrderFrame)
        self.OrderVar.set(OPTIONS[0])

        self.OrderMenu = tk.OptionMenu(OrderFrame, self.OrderVar, *OPTIONS)
        self.OrderMenu.config(bg="RoyalBlue1")
        self.OrderMenu.pack()

        # Filter Menu
        OPTIONS = ["All", "Events", "Tasks"]

        instrLabel9 = tk.Label(self.window, text="Filter", fg="black")
        instrLabel9.place(x=700, y=380)
        filterFrame = tk.Frame(master=self.window, borderwidth=1)
        filterFrame.grid(padx=5, pady=5)
        filterFrame.place(x=700, y=398)

        self.filterVar = tk.StringVar(filterFrame)
        self.filterVar.set(OPTIONS[0])

        self.filterMenu = tk.OptionMenu(filterFrame, self.filterVar, *OPTIONS)
        self.filterMenu.config(bg="RoyalBlue1")
        self.filterMenu.pack()

        # Sort Button
        searchButtonFrame = tk.Frame(self.window, borderwidth=1)
        searchButtonFrame.place(x=825, y=400)   
        self.searchButton = tk.Button(searchButtonFrame, text="Sort", bg="RoyalBlue1", fg="black", width=15, height=1, command= lambda: self.sortAct())
        self.searchButton.pack()

        # Activity list
        self.listMainFrame = tk.Frame(self.window, borderwidth=1)
        self.listMainFrame.place(x=20, y=450)
        self.listCanvas = tk.Canvas(self.listMainFrame, bg="white", width=890)
        self.listCanvas.grid(row=1, column=0)

        self.listFrame = tk.Frame(self.listCanvas, borderwidth=1, height=15)
        self.listCanvas.create_window((10,10), window=self.listFrame, anchor="nw", tags="self.listFrame")
        self.listFrame.grid_rowconfigure(1, weight=1)
        self.listFrame.grid_columnconfigure(1, weight=1)
        self.listFrame.bind("<Configure>", self.OnFrameConfigure)

        self.scroll = tk.Scrollbar(self.listMainFrame, command=self.listCanvas.yview)      
        self.scroll.grid(row=1, column=1, rowspan=15, sticky="ns")
        self.listCanvas.configure(yscrollcommand=self.scroll.set)
        
        headerRowFrame = tk.Frame(self.window, borderwidth=1)
        headerRowFrame.place(x=24, y=435)

        tableEntry = tk.Entry(headerRowFrame, bg="grey", width=40)
        tableEntry.grid(row=0, column=0)
        tableEntry.insert(tk.END, "Activity")

        tableEntry = tk.Entry(headerRowFrame, bg="grey", width=5)
        tableEntry.grid(row=0, column=1)
        tableEntry.insert(tk.END, "Type")

        tableEntry = tk.Entry(headerRowFrame, bg="grey", width=40)
        tableEntry.grid(row=0, column=3)
        tableEntry.insert(tk.END, "Date")

        tableEntry = tk.Entry(headerRowFrame, bg="grey", width=40)
        tableEntry.grid(row=0, column=4)
        tableEntry.insert(tk.END, "Time")

        tableEntry = tk.Entry(headerRowFrame, bg="grey", width=20)
        tableEntry.grid(row=0, column=5)
        tableEntry.insert(tk.END, "Priotity")

        self.listCanvas.configure(scrollregion=self.listCanvas.bbox("all"))

    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.listCanvas.configure(scrollregion=self.listCanvas.bbox("all"))


    def addActivity(self):
        """
        Adds an activity to the backend activity list before updating the list in the window.
        """
        self.clearSearch()
        act_type = self.eventTaskVariable.get()
        if len(self.nameField.get("1.0", "end")) > 1:
            act_name = self.nameField.get("1.0", "end").strip()
            self.nameField.delete(1.0, "end")
        else:
            self.console.configure(text="Must enter name")
            return
        act_description = self.desField.get("1.0", "end").strip()
        self.desField.delete(1.0, "end")
        act_importance = self.impvariable.get()
        act_date = self.cal.get_date()
        time = str(self.time_picker.hours24()) + ":" + str(self.time_picker.minutes())
        act_time = datetime.strptime(time, '%H:%M')
        act_time = act_time.time()

        if str(act_type) == "Event":
            # print("Creating event...")
            activity = EventBuilder().setTitle(act_name).setDescription(act_description).setPriority(act_importance).setDate(act_date).setTime(act_time).build()
        elif str(act_type) == "Task":
            # print("Creating task")
            activity = TaskBuilder().setTitle(act_name).setDescription(act_description).setPriority(act_importance).setDate(act_date).setTime(act_time).build()

        self.activity_list.append((activity))
        self.updateList(self.activity_list)
        
    
    def updateList(self, act_list):
        """
        Clears the list on display and displays a new list with the updated activity_list.

        Autosaves/dumps after updating
        """
        i = 1
        for activity in act_list:
            if type(activity) == Event:
                actType = "E"
            elif type(activity) == Task:
                actType = "T"
            i += 1
            if act_list == self.activity_list:
                activity.setIndex(i-2)
            tableEntry = tk.Entry(self.listFrame, bg="white", width=40)
            tableEntry.grid(row=i, column=1)
            tableEntry.insert(tk.END, activity.getTitle())
            tableEntry.bind("<1>", lambda event, return_activity=activity:
                self.displayAct(return_activity))

            tableEntry = tk.Entry(self.listFrame, bg="white", width=5)
            tableEntry.grid(row=i, column=2)
            tableEntry.insert(tk.END, actType)

            tableEntry = tk.Entry(self.listFrame, bg="white", width=40)
            tableEntry.grid(row=i, column=3)
            tableEntry.insert(tk.END, activity.getDate())

            tableEntry = tk.Entry(self.listFrame, bg="white", width=40)
            tableEntry.grid(row=i, column=4)
            tableEntry.insert(tk.END, str(activity.getTime())[0:5])

            tableEntry = tk.Entry(self.listFrame, bg="white", width=20)
            tableEntry.grid(row=i, column=5)
            tableEntry.insert(tk.END, activity.getPriority())

            # self.scroll = tk.Scrollbar(self.listFrame)
            # self.scroll.grid(row=0, column=6, sticky="ns")
            self.listCanvas.configure(scrollregion=self.listCanvas.bbox("all"))

        self.dumpActivities(self.save_path)

    def displayAct(self, return_activity):
        """
        When an activity in the list is selected, displays its information in the top of the screen, while also
        disabling and enabling some buttons
        """
        self.addButton.config(state='disabled')
        self.removeButton.config(state="normal", command= lambda: self.removeAct(return_activity.getIndex()))
        # self.clearButton.config(state="normal", command= lambda:self.clearAct())
        self.updateButton.config(state="normal", command= lambda:self.updateAct(return_activity.getIndex()))
        self.nameField.delete(1.0, "end")
        self.nameField.insert(1.0, return_activity.getTitle())
        self.desField.delete(1.0, "end")
        self.desField.insert(1.0, return_activity.getDescription())
        self.cal.selection_set(return_activity.getDate())
        self.cal.pack()

    def clearAct(self):
        """
        Action called by clear button in order to unselect an entry from the list.
        """
        self.clearSearch()
        self.nameField.delete(1.0, "end")
        self.desField.delete(1.0, "end")
        self.addButton.config(state="normal")
        self.removeButton.config(state="disabled")
        # self.clearButton.config(state="disabled")
        self.updateButton.config(state="disabled")
        self.console.configure(text="")
        for widgets in self.listFrame.winfo_children():
            widgets.destroy()
        self.updateList(self.activity_list)

    def removeAct(self, actIndex):
        """
        Action called by remove button which removes the selected activity from the list,
        and updates the display
        Param:
            actIndex: int, the index of the activity in activity_list.
        """     
        self.nameField.delete(1.0, "end")
        self.desField.delete(1.0, "end")
        self.addButton.config(state='normal')       
        self.removeButton.config(state="disabled")
        self.clearSearch()
        self.updateButton.config(state="disabled")
        del self.activity_list[actIndex]
        for widgets in self.listFrame.winfo_children():
            widgets.destroy()
        self.updateList(self.activity_list)   

    def updateAct(self, actIndex):
        """
        Called by update button that updates an activity by deleting it and creating a new
        one with the new parameters
        Parameters:
            actIndex: int, the index of the activity in activity_list.
        """
        self.addActivity()
        self.clearSearch()
        self.nameField.delete(1.0, "end")
        self.desField.delete(1.0, "end")
        self.addButton.config(state='normal')       
        self.removeButton.config(state="disabled")
        # self.clearButton.config(state="disabled")
        self.updateButton.config(state="disabled")
        del self.activity_list[actIndex]
        for widgets in self.listFrame.winfo_children():
            widgets.destroy()
        self.updateList(self.activity_list)

    def searchAct(self, searchfor):
        """
        Called by search button to search the list and update list.
        parameters:
            searchfor: str, title to search for
        """
        self.searching = True
        for widgets in self.listFrame.winfo_children():
            widgets.destroy()
        self.searchList = makeOrder.search(self.activity_list, searchfor)
        if len(self.searchList) == 0:
            self.console.configure(text="No matching entries")
        self.updateList(self.searchList)
        return

    def sortAct(self):
        """
        Called by sort button to sort list given a specific paramater from the dropdown menu
        """
        sortby = self.SortVar.get()
        order = self.OrderVar.get()
        filterby = self.filterVar.get()
        if sortby != "None" or filterby != "All":
            for widgets in self.listFrame.winfo_children():
                widgets.destroy()

        if self.searching == True:
            unfiltered_act_list = self.searchList
        else:
            unfiltered_act_list = self.activity_list
        act_list = self.filterActs(unfiltered_act_list)

        if sortby == "None":
            self.sortList = act_list
        elif sortby == "Title":
            if order == "Ascending":
                self.sortList = makeOrder.makeAscendTitle(act_list)
            else:
                self.sortList = makeOrder.makeDescendTitle(act_list)
        elif sortby == "Date":
            if order == "Ascending":
                self.sortList = makeOrder.makeAscendDate(act_list)
            else:
                self.sortList = makeOrder.makeDescendDate(act_list)
        elif sortby == "Time":
            if order == "Ascending":
                self.sortList = makeOrder.makeAscendTime(act_list)
            else:
                self.sortList = makeOrder.makeDescendTime(act_list)
        elif sortby == "Priority":
            if order == "Ascending":
                self.sortList = makeOrder.makeAscendPriority(act_list)
            else:
                self.sortList = makeOrder.makeDescendPriority(act_list)
        self.updateList(self.sortList)  

    def filterActs(self, act_list):
        """
        Takes a list of activities and returns a new list filtered by the specified activity type
        """
        if self.filterVar.get() == "All":
            return act_list
        elif self.filterVar.get() == "Events":
            return makeOrder.eventFilters(act_list)
        else:
            return makeOrder.taskFilters(act_list)
    
    def clearSearch(self):
        """
        Resets searching vars and empties search field
        """
        self.searching = False
        self.searchField.delete(1.0, "end")

    def dumpActivities(self, output):
        """Serialize the current activity_list to json format
           and send it to output file

        :param output: name of output file
        :type output: String
        """
        data = []
        with open(output, "w+") as f:
            for activity in self.activity_list:
                fields = activity.getFields()
                data.append(fields)
            out=json.dumps(data, indent=2)
            f.write(out)


    def loadActivities(self, input):
        """Appends items to activity_list from file created using dumpActivities

        :param input: name of input file
        :type input: String
        """
        if (exists(input)):
            with open(input, "r") as f:
                data = json.load(f)
            for item in data:
                builder = ActivityBuilder()
                self.activity_list.append(builder.buildfromDict(item))
        else:
            pass
       # for item in self.activity_list:
         #   print(item.getFields())
    
def mainloop():
    mainWindow = MainWindow()
    mainWindow.window.mainloop()
    mainWindow.testDisplay

if __name__ == "__main__":
    mainThread = threading.Thread(target=mainloop)
    mainThread.start()
    print("all good")
        