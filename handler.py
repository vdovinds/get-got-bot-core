import json


def handler(event, context):
    httpMethod = event["httpMethod"]
    params = event["queryStringParameters"]

    return {
        'statusCode': 200,
        #'body': json.dumps(params),
        'body': "ok",
    }