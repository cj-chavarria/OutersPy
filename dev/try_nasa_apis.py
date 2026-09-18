import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    from typing import Any

    import httpx
    from httpx._models import Response

    return Any, Response, httpx


@app.cell
def _():
    JPL_API_URL= "https://ssd-api.jpl.nasa.gov/sbdb_query.api"
    params: dict[str, str] = {
        "fields": "full_name,epoch,e,a,q,i,om,w",
        "sb-class": "COM"
    }
    return JPL_API_URL, params


@app.cell
def _(Any, JPL_API_URL, Response, httpx, params: dict[str, str]):
    response: Response = httpx.get(url=JPL_API_URL, params=params)
    response.raise_for_status()

    data: Any = response.json()
    return


@app.cell
def _(Response, httpx):
    response2: Response = httpx.get(
        url="https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='499'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@399'&START_TIME='2006-01-01'&STOP_TIME='2006-01-20'&STEP_SIZE='1%20d'&QUANTITIES='1,9,20,23,24,29'"
    )
    response2.raise_for_status()

    data2: str = response2.text
    return (data2,)


@app.cell
def _(data2: str):
    print(data2)
    return


if __name__ == "__main__":
    app.run()
