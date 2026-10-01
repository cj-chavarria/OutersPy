import json
from datetime import UTC, datetime, timedelta
from pprint import pprint

from pipeline.clients.boto3_client import get_json, load_json
from pipeline.clients.jpl_client import JPLService

now = datetime.now(tz=UTC)
week = now + timedelta(days=6)

json_path = "test5.json"


def _load_data():
    with JPLService(start_time=now, stop_time=week) as jpl:
        ca_test = jpl.close_approaches(body="Earth")

    json_obj = json.dumps(ca_test)

    load_json(path=json_path, json=json_obj, metadata={"prueba5": "test5"})


def _get_data():
    r2_json = get_json(path=json_path)
    return r2_json


if __name__ == "__main__":
    _load_data()
    pprint(_get_data(), sort_dicts=False)
