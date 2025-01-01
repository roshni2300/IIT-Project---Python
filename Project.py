import os

# Path to the file where tasks will be stored
TASKS_FILE = "tasks.txt"


def load_tasks():
    """Loads tasks from the tasks file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = file.readlines()
    tasks = [task.strip() for task in tasks]  # Remove newline characters
    return tasks


def save_tasks(tasks):
    """Saves the current list of tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task():
    """Adds a new task to the to-do list."""
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = len(load_tasks()) + 1  # Generate task ID
    task = f"{task_id},{description},{deadline},Pending"
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")
    print("(Task saved to tasks.txt)")


def view_tasks():
    """Displays all tasks in the to-do list."""
    tasks = load_tasks()
    print("\nTo-Do List:")
    pending_tasks = [task for task in tasks if "Pending" in task]
    completed_tasks = [task for task in tasks if "Completed" in task]

    if pending_tasks:
        print("[Pending]")
        for task in pending_tasks:
            task_id, description, deadline, _ = task.split(",", 3)
            print(f"{task_id}. {description} - Deadline: {deadline}")
    else:
        print("[Pending] No tasks pending.")

    if completed_tasks:
        print("\n[Completed]")
        for task in completed_tasks:
            task_id, description, deadline, _ = task.split(",", 3)
            print(f"{task_id}. {description} - Deadline: {deadline}")
    else:
        print("[Completed] No tasks completed yet.")


def mark_completed():
    """Marks a task as completed."""
    task_number = int(input("Enter task number to mark as completed: "))
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        task_id, description, deadline, status = task.split(",", 3)
        if int(task_id) == task_number:
            tasks[i] = f"{task_id},{description},{deadline},Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            print("(Task status updated in tasks.txt)")
            return
    print(f"No task found with ID {task_number}.")


def delete_task():
    """Deletes a task from the to-do list."""
    task_number = int(input("Enter task number to delete: "))
    tasks = load_tasks()
    tasks = [task for task in tasks if not task.startswith(f"{task_number},")]
    save_tasks(tasks)
    print(f"Task {task_number} deleted successfully!")


def edit_task():
    """Edits a task description, deadline, or marks it as completed."""
    task_number = int(input("Enter task number to edit: "))
    tasks = load_tasks()

    task_found = False
    for i, task in enumerate(tasks):
        task_id, description, deadline, status = task.split(",", 3)
        if int(task_id) == task_number:
            task_found = True
            print(f"\nCurrent Task: {description} - Deadline: {deadline} - Status: {status}")
            print("What would you like to do?")
            print("1. Edit description or deadline")
            print("2. Mark as Completed")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Edit the description or deadline
                new_description = input("Enter new description: ")
                new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
                tasks[i] = f"{task_id},{new_description},{new_deadline},{status}"
                save_tasks(tasks)
                print("Task updated successfully!")
                break
            elif choice == "2":
                # Mark as Completed
                if status == "Completed":
                    print("This task is already marked as completed.")
                else:
                    tasks[i] = f"{task_id},{description},{deadline},Completed"
                    save_tasks(tasks)
                    print("Task marked as completed!")
                break
            else:
                print("Invalid choice. Returning to main menu.")
                break

    if not task_found:
        print(f"No task found with ID {task_number}.")


def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()  # Calls the edit task function
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
