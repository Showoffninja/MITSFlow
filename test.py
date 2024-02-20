import boto3
import json

client = boto3.client('dynamodb')
table = 'park'

client = DynamoDB.Client(
    host='http://localhost:8000',
    port=8000,
    aws_access_key_id='12345678',
    aws_secret_access_key='12345678',
    is_secure=False
    )