import json
import boto3
import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
def lambda_handler(event, context):

    # logger.debug('Got an event!')
    # logger.debug(event)
    print(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from invoiceService!",
        }),
    }

