import json
import logging
import boto3

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info('Got an event!')
    logger.info(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from invoiceService!",
        }),
    }

