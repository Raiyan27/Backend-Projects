from datetime import datetime
import storage

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = storage.load_tasks()
    new_task = {
        'id': get_next_id(tasks),
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'updatedAt': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, description):
    tasks = storage.load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            storage.save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = storage.load_tasks()
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_len:
        storage.save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")

def mark_task(task_id, status):
    tasks = storage.load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            storage.save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks(status_filter=None):
    tasks = storage.load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    filtered_tasks = [t for t in tasks if status_filter is None or t['status'] == status_filter]
    
    if not filtered_tasks:
        print(f"No tasks found with status: {status_filter}")
        return

    print(f"{'ID':<5} {'Status':<15} {'Description':<30} {'Created At':<25} {'Updated At':<25}")
    print("-" * 100)
    for task in filtered_tasks:
        print(f"{task['id']:<5} {task['status']:<15} {task['description']:<30} {task['createdAt']:<25} {task['updatedAt']:<25}")
