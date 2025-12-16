#!/usr/bin/env python3
"""
Todo List Application
A simple command-line todo list manager.
"""

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        """Add a new task to the todo list."""
        if not description:
            print("Error: Task description cannot be empty.")
            return False
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task added: {description}")
        return True
    
    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        print("\n--- Todo List ---")
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"{task['id']}. [{status}] {task['description']}")
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
    
    def get_stats(self):
        """Get statistics about tasks."""
        total = len(self.tasks)
        if total == 0:
            print("No tasks yet. Add some tasks to see statistics.")
            return
        
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        # Fixed: Added check to prevent division by zero
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        print(f"\n--- Statistics ---")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        print(f"Completion rate: {completion_rate:.1f}%")
        print("------------------\n")


def main():
    """Main function to run the todo app."""
    todo = TodoList()
    
    print("Welcome to Todo List App!")
    print("Commands: add, list, complete, delete, stats, quit\n")
    
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "add":
            description = input("Enter task description: ").strip()
            todo.add_task(description)
        elif command == "list":
            todo.list_tasks()
        elif command == "complete":
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif command == "delete":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif command == "stats":
            todo.get_stats()
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Try: add, list, complete, delete, stats, quit")


if __name__ == "__main__":
    main()
