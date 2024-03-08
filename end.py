from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI()

example_data = {
    "john": True,
    "alice": False,
    "abhijeet": True,
    "bob": True
}

@app.post("/satwika_endpoint")
async def satwika_endpoint(data: Dict[str, bool]):
    if "abhijeet" in data and data["abhijeet"]:
        return {"status": True}
    else:
        return {"status": False}


@app.get("/test_satwika")
async def test_satwika():
    return example_data
