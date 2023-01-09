from activity_builder import ActivityBuilder
import event_and_task

class makeOrder():
  
   def makeAscendTitle(lst):
       lst2 = lst[:]
       lst2.sort(key=lambda x: x.title)
       return lst2
 
 
   def makeDescendTitle(lst):
       lst2 = lst[:]
       lst2.sort(key=lambda x: x.title, reverse=True)
       return lst2
 
 
   def makeAscendDate(lst):
        lst2 = lst[:]
        for x in lst2:
            splits = []
            for y in x.getDate().split('/'):
                if len(y) <2:
                    splits.append("0"+y)
                else:
                    splits.append(y)
            x.setDate("/".join(splits))
        lst2.sort(key=lambda v: v.date)
        return lst2
 

   def makeDescendDate(lst):
        lst2 = lst[:]
        for x in lst2:
            splits = []
            for y in x.getDate().split('/'):
                if len(y) <2:
                    splits.append("0"+y)
                else:
                    splits.append(y)
            x.setDate("/".join(splits))
        lst2.sort(key=lambda v: v.date, reverse=True)
        return lst2


   def makeAscendTime(lst):
       lst2 = lst[:]
       lst2.sort(key=lambda x: x.time)
       return lst2
 

   def makeDescendTime(lst):
       lst2 = lst[:]
       lst2.sort(key=lambda x: x.time, reverse=True)
       return lst2
 

   def makeDescendPriority(lst):
       urg = []
       important = []
       not_important = []
       should_do = []
       for x in lst:
            priority = x.getPriority().strip()
            if priority == "Urgent":
                urg.append(x)
            elif priority == "Important":
                important.append(x)
            elif priority == "Should do":
                should_do.append(x)
            elif priority == "Unimportant":
                not_important.append(x)
       big_lst = urg + important + should_do + not_important
       return big_lst
 

   def makeAscendPriority(lst):
        urg = []
        important = []
        not_important = []
        should_do = []
        for x in lst:
                priority = x.getPriority().strip()
                if priority == "Urgent":
                    urg.append(x)
                elif priority == "Important":
                    important.append(x)
                elif priority == "Should do":
                    should_do.append(x)
                elif priority == "Unimportant":
                    not_important.append(x)
        big_lst = not_important+should_do+important+urg
        return big_lst


   def search(lst, searchfor):
        lst2 = []
        for x in lst:
            if str(x.getTitle()).strip() == str(searchfor).strip():
                lst2.append(x)
        return lst2


   def eventFilters(lst):
        lst2=lst[:]
        for y in range(len(lst2)):
            for x in lst2:
                if type(x) != event_and_task.Event:
                    lst2.remove(x)
        return(lst2)


   def taskFilters(lst):
        lst2=lst[:]
        for y in range(len(lst2)):
            for x in lst2:
                if type(x) != event_and_task.Task:
                    lst2.remove(x)
        return(lst2)