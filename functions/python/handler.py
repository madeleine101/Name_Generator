import os
import json
import boto3
from botocore.exceptions import NoCredentialsError
import subprocess

def handler(event, context):
    # Initialize the S3 client with custom environment variables
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv('MY_AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('MY_AWS_SECRET_ACCESS_KEY'),
                      region_name=os.getenv('MY_AWS_REGION'))

    bucket_name = os.getenv('MY_S3_BUCKET_NAME')
    file_name = 'output.txt'

    try:
        # Execute the script and capture its output
        script_output = subprocess.check_output(["python3", "functions/python/script.py"], text=True)

        # Optionally, you can still upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=script_output)

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Script executed successfully!", "output": script_output})
        }
    except NoCredentialsError:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Credentials not available"})
        }
    except subprocess.CalledProcessError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Script execution failed", "output": e.output})
        }
