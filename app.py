#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_change_observer.aws_change_observer_stack import AwsChangeObserverStack

from dotenv import load_dotenv

load_dotenv()

region = os.getenv("REGION")
account = os.getenv("ACCOUNT")
is_prod = os.getenv("PROD") == 'True'  # Convert string to boolean if needed


app = cdk.App()
AwsChangeObserverStack(app, "AwsChangeObserverStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account=account, region=region),

    is_prod=is_prod,

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
