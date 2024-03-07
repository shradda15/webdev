from typing import Union
# http://3.27.215.225/vinn?key=gundladodla

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"detail": "not found"}


@app.get("/{item_id}")
def read_item(item_id: str, key: Union[str, None] = None):
    if(item_id=="vinn" and key=="ka"):
        return {"token":"14341L"}
    else:
        return {"token": "wrong guess"}
