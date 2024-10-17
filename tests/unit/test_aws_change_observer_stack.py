import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_change_observer.aws_change_observer_stack import AwsChangeObserverStack

# example tests
def test_lambda_function_created():
    app = core.App()
    stack = AwsChangeObserverStack(app, "aws-change-observer")
    template = assertions.Template.from_stack(stack)

    # Check if there is a Lambda function resource in the stack
    template.resource_count_is("AWS::Lambda::Function", 1)
