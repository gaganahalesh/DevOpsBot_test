def handler(request):
    # You can still log this for debugging
    print("Hello from Python (this will go to Vercel logs)")
    
    # But this is what the user sees in the browser
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"message": "Hello from Python!"}'
    }
