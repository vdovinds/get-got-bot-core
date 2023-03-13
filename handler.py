import json


def handler(event, context):
    httpMethod = event["httpMethod"]
    params = event["queryStringParameters"]

    return {
        'statusCode': 200,
        'body': json.dumps(params),
    }


# For local testing only
if __name__ == '__main__':
    test = [{'a': "va"}, {'b': "vb"}, {'c': "vc"}]
    print(test)
