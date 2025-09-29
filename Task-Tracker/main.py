import json
import argparse
import os
from datetime import datetime

file_path = "tasks_list.json"
   
def check_file(file_path):
    """To check file exits or not and creates if doe not"""
    try:
        with open(file_path, 'x'):
            pass
    except FileExistsError:
        pass

def add_task():
    pass
    
def display_tasks_list():
    pass

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
    parser.add_argument('-u', '--update', help='Type new description or something you want', required=False)
    parser.add_argument('-m', '--mark', help='Type "in-progress" or "done"', required=False)
    parser.add_argument('-d', '--delete', help='Delete', required=False)
    
    args = parser.parse_args()
    check_file(file_path)
    if args.add:
        add_task()

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