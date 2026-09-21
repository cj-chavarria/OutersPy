import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full")


@app.cell
def _():
    import csv
    import json
    from datetime import UTC, datetime, timedelta
    from io import StringIO

    import httpx
    import pandas as pd

    return UTC, datetime, httpx, timedelta


@app.cell
def _(UTC, datetime, timedelta):
    now = datetime.now(tz=UTC)
    week = now + timedelta(days=7)
    return now, week


@app.cell
def _():
    JPL_API_URL = "https://ssd-api.jpl.nasa.gov/sbdb_query.api"
    params_jpl: dict[str, str] = {
        "fields": "full_name,epoch,e,a,q,i,om,w",
        "sb-class": "COM",
    }
    return


@app.cell
def _(now, week):
    HORIZON_API = "https://ssd.jpl.nasa.gov/api/horizons.api"
    params_horizon: dict[str, str] = {
        "format": "text",
        "COMMAND": "499",
        "EPHEM_TYPE": "ELEMENTS",
        "START_TIME": now.date(),
        "STOP_TIME": week.date(),
        "STEP_SIZE": "1d",
        "CENTER": "@10",
        "CSV_FORMAT": "YES",
    }
    return HORIZON_API, params_horizon


@app.cell
def _(HORIZON_API, httpx, params_horizon: dict[str, str]):
    response = httpx.get(url=HORIZON_API, params=params_horizon)
    response.raise_for_status()
    horizon_res = response.text
    print(horizon_res)
    return


@app.cell
def _(now, week):
    from astroquery.jplhorizons import Horizons

    obj = Horizons(
        id="2026 RR34",
        location="@10",
        epochs={
            "start": str(now.date()),
            "stop": str(week.date()),
            "step": "1d",
        },
    )
    obj
    return (obj,)


@app.cell
def _(obj):
    elem = obj.elements()
    df = elem.to_df("polars")
    df
    return


@app.cell
def _(httpx, now, week):
    SB_CA_URL = "https://ssd-api.jpl.nasa.gov/cad.api"
    params_ca = {
        "date-min": now.date(),
        "date-max": week.date(),
        "body": "Earth",
        "limit": 5,
        "sort": "dist-min",
        "fullname": True,
    }

    sb_ca_res = httpx.get(url=SB_CA_URL, params=params_ca)
    sb_ca_res.raise_for_status()

    ca_data = sb_ca_res.json()

    ca_data
    return


if __name__ == "__main__":
    app.run()
