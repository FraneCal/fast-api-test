from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ListRequest(BaseModel):
    numbers: list[int]

@app.post("/")
async def root(request: ListRequest):
    # int32 range
    int32_min = -2**31
    int32_max = 2**31 - 1

    for number in request.numbers:
        if not (int32_min <= number <= int32_max):
            raise HTTPException(status_code=400, detail="All elements must be int32 numbers")
        
    result = sum(request.numbers)
    
    return {"result": result}
