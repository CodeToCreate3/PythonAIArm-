# this file demonstrating on the use of the OOP in python
# file name: project_review.py
# author: denhis123
# date: 19/02/2025

# declaring class in python using the keyword as class
class Task1:
    # define the class constructors
    def __init__(self, name_of_task, description, status):
        self.name_of_task = name_of_task
        self.description = description
        self.status = "Not done"
    
    # Function to show the status of the task
    def job_status(self):
        self.job_status = "Done"

    # Function to print the details about the tasks
    # The function to return a string about the task
    def __str__(self):
        return f"Task: {self.name_of_task}\n\t Status: {self.job_status}\n Description: {self.description}"


# end of the class

# Create the data structure 
# List
my_tasks = []
#print(type(my_tasks))

# functions to help control on the list created
def add_task(my_task):
    my_tasks.append(my_task)
    # the object my_task is added in the data structure my_tasks

def remove_task_(task_):
    # using the for loop search through the loop to find on the task to remove
    for my_task in my_tasks: # in the my_tasks list check on every single task
        my_task.name == task_ # check on the task names
        my_tasks.remove(my_task) # from the list remove particular task
        break # action completed

def display_tasks():
    if not my_tasks: # if the my_tasks is empty it should print the message "no tasks to display"
        print("No tasks to display.")
    for my_task in my_tasks: # checks and display every task in the list
        print(f"{my_task}\n")

# create the user interaction screen
# User interaction loop
while True:
    action = input("Do you want to add, remove, display tasks, or quit? (add/remove/display/quit): ").lower()

    if action == "add":
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        task = Task(name, description)
        add_task(task)
        print(f"Task '{name}' added!")

    elif action == "remove":
        task_name = input("Enter task name to remove: ")
        remove_task(task_name)
        print(f"Task '{task_name}' removed!")

    elif action == "display":
        print("Displaying tasks:")
        display_tasks()

    elif action == "quit":
        print("Goodbye!")
        break

