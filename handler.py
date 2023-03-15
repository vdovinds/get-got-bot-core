import json

import main


def handler(event, context):
    params = event["queryStringParameters"]
    user_type = params["user_type"]
    user_id = params["user_id"]

    match params["action"]:
        case 'poem':
            return create_ok_response(main.get_random_poem())
        case 'task':
            return create_ok_response(main.issue_task(user_type, user_id))
        case 'check':
            return create_ok_response('check')
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
