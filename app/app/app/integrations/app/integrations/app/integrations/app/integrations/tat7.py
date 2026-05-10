COHERENCE_THRESHOLD = 0.5
MAX_ITERATIONS = 7

def check_coherence(stock_data, zones):
    issues = []
    for sku, info in stock_data.items():
        location_found = any(info["location"] in z.get("locations", "") for z in zones)
        if not location_found:
            issues.append(f"Товар {sku}: место {info['location']} не найдено в справочнике")
    return len(issues) == 0, issues
