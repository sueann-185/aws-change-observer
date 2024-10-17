from aws_cdk import (
    aws_lambda,
    aws_apigateway,
    Stack
)
from constructs import Construct

class AwsChangeObserverStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function 
        example_lambda_function = aws_lambda.Function(
            self, 'ExampleLambdaFunction',
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler='lambda_function.lambda_handler',
            code=aws_lambda.Code.from_asset('lambda')
        )

        # API Gateway
        api = aws_apigateway.LambdaRestApi(
            self, 'ExampleApiGateway',
            handler=example_lambda_function,
            proxy=False
        )

        # Add a specific resource
        hello_resource = api.root.add_resource("hello")
        hello_resource.add_method("GET") # GET /hello
