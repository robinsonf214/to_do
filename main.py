class Task:
    def __init__(self, name, status='Pending'):
        self.name = name
        self.status = status

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task.name} - {task.status}")

    def mark_task_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.status = 'Completed'
                print(f"Task '{name}' marked as completed.")
                break
        else:
            print(f"Task '{name}' not found in the to-do list.")

    def clear_tasks(self):
        self.tasks = []
        print("To-do list cleared.")

def main():
    todo_manager = ToDoListManager()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Clear to-do list")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            todo_manager.add_task(name)
        elif choice == '2':
            todo_manager.list_tasks()
        elif choice == '3':
            name = input("Enter task name: ")
            todo_manager.mark_task_completed(name)
        elif choice == '4':
            todo_manager.clear_tasks()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
