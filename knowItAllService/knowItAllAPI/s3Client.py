import boto3
import os
from botocore.client import Config
from botocore.exceptions import ClientError
from .constants import *

def saveFile(bucketName, key, fileBinary):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        config=Config(signature_version='s3v4')
    )

    bucket = s3.Bucket(bucket_name)
    bucket.put_object(
        Key=key,
        Body = fileBinary
    )

def getObject(bucketName, key):
    client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        config=Config(signature_version='s3v4')
    )
    response = None
    try:
        response = client.get_object(
            Bucket=bucketName,
            Key=key
        )
        body = response['Body'].read()
        return body
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print("No such key:", key)
        return ""