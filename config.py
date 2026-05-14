import json
import os

SETTINGS_FILE = "settings.json"

# СТАНДАРТНІ НАЛАШТУВАННЯ
DEFAULT_TEXTS = [
    "веселий / > чи продуктивний для мене",
    "нейтральний / > чи нічого б не втратив не подивившись",
    "поганий / > чи деградуючий для мене",
]
DEFAULT_COLORS = ["#28b44b", "#ffeb00", "#b01217"]
DEFAULT_T_COLORS = ["black", "black", "black"]
DEFAULT_OPTIONS = [
    ["приємні", "мотиваційні", "смішні", "пізнавальний"],               
    [],                
    ["Інше"]  
]

# ПОТОЧНІ ЗМІННІ
BG_COLOR = "#dddddd"
TEXTS = []
COLORS = []
TEXT_COLORS = []
BUTTON_OPTIONS = []

def load_settings():
    global TEXTS, COLORS, TEXT_COLORS, BUTTON_OPTIONS
    TEXTS = list(DEFAULT_TEXTS)
    COLORS = list(DEFAULT_COLORS)
    TEXT_COLORS = list(DEFAULT_T_COLORS)
    BUTTON_OPTIONS = list(DEFAULT_OPTIONS)

    if not os.path.exists(SETTINGS_FILE):
        return

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            TEXTS = data.get("TEXTS", TEXTS)
            COLORS = data.get("COLORS", COLORS)
            TEXT_COLORS = data.get("TEXT_COLORS", TEXT_COLORS)
            BUTTON_OPTIONS = data.get("BUTTON_OPTIONS", BUTTON_OPTIONS)
    except Exception:
        pass

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

def reset_to_defaults():
    global TEXTS, COLORS, TEXT_COLORS, BUTTON_OPTIONS
    TEXTS = list(DEFAULT_TEXTS)
    COLORS = list(DEFAULT_COLORS)
    TEXT_COLORS = list(DEFAULT_T_COLORS)
    BUTTON_OPTIONS = list(DEFAULT_OPTIONS)
    save_settings()

load_settings()