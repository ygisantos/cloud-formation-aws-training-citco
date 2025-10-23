import json

def handler(event, context):
    print("Event received")
    print(json.dumps(event, indent=2))
    
    return "ok"