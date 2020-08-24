import json
import logging
import boto3

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):

    logger.debug('Got an event!')
    logger.debug(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from invoiceService!",
        }),
    }

