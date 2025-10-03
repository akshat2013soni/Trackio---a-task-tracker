# Trackio

Trackio is a task tracker project used to track and manage your tasks.
It is a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.

Each task has the following properties:

id: A unique identifier for the task

description: A short description of the task

status: The status of the task (todo, in-progress, done)

createdAt: The date and time when the task was created

updatedAt: The date and time when the task was last updated
## Usage

```python

# add task with description 'Clean my room'
python trackio.py add "Clean my room" 

# lists all the tasks
python trackio.py list

# lists all the tasks with 'Pending' status
python trackio.py list Pending

# lists all the tasks with 'Completed' status
python trackio.py list Completed

# mark the task <id> with 'Pending' or 'Completed' status
python trackio.py mark <id> [completed|pending]

# update the task <id> description
python trackio.py update 5 "Clean my bathroom"

# delete the task <id>
python trackio.py delete 5
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
