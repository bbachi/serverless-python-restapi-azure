data = {
    "todos": [
      {
        "id": 1,
        "task": 'task1',
        "assignee": 'assignee1000',
        "status": 'completed'
      },
      {
        "id": 2,
        "task": 'task2',
        "assignee": 'assignee1001',
        "status": 'completed'
      },
      {
        "id": 3,
        "task": 'task3',
        "assignee": 'assignee1002',
        "status": 'completed'
      },
      {
        "id": 4,
        "task": 'task4',
        "assignee": 'assignee1000',
        "status": 'completed'
      },
      
    ]
}

def get_todos():
    return data['todos']

def add_todo(task):
    task["id"] = len(data['todos']) + 1
    data['todos'].append(task)
    return {
      "message": "task added",
      "number of tasks": len(data['todos'])
    }

def edit_todo(task):
    for i,todo in enumerate(data["todos"]):
        if todo["id"] == task["id"]:
           data["todos"][i] = task
    
    return {
      "message": "task edited",
      "number of tasks": len(data['todos'])
    }

def delete_todo(task_id):
    item_to_remove = '';
    for todo in data["todos"]:
        if int(task_id) == todo["id"]:
            item_to_remove = todo
    if item_to_remove:
        data["todos"].remove(item_to_remove)
    
    return {
      "message": "task deleted",
      "number of tasks": len(data['todos'])
    }