import json

class TodoListManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'name': task, 'status': 'Pending'})
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            print(f"- {task['name']} [{task['status']}]")

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                task['status'] = 'Completed'
                self.save_tasks()
                return True
        return False

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()

if __name__ == '__main__':
    todo_list = TodoListManager()

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task name: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_name = input("Enter task name: ")
            if todo_list.mark_task_completed(task_name):
                print(f"Task '{task_name}' marked as completed.")
            else:
                print(f"Task '{task_name}' not found.")
        elif choice == '4':
            todo_list.clear_tasks()
            print("All tasks cleared.")
        elif choice == '0':
            break
