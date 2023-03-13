import json


def handler(event, context):
    httpMethod = event["httpMethod"]
    params = event["queryStringParameters"]
    response_body = ''

    match params["action"]:
        case 'poem':
            response_body = 'get poem'
        case 'task':
            response_body = 'get new task'
        case 'check':
            response_body = 'check answer'
        case _:
            response_body = 'unknown request type'

    return {
        'statusCode': 200,
        'body': json.dumps(response_body),
    }


# For local testing only
# if __name__ == '__main__':
    # test = {"action": "poem", "answer": "get", "user_id": "12345", "user_type": "tg"}
