#!/usr/bin/env python3
"""
Todo List Application
A simple command-line todo list manager.
"""

class TodoApp:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task to the todo list."""
        if not description or not description.strip():
            print("Error: Task description cannot be empty.")
            return False
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description.strip(),
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task added: {task['description']}")
        return True
    
    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n--- Todo List ---")
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"[{status}] {task['id']}: {task['description']}")
        print("-----------------\n")
    
    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed.")
                return True
        print(f"Task {task_id} not found.")
        return False
    
    def delete_task(self, task_id):
        """Delete a task from the list."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed = self.tasks.pop(i)
                print(f"Task deleted: {removed['description']}")
                return True
        print(f"Task {task_id} not found.")
        return False
    
    def get_task_count(self):
        """Get the total number of tasks."""
        return len(self.tasks)
    
    def get_completion_percentage(self):
        """Get the percentage of completed tasks."""
        total = len(self.tasks)
        if total == 0:
            return 0.0  # Fixed: Return 0 when no tasks instead of dividing by zero
        
        completed = sum(1 for task in self.tasks if task['completed'])
        return (completed / total) * 100


def main():
    app = TodoApp()
    
    while True:
        print("\n=== Todo List Menu ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Show statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ")
            app.add_task(description)
        
        elif choice == '2':
            app.list_tasks()
        
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                app.complete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid task ID.")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                app.delete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid task ID.")
        
        elif choice == '5':
            total = app.get_task_count()
            percentage = app.get_completion_percentage()
            print(f"\nTotal tasks: {total}")
            print(f"Completion: {percentage:.1f}%")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
