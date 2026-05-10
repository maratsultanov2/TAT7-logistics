from fastapi import FastAPI
from .api import router

app = FastAPI(title="TAT-7 Logistics")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok", "message": "TAT-7 Logistics running"}
