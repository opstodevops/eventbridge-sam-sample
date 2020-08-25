import json
import boto3
import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
def lambda_handler(event, context):
    event_bridge = boto3.client('events')
    
    response = event_bridge.put_events(
        Entries=[
            {
                'Source': 'demo.orders',
                'DetailType': 'New Order',
                'Detail': json.dumps({
                    "state": "created",
                    "id": "123"
                    }),
            },
        ]
    )
    
    # logger.debug(response)
    print(response)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from orderService!",
        }),
    }
