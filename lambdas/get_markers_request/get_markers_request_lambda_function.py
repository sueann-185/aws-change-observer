import json
import os
import logging
import boto3
from data_service import DataService

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize outside the handler for connection reuse
dynamodb_resource = boto3.resource('dynamodb')

def lambda_handler(event, context):
    """
    AWS Lambda handler function to retrieve location markers.

    :param event: AWS Lambda event object.
    :param context: AWS Lambda context object.
    :return: HTTP response with status code and body.
    """
    table_name = os.environ.get('TABLE_NAME')
    if not table_name:
        logger.error("TABLE_NAME environment variable is not set.")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Server configuration error.'})
        }

    data_service = DataService(table_name=table_name, dynamodb_resource=dynamodb_resource)
    
    try:
        markers = data_service.get_markers()
        logger.info(f"Successfully retrieved {len(markers)} markers.")
    except NotImplementedError as e:
        logger.error(f"get_markers() not implemented: {e}")
        return {
            'statusCode': 501,
            'body': json.dumps({'error': 'Functionality not implemented.'})
        }
    except Exception as e:
        logger.error(f"Error retrieving markers: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to retrieve markers.'})
        }

    return {
        'statusCode': 200,
        'body': json.dumps({'markers': markers})
    }
