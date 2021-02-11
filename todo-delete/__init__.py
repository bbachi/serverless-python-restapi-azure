import logging, json

import azure.functions as func
from services.todo_service import delete_todos


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        task_id = req.route_params.get('id')
    except ValueError:
        pass
    
    data = delete_todos(task_id)
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
