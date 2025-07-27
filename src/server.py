import sys
from fastapi import FastAPI

app = FastAPI(title="Outside Thingy", version="0.1.0")

@app.get('/')
async def status():
    return {
        "success": True,
        "data": "Thingy 0.1.0 running."
    }


