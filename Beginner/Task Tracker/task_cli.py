import sys
import task_manager

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Description is required for 'add' command.")
            return
        task_manager.add_task(sys.argv[2])
    
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Error: ID and Description are required for 'update' command.")
            return
        try:
            task_id = int(sys.argv[2])
            task_manager.update_task(task_id, sys.argv[3])
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: ID is required for 'delete' command.")
            return
        try:
            task_id = int(sys.argv[2])
            task_manager.delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Error: ID is required for 'mark-in-progress' command.")
            return
        try:
            task_id = int(sys.argv[2])
            task_manager.mark_task(task_id, 'in-progress')
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Error: ID is required for 'mark-done' command.")
            return
        try:
            task_id = int(sys.argv[2])
            task_manager.mark_task(task_id, 'done')
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'list':
        if len(sys.argv) == 3:
            status = sys.argv[2]
            if status not in ['todo', 'in-progress', 'done']:
                print("Error: Invalid status. Use 'todo', 'in-progress', or 'done'.")
                return
            task_manager.list_tasks(status)
        else:
            task_manager.list_tasks()
    
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
