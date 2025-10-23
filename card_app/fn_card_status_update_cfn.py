import json

def handler(event, context):
    print("#event")
    print(json.dumps(event, indent=2))
    
    return {
        'statusCode': 200,
        'body': "card status update api invoked!"
    }