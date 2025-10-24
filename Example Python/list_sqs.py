import json
import boto3
from decimal import Decimal
import os

dynamodb = boto3.resource('dynamodb')

class DecimalEncoder(json.JSONEncoder):
    """Custom JSON encoder to convert DynamoDB Decimals to strings."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

def handler(event, context):
    """
    Lambda entry point.
    Scans all items in the DynamoDB table.
    """
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    response = table.scan()
    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(items, cls=DecimalEncoder)
    }
