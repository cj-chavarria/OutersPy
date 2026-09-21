import marimo

__generated_with = "0.24.2"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    import csv
    from io import StringIO
    import httpx
    import pandas as pd

    return StringIO, httpx, pd


@app.cell
def _():
    JPL_API_URL = "https://ssd-api.jpl.nasa.gov/sbdb_query.api"
    params_jpl: dict[str, str] = {
        "fields": "full_name,epoch,e,a,q,i,om,w",
        "sb-class": "COM",
    }
    return


@app.cell
def _():
    HORIZON_API = "https://ssd.jpl.nasa.gov/api/horizons.api"
    params_horizon: dict[str, str] = {
        "format": "json",
        "COMMAND": "499",
        "EPHEM_TYPE": "ELEMENTS",
        "START_TIME": "2026-09-19",
        "STOP_TIME": "2026-09-30",
        "STEP_SIZE": "1d",
        "CENTER": "@10",
        "CSV_FORMAT": "YES",
    }
    return HORIZON_API, params_horizon


@app.cell
def _(HORIZON_API, httpx, params_horizon: dict[str, str]):
    response = httpx.get(url=HORIZON_API, params=params_horizon)
    response.raise_for_status()

    data = response.json()
    return (data,)


@app.cell
def _(data):
    result = data.get("result")
    print(result)
    return (result,)


@app.cell
def _():
    columns = ['JDTDB','Calendar Date (TDB)','EC','QR','IN','OM','W','Tp','N','MA','TA','A','AD','PR']
    return (columns,)


@app.cell
def _(result):
    if "$$SOE" in result and "$$EOE" in result:
        table = result.split("$$SOE\n")[1].split("\n$$EOE")[0]
    else:
        print("No table")
    return (table,)


@app.cell
def _(StringIO, columns, pd, table):
    df = pd.read_csv(StringIO(table), header=None, names=columns, index_col=False)
    df
    return


@app.cell
def _():
    from astroquery.jplhorizons import Horizons

    obj = Horizons(
        id="499",
        location="@10",
        epochs={"start": "2026-09-19", "stop": "2026-09-30", "step": "1d"},
    )
    return (obj,)


@app.cell
def _(obj):
    elem = obj.elements()
    return (elem,)


@app.cell
def _(elem):
    elem.to_pandas()
    return


if __name__ == "__main__":
    app.run()
