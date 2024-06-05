import os
import json
import boto3
from botocore.exceptions import NoCredentialsError

def handler(event, context):
    # Initialize the S3 client with custom environment variables
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv('MY_AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('MY_AWS_SECRET_ACCESS_KEY'),
                      region_name=os.getenv('MY_AWS_REGION'))

    bucket_name = os.getenv('MY_S3_BUCKET_NAME')
    file_content = 'Hello, world!'
    file_name = 'output.txt'

    try:
        # Upload the file to the specified S3 bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Script executed and file stored successfully!"})
        }
    except NoCredentialsError:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Credentials not available"})
        }
