from tabulate import tabulate
import sys
import csv
import os
from datetime import date, datetime

# Class representing a Task
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self._deadline = deadline
        self.completion_status = "Not Complete ❌"

    def __str__(self):
        return str(self.dict())

    def dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "deadline": str(self._deadline),
            "completion_status":  self.completion_status 
        }
    
    def to_tuple(self):
        return (
            self.name,
            self.description,
            self._deadline,
            self.completion_status,
        )

    def reminder(self):
        date_string = datetime.strptime(self._deadline, "%Y-%m-%d").date()
        left = date_string - datetime.now().date()
        return True if left.days < 1 and self.completion_status == "Not Complete ❌" else False

    @classmethod
    def get(cls):
        name = input("Task: ")
        description = input("Description: ")
        deadline = input("Deadline(YYYY-MM-DD): ")

        task = cls(name, description, None)
        task.deadline = deadline

        return task

    def mark_as_completed(self):
        self.completion_status = "Completed ✅"

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        try:
            year, month, day = map(int, deadline.split("-"))
            self._deadline = date(year, month, day)
        except ValueError:
            sys.exit("Invalid date format. Please use (YYYY-MM-DD) format.")

# File to save tasks permanently
FILE = "backup.csv"

# Main program
def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Tasks as Completed")
        print("3. View All the Tasks")
        print("4. Display Completion Rate")
        print("5. View Reminder")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("Enter your choice ")
        # Handle the user choices
        match choice:
            case "1": # Add task:
                tasks = add()
                save_tasks(tasks, FILE)

            case "2": # Mark As Completed
                loaded = load_tasks(FILE)
                new_tasks = complete(loaded)
                save_changes(new_tasks, FILE)

            case "3": # View
                saved_tasks = [task.dict() for task in load_tasks(FILE)]

                print(tabulate(saved_tasks, headers="keys", tablefmt="fancy_grid"))


            case "4": # Calculate and display the completion rate
                completed_tasks = 0
                total_tasks = load_tasks(FILE)

                for task in total_tasks:
                    if task.completion_status == "Completed ✅":
                        completed_tasks += 1
                
                
                completion_rate = (completed_tasks / len(total_tasks)) * 100
                print(f"Completion Rate: {completion_rate:.2f}%")

            case "5": # Set reminder for expiring tasks
                reminder_list = []

                for task in load_tasks(FILE):
                    if task.reminder() == True:
                        reminder_list.append(task.dict())

                if len(reminder_list) == 0:
                    print("No task remindered")
                    break

                print("\nThe following task(s) expire within a day")
                print(tabulate(reminder_list, headers="keys", tablefmt="fancy_grid"))

            case "6": # Delete one or more tasks
                left_tasks = delete_task(load_tasks(FILE))
                save_changes(left_tasks, FILE)

            case "7": # Exit the program
                sys.exit()

            case _:
                sys.exit("Invalid Command. Please choose a number between 1 and 6")


def add():
    tasks_list = []
    while True:
        task = Task.get()
        tasks_list.append(task)
        print("Task added successfully!\n")

        another_task = input("Do you wanna add another task? (Yes/No) ").lower()

        if another_task != "yes":
            break
    
    return tasks_list


def complete(tasks):
    while True:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.name}")

        try:
            number = int(input("Choose the number of the task you have you completed: "))
            if 0 < number < len(tasks) + 1:
                if tasks[number - 1].completion_status != "Completed ✅":
                    tasks[number - 1].mark_as_completed()
                    print("Completion Saved successfully!")
                else:
                    print("Already completed")

        except ValueError:
            print("Invalid number of task")

        another = input("Have you completed another task? (Yes/No) ").lower()
        if another != "yes":
            break

    return tasks


def delete_task(task_list):
    while True:
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task.name}")

        try:
            number = int(input("The number of the task you would like to delete: "))
            if 0 < number < len(task_list) + 1:
                del task_list[number - 1]
                print("Task deleted successfully!")
            else:
                print("Invalid number")
        except ValueError:
            raise ValueError("The number of task must be an integer.")

        another = input("Would you like to dalete another task? (Yes/No) ").lower()
        if another != "yes":
            break
        i += 1
    return task_list


def save_tasks(tasks_list, file_path):
    is_empty = os.path.getsize(file_path) == 0

    with open(file_path, "a", newline='') as file:
        fieldnames = ["name", "description", "deadline", "completion_status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if is_empty:
            writer.writeheader()
        for task in tasks_list:
            writer.writerow(task.dict())


def load_tasks(file_path):
    tasks = []
    with open(file_path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            task = Task(row["name"], row["description"], row["deadline"])
            task.completion_status = row["completion_status"]
            tasks.append(task)

    return tasks


def save_changes(list, file_path):
    with open(file_path, "w", newline='') as file:
        fieldnames = ["name", "description", "deadline", "completion_status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for task in list:
            writer.writerow(task.dict())


if __name__ == "__main__":
    main()