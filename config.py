import json
import os

# Назва файлу для збереження налаштувань
SETTINGS_FILE = "settings.json"

# Значення за замовчуванням
BG_COLOR = "#dddddd"
TEXTS = [
    "веселий / > чи продуктивний для мене",
    "нейтральний / > чи нічого б не втратив не подивившись",
    "поганий / > чи деградуючий для мене",
]
COLORS = ["#28b44b", "#ffeb00", "#b01217"]
TEXT_COLORS = ["black", "black", "black"]
BUTTON_OPTIONS = [
    ["приємні", "мотиваційні", "смішні", "пізнавальний"],               
    [],                
    ["Інше"]  
]

# Функція для завантаження налаштувань з файлу
def load_settings():
    global BG_COLOR, TEXTS, COLORS, TEXT_COLORS, BUTTON_OPTIONS
    
    if not os.path.exists(SETTINGS_FILE):
        return

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            BG_COLOR = data.get("BG_COLOR", BG_COLOR)
            TEXTS = data.get("TEXTS", TEXTS)
            COLORS = data.get("COLORS", COLORS)
            TEXT_COLORS = data.get("TEXT_COLORS", TEXT_COLORS)
            BUTTON_OPTIONS = data.get("BUTTON_OPTIONS", BUTTON_OPTIONS)
    except Exception:
        pass

# Функція для збереження налаштувань у файл
def save_settings():
    data = {
        "BG_COLOR": BG_COLOR,
        "TEXTS": TEXTS,
        "COLORS": COLORS,
        "TEXT_COLORS": TEXT_COLORS,
        "BUTTON_OPTIONS": BUTTON_OPTIONS
    }
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

load_settings()