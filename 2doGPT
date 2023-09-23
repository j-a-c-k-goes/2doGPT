import os

# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to mark a task as completed
def complete_task(todo_list, index):
    if 1 <= index <= len(todo_list):
        completed_task = todo_list.pop(index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index. Please try again.")

# Main program loop
if __name__ == "__main__":
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            display_todo_list(todo_list)
            index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(todo_list, index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
