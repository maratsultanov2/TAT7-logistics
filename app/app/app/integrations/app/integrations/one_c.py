import httpx
from typing import Dict, Any

ONE_C_URL = "http://1c-server/api/v1"
HEADERS = {"Authorization": "Bearer your_token"}

async def get_1c_stock(doc_number: str) -> Dict[str, Any]:
    url = f"{ONE_C_URL}/get_items?doc_number={doc_number}"
    async with httpx.AsyncClient(headers=HEADERS) as client:
        response = await client.get(url)
        return response.json()
