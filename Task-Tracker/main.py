import json
import argparse
import os
from datetime import datetime

file_path = "tasks_list.json"
time = datetime.now()
formatted_time = time.strftime('%H:%M %d %B %Y')

def check_file(file_path):
    """To check file exits or not and creates if doe not"""
    try:
        with open(file_path, 'x'):
            return True
    except FileExistsError:
        return False

def add_task(task):
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Getting last id from json file
        last_id = max(item['id'] for item in data) if data else 0
        new_task = {
            'id': last_id + 1,
            'description': task,
            'status': 'todo',
            'createdAt': formatted_time,
            'updatedAt': formatted_time
        }
        data.append(new_task)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
def display_tasks_list(status):
    with open(file_path, 'r') as tasks_file:
        tasks = json.load(tasks_file)
    if status == "all":
        print(json.dumps(tasks, indent=4))
    elif status == "todo":
        print(json.dumps([task for task in tasks if task.get('status')=='todo'],indent=4))
    elif status == "done":
        print(json.dumps([task for task in tasks if task.get('status')=='done'],indent=4))
    elif status == "in-progress":
        print(json.dumps([task for task in tasks if task.get('status')=='in-progress'],indent=4))
    else:
        print("No data with such status exists")
        exit()

def update_task():
    pass

def mark_task():
    pass

def delete_task():
    pass
    
def main():
    #make a parser
    parser = argparse.ArgumentParser(
        prog="Trackio - Your task tracking helper",
        description="App used to track and manage your tasks",
        epilog=""
    )
    parser.add_argument('-a','--add',help='Add a task', required=False)
    parser.add_argument('-ls','--list',help='-l [todo|all|done|in-progress] for sowing tasks', required=False)
    parser.add_argument('-p', '--pick', help='Pick which id you want to look', required=False)
    parser.add_argument('-u', '--update', help='Type new description or something you want', required=False)
    parser.add_argument('-m', '--mark', help='Type "in-progress" or "done"', required=False)
    parser.add_argument('-d', '--delete', help='Delete', required=False)
    
    args = parser.parse_args()
    
    if args.add:
        add_task(args.add)

    elif args.list:
        display_tasks_list(str(args.list))

    elif args.pick:
        if args.update:
            update_task()
        elif args.mark:
            mark_task()
        elif args.delete:
            delete_task()
        else:
            parser.error('For pick, you must specify either --update or --mark')

    else:
        exit()
        
            
if __name__ == '__main__':
    main()