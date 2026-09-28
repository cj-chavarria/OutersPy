from datetime import UTC, datetime, timedelta

import boto3
from jpl_client import JPLService

s3 = boto3.client(
    service_name="s3",
    endpoint_url="",
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name="auto",
)

now = datetime.now(tz=UTC)
week = now + timedelta(days=6)

file_name = "test.json"
test = JPLService(now, week).close_approaches("Earth")

if __name__ == "__main__":
    print(type(test))
