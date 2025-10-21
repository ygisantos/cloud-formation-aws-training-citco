import json

def handler(event, context):
    print("S3 Event!")
    print(json.dumps(event, indent=2))
    return "Happy birthday janna"
    
