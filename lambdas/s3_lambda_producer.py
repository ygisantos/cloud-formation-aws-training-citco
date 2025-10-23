import json
import boto3
import os

def handler(event, context):
    print("#event recieved")
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    message=f"A file has been uploaded to bucket: {bucket_name}"
    message+=f"File name: {file_name}"
    
    sqs = boto3.client('sqs')
    queue_url = os.getenv['QUEUE_URL', None]
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print(message)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
