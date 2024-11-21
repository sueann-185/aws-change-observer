import json  
import os  
import logging  
import boto3  
from data_service import DataService  
from location_marker import LocationMarker  

# Configure logging  
logger = logging.getLogger()  
logger.setLevel(logging.INFO)  

# Initialize outside the handler for connection reuse  
dynamodb_resource = boto3.resource('dynamodb')  

def lambda_handler(event, context):  
    """  
    AWS Lambda handler function to view historical images of a location marker.  

    :param event: AWS Lambda event object, expected to contain the markerId in the body.  
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
        body = json.loads(event.get('body', '{}'))  
        marker_id = body.get('markerId')  

        if not marker_id:  
            logger.error("markerId is missing from the request body.")  
            return {  
                'statusCode': 400,  
                'body': json.dumps({'error': 'markerId is required.'})  
            }  
    except json.JSONDecodeError as e:  
        logger.error(f"Invalid JSON in request body: {e}")  
        return {  
            'statusCode': 400,  
            'body': json.dumps({'error': 'Invalid request body.'})  
        }  

    try:  
        # Retrieve the location marker from the database using the markerId  
        marker = data_service.get_marker(marker_id)  
        if not marker:  
            logger.warning(f"No location marker found with ID: {marker_id}")  
            return {  
                'statusCode': 404,  
                'body': json.dumps({'error': 'Location marker not found.'})  
            }  

        # Retrieve historical images 
        historical_images = marker.get_historical_images()
        if not historical_images:  
            logger.info(f"No historical images found for marker ID: {marker_id}")  
            return {  
                'statusCode': 404,  
                'body': json.dumps({'error': 'Historical images unavailable.'})  
            }  

        # Return the historical images in the response  
        return {  
            'statusCode': 200,  
            'body': json.dumps({  
                'markerId': marker.get_marker_id(),  
                'historicalImages': [image.to_json() for image in historical_images]  
            })  
        }  
    except Exception as e:  
        logger.error(f"Error retrieving historical images: {e}")  
        return {  
            'statusCode': 500,  
            'body': json.dumps({'error': 'Failed to retrieve historical images.'})  
        }
    
