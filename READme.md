# YOUR PROJECT TITLE: TaskMaster: A Python-Based Task Management System
#### Video Demo:  https://youtu.be/gwr-b77_-TE?si=MNgCb4LQ7fMfnyHv
#### Description: TaskMaster is a Python-based task management system designed to help users efficiently organize and track their tasks. This command-line program provides a range of features for task management, including task addition, completion tracking, viewing, completion rate calculation, reminders, and task deletion.

## Features

### Adding Tasks
1. Select option 1 from the menu.
2. Enter task details, including name, description, and deadline in the format (YYYY-MM-DD).
3. Tasks can be added consecutively, and users can choose to add another task or exit.

### Marking Tasks as Completed
1. Choose option 2 from the menu.
2. Select the number of the task you have completed.
3. Tasks marked as completed will have their status updated.

### Viewing All Tasks
Select option 3 to view all tasks in a tabulated format with their details.

### Displaying Completion Rate
Choose option 4 to see the completion rate of tasks as a percentage.

### Setting Reminders
Choose option 5 to view tasks set to expire within a day, serving as a reminder.

### Deleting Tasks
Choose option 6 to delete one or more tasks by selecting their corresponding numbers.

### Exiting the Program
Choose option 7 to exit the program.

## File Storage
Task details are stored in a CSV file (`tasks.csv`) to ensure data persistence across program executions.

## Unit Tests
The project includes unit tests to ensure the correctness of key functions:

- **test_save_changes.py**: Tests the `save_changes` function.
- **test_load_tasks.py**: Tests the `load_tasks` function.
- **test_save_tasks.py**: Tests the `save_tasks` function.

## Getting Started
1. Ensure you have Python installed on your machine.
2. Install the required dependencies: `pip install tabulate`.
3. Run the program by executing the `project.py` file.

Feel free to explore and enhance TaskMaster to suit your task management needs!
