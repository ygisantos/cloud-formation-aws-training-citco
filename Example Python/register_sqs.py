import json
import boto3
import os
from decimal import Decimal

# Initialize AWS clients outside the handler (for better cold-start performance)
dynamodb = boto3.resource('dynamodb')
sqs = boto3.client('sqs')

def handler(event, context):
    """
    Lambda entry point.
    Expects event['body'] with JSON data:
    {
      "cardId": "CARD123",
      "owner": "Ygi Santos"
    }
    """
    try:
        body = json.loads(event.get('body', '{}'))
        register_card(body)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Card registered successfully!'})
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def register_card(item):
    """
    Insert card record into DynamoDB and send message to SQS.
    Adds default fields: status=INACTIVE, balance=0.
    """
    table_name = os.environ['TABLE_NAME']
    queue_url = os.environ['QUEUE_URL']

    table = dynamodb.Table(table_name)

    # Default attributes
    item['status'] = 'INACTIVE'
    item['balance'] = Decimal(0)

    # Save to DynamoDB
    table.put_item(Item=item)

    # Send message to SQS
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(item, default=str)
    )
