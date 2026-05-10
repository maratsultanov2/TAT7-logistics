from fastapi import FastAPI, Request, HTTPException
from app.integrations.tat7 import dialogue_ring
from app.integrations.giga import generate_instruction
app = FastAPI(title="TAT-7 Logistics", version="4.2")

@app.post("/webhook/tat7")
async def tat7_processor(request: Request):
    data = await request.json()
    # Вызов защищённого ядра
    result = dialogue_ring(data, {"stock": 10}, {"priority": 1}, max_iters=7)
    instruction = await generate_instruction(data, {}, result)
    return {"coherence": result, "instruction": instruction}
