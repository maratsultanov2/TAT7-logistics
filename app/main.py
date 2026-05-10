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

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from app.integrations.tat7 import dialogue_ring
from app.integrations.giga import generate_instruction

app = FastAPI(title="TAT-7 Logistics", version="4.2")

# Демо-страница
@app.get("/demo", response_class=HTMLResponse)
async def demo_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TAT-7 Logistics Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: system-ui, sans-serif; max-width: 800px; margin: 2rem auto; padding: 1rem; background: #0a0e27; color: #e0e0e0; }
            .card { background: #1a1f3a; border-radius: 24px; padding: 2rem; box-shadow: 0 8px 20px rgba(0,0,0,0.3); border: 1px solid #2a2f4a; }
            button { background: #7c3aed; color: white; border: none; padding: 12px 24px; border-radius: 40px; font-size: 16px; cursor: pointer; transition: 0.2s; margin-top: 1rem; }
            button:hover { background: #8b5cf6; transform: scale(1.02); }
            pre { background: #0a0e1a; padding: 1rem; border-radius: 16px; overflow-x: auto; border-left: 4px solid #7c3aed; }
            select, input { padding: 8px 12px; border-radius: 20px; border: 1px solid #2a2f4a; background: #0a0e1a; color: white; margin: 0 0.5rem; }
            .badge { background: #10b98120; color: #10b981; padding: 4px 12px; border-radius: 40px; font-size: 14px; }
            h1 { display: flex; align-items: center; gap: 12px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🧠 TAT-7 Logistics <span class="badge">Демо-прототип</span></h1>
            <p>Проверка когерентности накладной по 5 слоям: <strong>тема, роль, эмоция, смысл, цель</strong>.</p>
            <div style="margin: 1.5rem 0;">
                <label>Накладная: </label>
                <input type="text" id="doc" value="ТОРГ-12 №123" style="width: 60%;">
                <label>Роль: </label>
                <select id="role">
                    <option value="worker">Кладовщик</option>
                    <option value="chief">Начальник склада</option>
                </select>
            </div>
            <button onclick="runDemo()">🚀 Запустить проверку TAT-7</button>
            <div style="margin-top: 2rem;">
                <pre id="result">Нажмите кнопку — система проверит когерентность и даст инструкцию.</pre>
            </div>
        </div>
        <script>
        async function runDemo() {
            const doc = document.getElementById('doc').value;
            const role = document.getElementById('role').value;
            document.getElementById('result').innerText = "🔄 Анализ 5 слоёв...";
            try {
                const res = await fetch('/api/demo/tat7', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({doc_number: doc, user_role: role})
                });
                const data = await res.json();
                document.getElementById('result').innerText = 
                    `📊 Когерентность: ${data.coherence_score} / 1.0\\n` +
                    `🔄 Итераций: ${data.iterations}\\n` +
                    `✅ Успех: ${data.success ? "Да" : "Нет"}\\n` +
                    `📋 Инструкция:\\n${data.instruction}`;
            } catch(e) {
                document.getElementById('result').innerText = "Ошибка: " + e.message;
            }
        }
        </script>
    </body>
    </html>
    """

# Демо-API, которое использует TAT-7
@app.post("/api/demo/tat7")
async def demo_tat7(payload: dict):
    # Моковые данные для демонстрации
    stock_data = {"stock": 12, "location": "A-12-3", "sku": "TEST-001"}
    zone_data = {"priority": 1, "zone": "A"}
    
    result = dialogue_ring(payload, stock_data, zone_data, max_iters=7)
    instruction = await generate_instruction(payload, stock_data, result)
    
    return {
        "coherence_score": round(result.get("coherence", 0.0), 3),
        "iterations": result.get("iterations", 0),
        "success": result.get("success", False),
        "instruction": instruction
    }

# Оригинальный эндпоинт для вебхука (сохранён для обратной совместимости)
@app.post("/webhook/tat7")
async def tat7_processor(request: Request):
    data = await request.json()
    stock_data = {"stock": 10}
    zone_data = {"priority": 1}
    result = dialogue_ring(data, stock_data, zone_data, max_iters=7)
    instruction = await generate_instruction(data, stock_data, result)
    return {"coherence": result, "instruction": instruction}

@app.get("/")
def root():
    return {"status": "ok", "message": "TAT-7 Logistics running", "demo": "/demo"}
