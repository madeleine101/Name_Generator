import os
import json
import subprocess

def handler(event, context):
    # Execute your Python script
    subprocess.run(["python3", "functions/python/script.py"])

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Script executed successfully!"})
    }
