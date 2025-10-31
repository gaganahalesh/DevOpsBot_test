def handler(request):
    # This is the simplest working Vercel Python handler
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": "Hello from Python!"
    }
