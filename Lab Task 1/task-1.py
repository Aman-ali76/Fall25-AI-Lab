from time import sleep
class TODO:
    def __init__(self):
        self.tasks = {}
        self.marked_tasks = {}

    def add_task(self,task , priority=None):
        """
        parameters:
            task (str): Task to be added
            priority (str,optional): Priority of the task 

        Returns:
            tuple: (bool,str) -> (Success/Failure,Message)

        Add a task to the todo list with an optional priority number if the number is not provided it will assign the next avalible priority number 
        """

        if task not in [i.replace("[ ] ","",1).replace("[✔] ","",1) for i in self.tasks.values()]:
            if priority is not None:
                if priority not in self.tasks.keys():
                    self.tasks[priority] = f"[ ] {task}"
                    return True, f"Task '{task}' added with priority {priority}"
                else:
                    return False, f"Priority {priority} already assigned to task '{self.tasks[priority].replace("[ ] ","",1).replace("[✔] ","",1)}'.\nPlease select another one or leave it empty to assign the next avalible priorty"
                
            else:
                if len(self.tasks) == 0:
                    self.tasks[1] = f"[ ] {task}"
                    return True, f"Task '{task}' added with proiority 1"
                else:
                    next_priority = int(max(self.tasks.keys())) + 1
                    self.tasks[next_priority] = f"[ ] {task}"
                    return True, f"Task '{task}' added with priority {next_priority}"
        else:
            return False, f"Task '{task}' already exists"



    def view_tasks(self):
        """
        Returns:
            tuple: (bool,dict/str) -> (Success/Failure,Tasks Dictionary)

        This will show all the tasks either marked as completed or uncompleted in a sorted order based on their priority numbers
        """
        if len(self.tasks) == 0:
            return False, "No tasks available"
        else:
            merged_tasks = {key: self.marked_tasks.get(key,val) for key,val in self.tasks.items()}
            merged_sorted_tasks = dict(sorted(merged_tasks.items()))
            return True, merged_sorted_tasks
        
    def mark_tasks(self,task=None,priority=None):
        """
        Parameters:
            task (str,optional): Task to be marked as completed
            priority (str,optional): Priority of the task to be marked as completed
        
        Returns:
            tuple: (bool,str) -> (Success/Failure,Message)

        Mark a task as completed either by providing the task name or the priority number one of the parameter is required
        """
        if task is None and priority is None:
            return False, "Please provide task name or priority to mark a task"
        else:
            if task is not None:
                if task in [i.replace("[ ] ","",1).replace("[✔] ","",1) for i in self.tasks.values()]:
                    for key , value in self.tasks.items():
                        if value.replace("[ ] ","",1).replace("[✔] ","",1) == task:
                            self.marked_tasks[key] = f"[✔] {task}"
                            return True, f"Task '{task}' marked as sompleted"
                else:
                    return False, f"Task '{task}' not exist in the list"
            elif priority is not None:
                if priority in self.tasks.keys():
                    self.marked_tasks[priority] = f"[✔] {self.tasks[priority].replace('[ ] ','',1)}"
                    return True, f"Task '{self.tasks[priority].replace('[ ] ','',1)}' marked as sompleted"
                else:
                    return False, f"Priority '{priority}' not exist in the list"
                


    def unmark_tasks(self,task=None,priority=None):
        """
        Parameters:
            task (str,optional): Task to be unmarked as uncompleted
            priority (str,optional): Priority of the task to be unmarked as uncompleted
        
        Returns:
            tuple: (bool,str) -> (Success/Failure,Message)

        Unmark a task as uncompleted either by providing the task name or the priority number one of the parameter is required
        """
        if task is None and priority is None:
            return False, "Please provide task name or priority to mark a task"
        else:
            if task is not None:
                if task in [i.replace("[ ] ","",1).replace("[✔] ","",1) for i in self.marked_tasks.values()]:
                    for key , value in self.marked_tasks.items():
                        if value.replace("[ ] ","",1).replace("[✔] ","",1) == task:
                            del self.marked_tasks[key]
                            return True, f"Task '{task}' marked as uncompleted"
                else:
                    return False, f"Task '{task}' not Marked as completed"
            elif priority is not None:
                if priority in self.marked_tasks.keys():
                    del self.marked_tasks[priority]
                    return True, f"Task '{self.tasks[priority].replace("[ ] ","",1).replace("[✔] ","",1)}' marked as uncompleted"
                else:
                    return False, f"Priority '{priority}' not Marked as completed"

    def delete_task(self,task=None,priority=None):
        """
        Parameters:
            task (str,optional): Task to be removed
            priority (str,optional): Priority of the task to be removed
        
        Returns:
            tuple: (bool,str) -> (Success/Failure,Message)

        Remove a task either by providing the task name or the priority number one of the parameter is required
        """
        if task is None and priority is None:
            return False, "Please provide task name or priority to mark a task"
        else:
            if task is not None:
                if task  in [i.replace("[ ] ","",1).replace("[✔] ","",1) for i in self.tasks.values()]:
                    for key , val in self.tasks.items():
                        if val.replace("[ ] ","",1).replace("[✔] ","",1) == task:
                            del self.tasks[key]
                            if key in self.marked_tasks.keys():
                                del self.marked_tasks[key]
                            return True , f"Task '{task}' deleted successfully"
                else:
                    return False, f"Task '{task}' not exist in the list"
            elif priority is not None:
                if priority in self.tasks.keys():
                    del self.tasks[priority]
                    if priority in self.marked_tasks.keys():
                        del self.marked_tasks[priority]
                    return True , f"Task '{self.tasks.replace("[ ] ","",1).replace("[✔] ","",1)}' deleted successfully"
                else:
                    return False, f"Priority '{priority}' not exist in the list"
                
    
    def clear_all_tasks(self):
        """
        Returns:
            tuple: (bool,str) -> (Success/Failure,Message)

        Clear all the tasks from the todo list
        """
        self.tasks.clear()
        self.marked_tasks.clear()
        return True, "All tasks cleared successfully"

def run():
    todo = TODO()
    choice = ''

    while choice != '7' or choice != '':
        print("---------- TODO Application MENU ----------")
        print("1: Add Task\n2: View Tasks\n3: Mark Task as Completed\n4: Unmark Task as Uncompleted\n5: Delete Task\n6: Clear All Tasks\n7: Exit Application")
        
        choice = input("Enter your choice num (1-7) or press enter to exit : ").strip()

        if choice in ['1','2','3','4','5','6','7','']:
            if choice == '1':
                task = input("\nEnter Task: ").strip()
                priority = input("Enter Priority in numbers only or leave empty by pressing entery key (optional): ").strip()
                try:
                    priority = int(priority) if priority != '' else None
                except :
                    priority = None
                    print("\nPriority should be a number only, it will be assigned automatically")
                
                succcess,msg = todo.add_task(task.lower(),priority)
                print(msg)
                print("------------------------------------------\n")

            elif choice == '2':
                succcess,msg = todo.view_tasks()
                if succcess:
                    print("Sorted Tasks: ")
                    for key,val in msg.items():
                        print(f"{key}: {val}")
                else:
                    print(msg)
                print("------------------------------------------\n")

            elif choice == '3':
                task = input("\nEnter Task to be marked as completed or leave empty by pressing entery key (optional): ").strip()
                priority = input("Enter Priority in numbers only f the task to be marked as completed  or leave empty by pressing entery key (optional): ").strip()   
                task = task.lower() if task != '' else None
                try:
                    priority = int(priority) if priority != '' else None
                except :
                    priority = None
                    print("\nPriority should be a number only, it will be assigned automatically")
                succcess,msg = todo.mark_tasks(task,priority)
                print(msg)
                print("------------------------------------------\n")

            elif choice == '4':
                task = input("\nEnter Task to be unmarked as uncompleted or leave empty by pressing entery key (optional): ").strip()
                priority = input("Enter Priority in numbers only f the task to be unmarked as uncompleted  or leave empty by pressing entery key (optional): ").strip()   
                task = task.lower() if task != '' else None
                try:
                    priority = int(priority) if priority != '' else None
                except :
                    priority = None
                    print("\nPriority should be a number only, it will be assigned automatically")
                
                succcess,msg = todo.unmark_tasks(task,priority)
                print(msg)
                print("------------------------------------------\n")
            
            elif choice == '5':
                task = input("\nEnter Task to be deleted or leave empty by pressing entery key (optional): ").strip()
                priority = input("Enter Priority in numbers only f the task to be deleted  or leave empty by pressing entery key (optional): ").strip()   
                task = task.lower() if task != '' else None
                try:
                    priority = int(priority) if priority != '' else None
                except :
                    priority = None
                    print("\nPriority should be a number only, it will be assigned automatically")
                
                succcess,msg = todo.delete_task(task,priority)
                print(msg)
                print("------------------------------------------\n")

            elif choice == '6':
                print("Are you sure you want to clear all tasks? This action cannot be undone.")
                confirm = input("Type 'yes' to confirm or 'no' to cancel: ").strip().lower()
                if confirm == 'yes':
                    succcess,msg = todo.clear_all_tasks()
                    print(msg)
                    print("------------------------------------------\n")
                else:
                    print("Clear all tasks operation cancelled.")
                    print("------------------------------------------\n")

            elif choice == '7' or choice == '':
                print("Exiting",end='')
                for i in range(4):
                    print("."*1,end='')
                    sleep(0.3)
                break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            print("------------------------------------------\n")
                

        
run()   