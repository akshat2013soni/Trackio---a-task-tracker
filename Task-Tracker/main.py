import json
import argparse
import os
from datetime import datetime

file_path = "tasks_list.json"
current_time = datetime.now()
formatted_time = current_time.strftime('%H:%M %d %B %Y')

def load_tasks():
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([],file)
        return []
    
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(description):
    tasks = load_tasks()
    task_id = get_next_id(tasks)
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'Pending',
        'createdAt': formatted_time,
        'updatedAt': formatted_time
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")
    
def display_tasks_list():
    pass
            
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = formatted_time
            save_tasks(tasks)
            print(f"The task #{task_id} updated successfully.")
            return
    print(f"The task #{task_id} not found.")

def mark_task(task_id, new_task_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_task_status
            task['updatedAt'] = formatted_time
            save_tasks(tasks)
            print(f"The task #{task_id}'s status updated successfully.")
            return
    print(f"The task #{task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"The task #{task_id} removed successfully.")
            return
    print(f"The task #{task_id} does not exist.")
    
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # List command
    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.add_argument("status", type=str, nargs='?', default=None, help="Status of the tasks to list (optional)")

    # Update command
    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("id", type=int, help="ID of the task to update")
    parser_update.add_argument("description", type=str, help="New description of the task")

    # Mark command
    parser_mark = subparsers.add_parser("mark", help="Mark a task as completed or pending")
    parser_mark.add_argument("id", type=int, help="ID of the task to mark")
    parser_mark.add_argument("status", type=str, choices=["completed", "pending"], help="New status of the task")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    print("Trackio - Your task tracking helper")

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        display_tasks_list(args.status)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "mark":
        mark_task(args.id, args.status.capitalize())
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()