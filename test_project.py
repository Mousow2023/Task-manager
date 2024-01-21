import csv
from backup import save_changes, save_tasks, load_tasks, Task

# test_save_changes.py
def test_save_changes(tmp_path):
    test_file = "test_backup.csv"

    # Task list
    task_list = [
        Task("Task1", "Description1", "2023-01-01"),
        Task("Task2", "Description2", "2023-02-02"),
        Task("Task3", "Description3", "2023-03-03")
    ]

    # Save changes
    save_changes(task_list, test_file)

    # Read the content of the saved file
    with open(test_file, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)


    assert rows[0] == ["name", "description", "deadline", "completion_status"]
    assert rows[1:] == [
        ["Task1", "Description1", "2023-01-01", "Not Complete ❌"],
        ["Task2", "Description2", "2023-02-02", "Not Complete ❌"],
        ["Task3", "Description3", "2023-03-03", "Not Complete ❌"]
    ]


def test_load_tasks(tmp_path):
    # Create a temporary file for testing
    test_file = "test_backup.csv"

    # Create a test task list
    task_list = [
        Task("Task1", "Description1", "2023-01-01"),
        Task("Task2", "Description2", "2023-02-02"),
        Task("Task3", "Description3", "2023-03-03")
    ]

    # Save the test task list to the temporary file
    with open(test_file, "w", newline='') as file:
        fieldnames = ["name", "description", "deadline", "completion_status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in task_list:
            writer.writerow(task.dict())

    # Call load_tasks function
    loaded_tasks = load_tasks(test_file)

    # Check if the loaded tasks match the original task list
    assert len(loaded_tasks) == len(task_list)
    for loaded_task, original_task in zip(loaded_tasks, task_list):
        assert loaded_task.name == original_task.name
        assert loaded_task.description == original_task.description
        assert loaded_task.deadline == original_task.deadline
        assert loaded_task.completion_status == original_task.completion_status


# test_save_tasks.py
def test_save_tasks(tmp_path):
    # Create a temporary file for testing
    test_file = "backup.csv"

    # Create an empty file
    open(test_file, 'w').close()

    # Create a test task list
    task_list = [
        Task("Task1", "Description1", "2023-01-01"),
        Task("Task2", "Description2", "2023-02-02"),
        Task("Task3", "Description3", "2023-03-03")
    ]

    # Call save_tasks function
    save_tasks(task_list, test_file)

    # Read the content of the saved file
    with open(test_file, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Check if the header and data were written correctly
    assert rows[0] == ["name", "description", "deadline", "completion_status"]
    assert rows[1:] == [
        ["Task1", "Description1", "2023-01-01", "Not Complete ❌"],
        ["Task2", "Description2", "2023-02-02", "Not Complete ❌"],
        ["Task3", "Description3", "2023-03-03", "Not Complete ❌"]
    ]
