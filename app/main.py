from tools import currency_converter, check_valid
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/api/rates")
async def get_exchange_rate(fr: str = Query(alias="from"), to: str = Query(), value: int = Query()):
    if not check_valid(fr, to):
        return {"result": "invalid pair"}

    result = currency_converter(fr, to, value)

    return {"result": result}
