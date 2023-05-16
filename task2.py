import boto3
import json
from datetime import datetime


def lambda_handler(event, context):

    BUCKET_NAME = 'aayusss2101-aws-assignment'
    now = str(datetime.now())

    data={}

    data['transaction_id']=12345
    data['payment_mode'] = 'card/netbanking/upi'
    data['amount'] = 200
    data['customer_id'] = 101
    data['timestamp'] = now

    s3_client = boto3.client('s3')

    file_name = now+'.json'
    json_data=json.dumps(data)

    s3_client.put_object(Body=json_data, Bucket=BUCKET_NAME, Key=file_name)
