import json

file_path = "tasks_list.json"
   
def check_file(file_path):
    """To check file exits or not and creates if doe not"""
    try:
        with open(file_path, 'x'):
            pass
    except FileExistsError:
        pass
    
def main():
    """Main function."""
    check_file(file_path)
    print("Welcome to \"Trackio\"! Type \"help\" to see available commands. Type \"exit\" to quit.\n")
    
    while True:
        try:
            user_input = input("trackio >>> ")
        except (KeyboardInterrupt, EOFError):
            print("\nClosing Trackio.")
            break
        
        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if user_input.strip().lower() == "help":
            print("""Available Commands:
                - add <description>
                - delete <id>
                - update <id> "new task description"
                - mark-in-progress
                - mark-done
                - list [all|done|in-progress|todo]
                - exit/quit
                """)
            continue
        
            
if __name__ == '__main__':
    main()