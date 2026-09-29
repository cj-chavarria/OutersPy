import boto3

from pipeline.core.config import boto3_config

r2 = boto3.client(
    service_name=boto3_config.service_name,
    endpoint_url=boto3_config.endpoint_url,
    aws_access_key_id=boto3_config.access_key_id,
    aws_secret_access_key=boto3_config.secret_access_key,
)

def load_json(folder_path: str, object):
