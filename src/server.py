import sys
from fastapi import FastAPI;
from api.controllers import BaseController;

app = FastAPI(title="Outside Thingy", version="0.1.0")

print(f"========= {sys.path} ==========")

@app.get('/')
@app.get('/status')
async def status():
    return {
        "success": True,
        "data": "Thingy 0.1.0 running."
    }

BaseController.setup(app)
