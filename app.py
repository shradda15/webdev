from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

customer_orders = {
    "katrina kaif": ["chocolate", "sunglasses", "perfume","kite"]
}

app = FastAPI()
class add(BaseModel):
    customer_name: str
    products : List[str]

@app.get("/add_order")
def fn(customer_name : str):
    if customer_name in customer_orders:
        return customer_orders[customer_name]
    else:
        return []  

@app.post("/add_order")
async def add_order(order_input: add):
    customer_name = order_input.customer_name
    products = order_input.products
    customer_orders[customer_name] = products
