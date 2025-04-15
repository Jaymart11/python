def add_task(tasks, description):
    """Add a new task to the list"""
    if not description.strip():
        print("Error: Task description cannot be empty!")
        return
    
    tasks.append({"description": description.strip(), "completed": False})
    print(f"Added task: '{description}'")

def view_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("No tasks  in the list!")
        return
    
    print("\nCurrent Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "X" if task["completed"] else " "
        print(f"{idx}. [{status}] {task['description']}")

def complete_task(tasks):
    """Mark a task as completed"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num-1]["completed"] = True
            print(f"Marked task '{tasks[task_num-1]['description']}' as completed")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def remove_task(tasks):
    """Remove a task from the list"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num-1)
            print(f"Removed task: '{removed['description']}'")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Manager:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-5.")
            continue
        
        match choice:
            case 1:
                description = input("Enter task description: ")
                add_task(tasks, description)
            case 2:
                view_tasks(tasks)
            case 3:
                complete_task(tasks)
            case 4:
                remove_task(tasks)
            case 5:
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()