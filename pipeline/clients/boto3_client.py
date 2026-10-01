import json

import boto3

from pipeline.core.config import boto3_config

r2 = boto3.client(
    service_name=boto3_config.service_name,
    endpoint_url=boto3_config.endpoint_url,
    aws_access_key_id=boto3_config.key_id,
    aws_secret_access_key=boto3_config.access_key,
)


def load_json(path: str, json: str, metadata: dict) -> str:
    response = r2.put_object(
        Bucket=boto3_config.bucket_name,
        Body=json,
        ContentType="application/json",
        Key=path,
        Metadata=metadata,
    )
    etag = response.get("ETag")
    return etag


def get_json(path: str) -> dict:
    response = r2.get_object(
        Bucket=boto3_config.bucket_name,
        Key=path,
        ResponseContentType="application/json",
    )
    content = response.get("Body").read().decode("utf-8")
    return json.loads(s=content)
