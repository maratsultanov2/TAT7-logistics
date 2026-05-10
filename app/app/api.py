import time
from typing import Dict, Any
from .integrations.one_c import get_1c_stock
from .integrations.excel import load_zones
from .integrations.tat7 import check_coherence, MAX_ITERATIONS
from .integrations.giga import generate_instruction
from .utils.logger import log

EXCEL_PATH = "data/zones.xlsx"

async def process_shipment(payload: Dict[str, Any]) -> Dict[str, Any]:
    start_time = time.time()
    doc_number = payload.get("doc_number")
    
    log.info(f"Шаг 1/6: получена накладная {doc_number}")
    
    stock_data = await get_1c_stock(doc_number)
    zones = load_zones(EXCEL_PATH)
    
    for attempt in range(MAX_ITERATIONS):
        coherent, issues = check_coherence(stock_data, zones)
        if coherent:
            log.info(f"Когерентность достигнута за {attempt+1} итераций")
            break
        log.info(f"Итерация {attempt+1}: когерентность <0.5, пробуем снова")
    
    instruction = await generate_instruction(payload, stock_data)
    
    return {
        "instruction": instruction,
        "stock_data": stock_data,
        "time_elapsed": time.time() - start_time
  }
