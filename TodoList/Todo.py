import json
import os

FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i+1}. {task['title']} [{status}]")

# Add task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

# Mark done
def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except:
        print("Invalid input!")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid input!")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()