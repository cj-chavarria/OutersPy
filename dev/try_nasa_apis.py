import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import csv
    import json
    from datetime import UTC, datetime, timedelta
    from io import StringIO

    import httpx
    import pandas as pd

    return StringIO, UTC, datetime, httpx, pd, timedelta


@app.cell
def _(UTC, datetime, timedelta):
    now = datetime.now(tz=UTC)
    week = now + timedelta(days=6)
    return now, week


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
    return (horizon_res,)


@app.cell
def _(horizon_res):
    res_lines = horizon_res.split("\n")
    res_lines
    return (res_lines,)


@app.cell
def _(res_lines):
    start_tbl_idx = 0
    end_tbl_idx = 0
    for idx, line in enumerate(res_lines):
        start_tbl_idx = idx  if "$$SOE" in line else start_tbl_idx
        end_tbl_idx = idx if "$$EOE" in line else end_tbl_idx

    if start_tbl_idx and end_tbl_idx != 0:
        header = res_lines[start_tbl_idx - 2].replace(" ","")
        data = [s for s in res_lines[start_tbl_idx + 1: end_tbl_idx]]

    data_str = "\n".join(data).replace(" ","")
    tbl_out = header + "\n" + data_str

    print(tbl_out)
    return (tbl_out,)


@app.cell
def _(StringIO, pd, tbl_out):
    pd.read_csv(StringIO(tbl_out))
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
