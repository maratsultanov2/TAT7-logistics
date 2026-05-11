
# TAT-7 Logistics

Когерентная логистика: 1С + Excel + TAT-7 + GigaChat + Битрикс24 + Честный знак
## 🧠 TAT-7 Logistics: Architecture Priority and Prior Art

**Author:** Marat Sultanov (@maratsultanov2)  
**Date of first public disclosure:** May 2026  
**Repository:** https://github.com/maratsultanov2/TAT7-logistics  
**Mirror:** https://gitverse.ru/maratsultanov2/TAT-7-logistics  
**Licenses:** Code — AGPL‑3.0, Data/weights — CC BY‑NC‑ND 4.0

---

### 1. What is being protected

This repository contains the first public description and implementation of a **coherent logistics architecture** for warehouse automation based on the TAT-7 core.

The protected novel elements include:

| Element | Description |
|---------|-------------|
| **Five‑layer coherence for logistics** | Theme (document type), role (user permissions), emotion (urgency/deviation), meaning (business intent), goal (target warehouse state). |
| **Dialogue ring in logistics** | Iterative reconciliation (up to 7 cycles) between 1С, Excel, and physical scanner data until coherence ≥0.5. |
| **TAT-7 as a logistics gateway** | A middleware that ingests data from 1С, Excel, and Bitrix24, applies coherence checks, and generates human‑readable instructions via GigaChat (or local fallback). |
| **Role‑based access in coherence layer** | Storekeeper sees only his zones; warehouse chief sees all data — enforced at the coherence stage, not just in UI. |
| **Fallback instruction generation** | Jinja2‑based template when GigaChat is unavailable — ensures warehouse operation continues offline. |
| **Adaptive weights for logistics** | Self‑adjusting coefficients for the five layers based on human feedback (confirm / ignore / correct). |
| **Lightweight deployment** | Optimised for Infinix Smart 6 HD (2GB RAM), runs via Termux or Docker on a low‑end server. |

---

### 2. Why this matters (priority claim)

- **First disclosure:** The architecture and its components were published in this repository in May 2026, with earlier discussions in issues #15 and #1121.
- **Independent work:** All logistics‑specific implementations (1С, Excel, Битрикс24 integration) were created by Marat Sultanov without access to non‑public vendor roadmaps.
- **Prior art:** Any subsequent public claim of a coherence‑based warehouse AI gateway will have to reference this repository as prior art.

---

### 3. How to cite or use

- **Code** (FastAPI, integrations, fallback templates): AGPL‑3.0 — you may use and modify, but modifications must be open sourced.
- **Data and weights** (adaptive weight settings, layer configurations): CC BY‑NC‑ND 4.0 — free for non‑commercial testing. Commercial use requires a separate license from the author.

**For commercial licensing or integration support:** maratsultanov2@gmail.com / Telegram @Marat_Sultanow

---

### 4. Legal notice (prior art protection)

This document serves as a **public prior art disclosure** for the described architectural patterns in warehouse logistics (five‑layer coherence, dialogue ring, TAT-7 logistics gateway, role‑based coherence, fallback instruction generation, adaptive weights for logistics). In case of any future patent or copyright dispute, the author can prove that these concepts were published and accessible before any conflicting claim.

*Last update: 12 May 2026*

## Быстрый старт

1. Клонируй репозиторий
2. Установи зависимости: `pip install -r requirements.txt`
3. Заполни `.env`
4. Запусти: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Компоненты

- **1С** — остатки, цены, заказы
- **Excel** — зоны, приоритеты
- **TAT-7** — когерентность, кольцо диалога, адаптивные веса
- **GigaChat** — инструкции
- **Битрикс24** — задачи и роли
- **Честный знак** — проверка маркировки

## Лицензии

- Код: AGPL-3.0
- Данные: CC BY-NC-ND 4.0

## Контакты

Марат Султанов — Telegram @Marat_Sultanow  

# TAT-7 + 1С + Excel + Битрикс24: Интеллектуальная система управления складом

**Проект:** Промышленный прототип системы внутренней логистики на базе когерентного ядра TAT-7.
**Стек:** Python 3.10+, FastAPI, httpx, openpyxl, Jinja2.
**Назначение:** Автоматизация сборки, перемещения и контроля остатков с самообучением и отказоустойчивостью.

## 🚀 Ключевые особенности (УТП)
*   **TAT-7 Когерентность:** Проверка согласованности данных из 1С, Excel и физического мира. Адаптивные веса (самообучение).
*   **Отказоустойчивость:** Fallback-генерация инструкций (Jinja2) и локальный режим при потере связи.
*   **Внутренняя логистика:** Полный цикл «Задача → Перемещение → Подтверждение (ТСД) → Обновление 1С».
*   **Безопасность:** Ролевой доступ (кладовщик / начальник) на основе данных из Битрикс24.
*   **Легкость:** Оптимизировано для работы на слабом железе (Infinix Smart 6 HD).

## 📦 Структура проекта
```
tat7_1c_excel_b24/
├── .env.example        # Пример конфигурации (переименовать в .env)
├── README.md           # Этот файл
├── requirements.txt    # Зависимости
└── app/
    ├── main.py         # Точка входа (FastAPI)
    ├── api.py          # Бизнес-логика обработки накладных
    └── integrations/   # Модули интеграций
        ├── __init__.py
        ├── one_c.py     # Интеграция с 1С
        ├── excel.py     # Работа со справочниками Excel
        ├── giga.py      # Интеграция с GigaChat
        └── tat7.py      # Ядро когерентности TAT-7
    └── utils/
        └── logger.py    # Логирование
    └── templates/      # Шаблоны для генерации документов
        └── instruction_fallback.txt
```

## ⚙️ Быстрый старт (на сервере или ПК)
> *Для запуска на телефоне используйте Termux + Python или Colab.*
1.  Установите зависимости: `pip install -r requirements.txt`
2.  Скопируйте `.env.example` в `.env` и заполните данные.
3.  Запустите сервер: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
4.  Настройте вебхук в Битрикс24 на ваш IP-адрес и порт `/webhook/bitrix24`.

## 📝 Лицензия
[MIT](LICENSE)
