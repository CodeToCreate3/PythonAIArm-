class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = "Not Done"
    
    def mark_done(self):
        self.status = "Done"
    
    def __str__(self):
        return f"{self.name} - {self.status}: {self.description}"

tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)

while True:
    action = input("Do you want to add, remove, or display tasks? (add/remove/display/quit): ").lower()
    if action == "add":
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        task = Task(name, description)
        add_task(task)
    elif action == "remove":
        task_name = input("Enter task name to remove: ")
        for task in tasks:
            if task.name == task_name:
                remove_task(task)
                break
    elif action == "display":
        for task in tasks:
            print(task)
    elif action == "quit":
        break
