import json
import boto3

def handler(event, context):
    register_card(json.loads(event['body']))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Card registered successfully!')
    }

def register_card(item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_accounts_cfn')
    item['status'] = 'INACTIVE'
    item['balance'] = 0
    
    table.put_item(
        Item=item
    )