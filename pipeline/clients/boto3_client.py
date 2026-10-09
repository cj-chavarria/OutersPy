import boto3
from botocore.exceptions import ClientError

from pipeline.core.config import boto3_config
from pipeline.core.logger_base import logger

r2 = boto3.client(
    service_name=boto3_config.service_name,
    endpoint_url=boto3_config.endpoint_url,
    aws_access_key_id=boto3_config.key_id,
    aws_secret_access_key=boto3_config.access_key,
)


def load_json(key: str, body: str, metadata: dict) -> dict:
    try:
        return r2.put_object(
            Bucket=boto3_config.bucket_name,
            Body=body,
            ContentType="application/json",
            Key=key,
            Metadata=metadata,
        )
    except ClientError as e:
        logger.error(e)
        raise


def get_json(key: str) -> dict:
    try:
        return r2.get_object(
            Bucket=boto3_config.bucket_name,
            Key=key,
            ResponseContentType="application/json",
        )
    except ClientError as e:
        logger.error(e)
        raise
