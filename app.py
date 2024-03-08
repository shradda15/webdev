customer_orders = {
    "katrina kaif": ["chocolate", "sunglasses", "perfume","kite"]
}

app = FastAPI()
class PromptInput(BaseModel):
    customer_name: str
    products : List[str]

@app.post("/chatgpt")
def fn(customer_name : str):
    if customer_name in customer_orders:
        return customer_orders[customer_name]
    else:
        return []   

s=fn("katrina kaif")

print(s)