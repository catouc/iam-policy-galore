#!/usr/bin/env python
import boto3

client = boto3.client('lambda')
with open('function.zip', 'rb') as f:
    zip_code = f.read()

function = client.create_function(
    FunctionName='TestingMinimumLambdaPermissions',
    Runtime='python3.7',
    Role='arn:aws:iam::983498139013:role/LambdaMinimumPermissionsTest',
    Handler='main.lambda_handler',
    Code={
        'ZipFile': zip_code
    }
)
