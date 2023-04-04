import ast
import json

import main


def handler(event, context):
    params = event["queryStringParameters"]

    match params["action"]:
        case 'poem':
            return create_ok_response(main.get_random_poem(params["user_type"], params["user_id"], ast.literal_eval(params["user_info"])))
        case 'task':
            return create_ok_response(main.issue_task(params["user_type"], params["user_id"], ast.literal_eval(params["user_info"])))
        case 'check':
            return create_ok_response(main.check_task(params["user_type"], params["user_id"], params["answer"]))
        case 'answer':
            return create_ok_response(main.get_task_answer(params["user_type"], params["user_id"]))
        case _:
            return create_not_found_response('unknown request type')


def create_ok_response(body):
    return {
        'statusCode': 200,
        'body': json.dumps(body, ensure_ascii=False, indent=4),
    }


def create_not_found_response(text):
    return {
        'statusCode': 404,
        'body': json.dumps(text),
    }
