from services.dummy_data import get_todos, add_todo, edit_todo, delete_todo

def list_todos():
    return get_todos()

def add_todos(task):
    return add_todo(task)

def edit_todos(task):
    return edit_todo(task)

def delete_todos(task_id):
    return delete_todo(task_id)