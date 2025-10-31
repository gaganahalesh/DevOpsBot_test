import json

def handler(request):
    body = {"message": "Hello, World!"}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
