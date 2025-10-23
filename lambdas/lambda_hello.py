import json

def handler(event, context):
    print("api invoked")
    print("#event")
    name = event.get("queryStringParameters").get("name", "")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello {name} from lambda"
        })
    }