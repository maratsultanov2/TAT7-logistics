import httpx

GIGACHAT_URL = "https://gigachat.devices.sberbank.ru/v1/chat/completions"
HEADERS = {"Authorization": "Bearer your_api_key"}

async def generate_instruction(payload: dict, stock_data: dict) -> str:
    items_text = []
    for item in payload.get("items", []):
        sku = item["sku"]
        info = stock_data.get(sku, {})
        items_text.append(f"Товар {sku}: {item['qty']} шт., место {info.get('location', 'неизвестно')}")
    
    prompt = f"Накладная №{payload.get('doc_number')} ({payload.get('customer')}).\n" + "\n".join(items_text)
    
    async with httpx.AsyncClient(headers=HEADERS) as client:
        response = await client.post(GIGACHAT_URL, json={"messages": [{"role": "user", "content": prompt}]})
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Инструкция не сгенерирована")
