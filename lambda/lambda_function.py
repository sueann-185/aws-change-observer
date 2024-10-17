def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Allow all origins for testing
            'Access-Control-Allow-Methods': 'GET,OPTIONS',  # Allowed methods
            'Access-Control-Allow-Headers': 'Content-Type',  # Allowed headers
        },
        'body': 'Hello from Lambda!'
    }