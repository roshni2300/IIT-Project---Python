import os 

# Path to the file where tasks will be stored
TASKS_FILE = "tasks.txt"


def load_tasks():
    """Loads tasks from the tasks file."""
    if not os.path.exists(TASKS_FILE):  # Check if the file exists
        return []  # If the file does not exist, return an empty list of tasks
    with open(TASKS_FILE, "r") as file:
        tasks = file.readlines()  # Read all lines from the file
    tasks = [task.strip() for task in tasks]  # Remove newline characters and any extra spaces
    return tasks


def save_tasks(tasks):
    """Saves the current list of tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")  # Write each task back to the file with a newline


def add_task():
    """Adds a new task to the to-do list."""
    description = input("Enter task description: ")  # Get task description from user
    deadline = input("Enter deadline (YYYY-MM-DD): ")  # Get task deadline from user
    task_id = len(load_tasks()) + 1  # Generate a new task ID based on the number of tasks in the list
    task = f"{task_id},{description},{deadline},Pending"  # Create the new task string
    tasks = load_tasks()  # Load current tasks from file
    tasks.append(task)  # Add the new task to the list
    save_tasks(tasks)  # Save the updated task list back to the file
    print("Task added successfully!")  # Confirm the task was added
    print("(Task saved to tasks.txt)")


def view_tasks():
    """Displays all tasks in the to-do list."""
    tasks = load_tasks()  # Load all tasks from the file
    print("\nTo-Do List:")

    # Split tasks into pending and completed based on their status
    pending_tasks = [task for task in tasks if "Pending" in task]
    completed_tasks = [task for task in tasks if "Completed" in task]

    if pending_tasks:
        print("[Pending]")  # Print the pending section header
        for task in pending_tasks:
            task_id, description, deadline, _ = task.split(",", 3)  # Extract task info
            print(f"{task_id}. {description} - Deadline: {deadline}")  # Print each pending task
    else:
        print("[Pending] No tasks pending.")  # If no pending tasks, display a message

    if completed_tasks:
        print("\n[Completed]")  # Print the completed section header
        for task in completed_tasks:
            task_id, description, deadline, _ = task.split(",", 3)  # Extract task info
            print(f"{task_id}. {description} - Deadline: {deadline}")  # Print each completed task
    else:
        print("[Completed] No tasks completed yet.")  # If no completed tasks, display a message


def mark_completed():
    """Marks a task as completed."""
    task_number = int(input("Enter task number to mark as completed: "))  # Get the task number from user
    tasks = load_tasks()  # Load all tasks from the file
    for i, task in enumerate(tasks):  # Iterate over tasks to find the one with the given task number
        task_id, description, deadline, status = task.split(",", 3)  # Extract task details
        if int(task_id) == task_number:  # If task ID matches the entered task number
            tasks[i] = f"{task_id},{description},{deadline},Completed"  # Mark the task as completed
            save_tasks(tasks)  # Save the updated task list
            print("Task marked as completed!")  # Confirm the update
            print("(Task status updated in tasks.txt)")
            return  # Exit the function after updating the task
    print(f"No task found with ID {task_number}.")  # If no task is found with the given task number


def delete_task():
    """Deletes a task from the to-do list."""
    task_number = int(input("Enter task number to delete: "))  # Get task number to delete
    tasks = load_tasks()  # Load all tasks from the file
    tasks = [task for task in tasks if not task.startswith(f"{task_number},")]  # Filter out the task to delete
    save_tasks(tasks)  # Save the updated task list
    print(f"Task {task_number} deleted successfully!")  # Confirm task deletion


def edit_task():
    """Edits a task description, deadline, or marks it as completed."""
    task_number = int(input("Enter task number to edit: "))  # Get task number to edit
    tasks = load_tasks()  # Load all tasks from the file

    task_found = False  # Flag to check if the task was found
    for i, task in enumerate(tasks):
        task_id, description, deadline, status = task.split(",", 3)  # Extract task details
        if int(task_id) == task_number:  # If task ID matches the entered task number
            task_found = True
            print(f"\nCurrent Task: {description} - Deadline: {deadline} - Status: {status}")
            print("What would you like to do?")
            print("1. Edit description or deadline")
            print("2. Mark as Completed")
            choice = input("Enter your choice: ")  # Get user's choice to edit or mark as completed

            if choice == "1":
                # Edit the description or deadline
                new_description = input("Enter new description: ")
                new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
                tasks[i] = f"{task_id},{new_description},{new_deadline},{status}"  # Update task details
                save_tasks(tasks)  # Save updated task list
                print("Task updated successfully!")
                break
            elif choice == "2":
                # Mark as Completed
                if status == "Completed":
                    print("This task is already marked as completed.")  # If already completed, show a message
                else:
                    tasks[i] = f"{task_id},{description},{deadline},Completed"  # Mark task as completed
                    save_tasks(tasks)  # Save updated task list
                    print("Task marked as completed!")
                break
            else:
                print("Invalid choice. Returning to main menu.")  # Handle invalid input
                break

    if not task_found:
        print(f"No task found with ID {task_number}.")  # If no task matches the entered task number


def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        # Display the main menu options
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")  # Get user's menu choice

        if choice == "1":
            add_task()  # Call add_task function to add a new task
        elif choice == "2":
            view_tasks()  # Call view_tasks function to display all tasks
        elif choice == "3":
            edit_task()  # Call edit_task function to edit an existing task
        elif choice == "4":
            delete_task()  # Call delete_task function to remove a task
        elif choice == "5":
            print("Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


if __name__ == "__main__":
    main_menu()  # Call the main menu function to start the program
