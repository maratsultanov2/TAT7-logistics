from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .api import process_shipment

app = FastAPI(title="TAT-7 Logistics")

@app.post("/webhook/bitrix24")
async def webhook(request: Request):
    try:
        payload = await request.json()
        result = await process_shipment(payload)
        return JSONResponse(content={"status": "ok", "result": result})
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)

@app.get("/")
def root():
    return {"status": "ok", "message": "TAT-7 Logistics running"}
