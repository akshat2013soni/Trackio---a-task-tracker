class Task:
    def __init__(self):
        pass
    
def initial_input():
    return input("What do you need to do today?\n1. Add a task\n2. Update a task\n3. Delete a task\n4. Change task status\n5. List all tasks\n6. List all tasks that are done\n7. List all tasks that are not done\n8. List all tasks that are in progress\n9. Exit\n")
    
def main():
    print("Welcome to Trackio! - Your task tracker")
    task_work = initial_input()
    print(task_work)

if __name__ == '__main__':
    main()