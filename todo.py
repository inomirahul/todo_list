"""
Todo List Application
Fixed: Removed accidental division by zero bug (INC-002)
"""

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task with the given description."""
        if not description:
            raise ValueError("Task description cannot be empty")
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task added: {description}")
        return task
    
    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return []
        
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"[{status}] {task['id']}: {task['description']}")
        return self.tasks
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed.")
                return task
        print(f"Task {task_id} not found.")
        return None
    
    def delete_task(self, task_id):
        """Delete a task by ID."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed = self.tasks.pop(i)
                print(f"Task deleted: {removed['description']}")
                return removed
        print(f"Task {task_id} not found.")
        return None
    
    def get_completion_percentage(self):
        """Get the percentage of completed tasks."""
        if len(self.tasks) == 0:
            # Fix: Handle empty task list to avoid division by zero
            return 0.0
        completed = sum(1 for task in self.tasks if task['completed'])
        return (completed / len(self.tasks)) * 100


def main():
    todo = TodoList()
    
    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Show completion percentage")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                todo.add_task(description)
            else:
                print("Description cannot be empty.")
        elif choice == '2':
            todo.list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == '5':
            percentage = todo.get_completion_percentage()
            print(f"Completion: {percentage:.1f}%")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
