import logging, json

import azure.functions as func
from services.todo_service import edit_todos


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    data = edit_todos(req_body.get('task'))
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
