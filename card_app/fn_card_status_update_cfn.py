import json
import boto3

def handler(event, context):
    item = json.loads(event['body'])
    update_card_status(item['card_no'], item['status'])

    return {
        'statusCode': 200,
        'body': json.dumps(f"Card {item['card_no']} Updated successfully")
    }

def update_card_status(card_no, status):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_accounts_cfn')
    response = table.update_item(
        Key={'card_no': card_no},
        UpdateExpression="set #status = :s",
        ExpressionAttributeNames={'#status': 'status'},
        ExpressionAttributeValues={':s': status},
        ReturnValues="UPDATED_NEW"
    )

    return response