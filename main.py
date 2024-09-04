from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a request model to validate the input data
class Int32ArrayRequest(BaseModel):
    numbers: List[int]

@app.post("/process_array")
async def process_array(request: Int32ArrayRequest):
    # Define the int32 range
    int32_min = -2**31
    int32_max = 2**31 - 1

    # Validate that all numbers are within the int32 range
    for number in request.numbers:
        if not (int32_min <= number <= int32_max):
            raise HTTPException(status_code=400, detail="All elements must be int32 numbers")

    # Process the array: For example, return the sum of the array
    result = sum(request.numbers)
    
    return {"result": result}

@app.post("/service_root")
async def service_root(endpoint_url: str):
    return {"received_url": endpoint_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
