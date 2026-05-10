async def generate_instruction(payload, stock_data, coherence_result):
    if coherence_result['success']:
        return f"✅ Инструкция (когерентность {coherence_result['coherence']:.2f}): Перемести {payload.get('qty',1)} шт."
    return f"⚠️ Требуется ручная проверка: {coherence_result['suggestion']}