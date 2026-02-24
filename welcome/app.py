import json

# import requests


def lambda_handler(event, context):
    #Sample pure Lambda function
    first_name = event["first_name"]
    last_name = event["last_name"]
    message = event["message"]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{message} from {first_name} {last_name}",
        }),
    }
