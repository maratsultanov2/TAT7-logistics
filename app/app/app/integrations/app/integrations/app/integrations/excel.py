import openpyxl
from typing import List, Dict

def load_zones(path: str) -> List[Dict]:
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0]:
            data.append({"zone": row[0], "locations": row[1], "priority": row[2]})
    wb.close()
    return data
