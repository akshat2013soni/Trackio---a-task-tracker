class Task:
    def __init__(self):
        pass
    
def initial_input():
    return input("What do you need to do today?\n1. Add a task\n2. Update a task\n3. Delete a task\n4. Change task status\n5. List all tasks\n6. List all tasks that are done\n7. List all tasks that are not done\n8. List all tasks that are in progress\n9. Exit\n")

def add_task():
    pass

def update_task():
    pass

def delete_task():
    pass

def change_task_status():
    pass

def list_tasks():
    pass
    
    
def main():
    print("Welcome to Trackio! - Your task tracker")
    task_work = initial_input()
    while not task_work.isnumeric():
        print("Please enter the number corresponding to the task")
        task_work = initial_input()
    task_number = int(task_work)
    if task_number == 1:
        add_task()
    elif task_number == 2:
        update_task()
    elif task_number == 3:
        delete_task()
    elif task_number == 4:
        change_task_status()
    elif task_number == 5:
        list_tasks()
    elif task_number == 6:
        list_tasks()
    elif task_number == 7:
        list_tasks()
    elif task_number == 8:
        list_tasks()
    elif task_number == 9:
        print("Closing")
    else:
        print("Please choose from the list of options!\nMore options to be added soon!")
                
            
if __name__ == '__main__':
    main()