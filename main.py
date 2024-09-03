from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Numbers(BaseModel):
    numbers: List[int]

@app.post("/process/")
async def process_numbers(data: Numbers):
    result = sum(data.numbers)
    return {"result": result}
