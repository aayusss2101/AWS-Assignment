import json
import os
import boto3
from datetime import datetime

def set_environment_variables(function_name, variables):
    client = boto3.client('lambda')
    response = client.update_function_configuration(
        FunctionName=function_name,
        Environment={
            'Variables': variables
        }
    )
    print("Environment variables set successfully.")


def send_data_to_s3():
    
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


def lambda_handler(event, context):
    
    function_name=context.function_name
    env_name='RUN_COUNT'
    count = os.environ.get(env_name)
    
    if not count:
        count=1
        
    count=int(count)
    
    if count<=3:
        send_data_to_s3()
    
    set_environment_variables(function_name,{env_name: str(count+1)})
    
