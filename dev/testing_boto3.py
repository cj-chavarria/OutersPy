import json
from datetime import UTC, datetime, timedelta

from pipeline.clients.boto3_client import load_json_2_r2
from pipeline.clients.jpl_client import JPLService

now = datetime.now(tz=UTC)
week = now + timedelta(days=6)


if __name__ == "__main__":
    json_path = "test5.json"

    with JPLService(start_time=now, stop_time=week) as jpl:
        ca_test = jpl.close_approaches(body="Earth")

    json_obj = json.dumps(ca_test)

    load_json_2_r2(path=json_path, json=json_obj, metadata={"prueba5": "test5"})
