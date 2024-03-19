class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = '✓' if task.completed else ' '
            print(f"{index}. [{status}] {task.description}")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].completed = True

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]


def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
