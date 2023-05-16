import boto3
import json
from datetime import datetime


def lambda_handler(event, context):

    BUCKET_NAME = 'aayusss2101-aws-assignment'

    now = str(datetime.now())
    data = event.copy()
    data['timestamp'] = now
    json_text = json.dumps(data)

    s3_client = boto3.client('s3')

    file_name = now+'.json'

    s3_client.put_object(Body=json_text, Bucket=BUCKET_NAME, Key=file_name)

    return {
        "file_name": file_name
    }
