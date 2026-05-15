import json
import os

SETTINGS_FILE = "settings.json"
LOCALES_DIR = "locales"

CURRENT_LANG = None
LANG_DATA = {}

# СТАНДАРТНІ НАЛАШТУВАННЯ 
DEFAULT_TEXTS = {
    "ua": [
        "веселий / > чи продуктивний для мене",
        "нейтральний / > чи нічого б не втратив не подивившись",
        "поганий / > чи деградуючий для мене",
    ],
    "en": [
        "good / > or productive for me",
        "neutral / > or wouldn't lose anything if I didn't watch",
        "bad / > or degrading for me",
    ],
    "es": [
        "bueno / > o productivo para mí",
        "neutral / > o no perdería nada si no lo viera",
        "malo / > o degradante para mí",
    ]
}
DEFAULT_COLORS = ["#28b44b", "#ffeb00", "#b01217"]
DEFAULT_T_COLORS = ["black", "black", "black"]
DEFAULT_OPTIONS = {
    "ua": [["приємні", "мотиваційні", "смішні", "пізнавальний"], [], ["Інше"]],
    "en": [["pleasant", "motivational", "funny", "educational"], [], ["Other"]],
    "es": [["agradables", "motivacionales", "divertidos", "educativos"], [], ["Otro"]]
}

# ПОТОЧНІ ЗМІННІ
BG_COLOR = "#dddddd"
TEXTS = []
COLORS = []
TEXT_COLORS = []
BUTTON_OPTIONS = []

def load_language(lang_code):
    global CURRENT_LANG, LANG_DATA
    if not lang_code:
        LANG_DATA = {}
        return
        
    file_path = os.path.join(LOCALES_DIR, f"{lang_code}.json")
    if not os.path.exists(file_path):
        lang_code = "en"
        file_path = os.path.join(LOCALES_DIR, "en.json")
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            LANG_DATA = json.load(f)
            CURRENT_LANG = lang_code
    except Exception as e:
        print(f"❌ LANGUAGE LOAD ERROR ({lang_code}.json): {e}")
        LANG_DATA = {}

def get_text(key_path, default=""):
    try:
        keys = key_path.split('.')
        value = LANG_DATA
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return default if default else key_path

def load_settings():
    global CURRENT_LANG, TEXTS, COLORS, TEXT_COLORS, BUTTON_OPTIONS
    
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                CURRENT_LANG = data.get("CURRENT_LANG", None)
        except Exception: pass

    if CURRENT_LANG:
        TEXTS = list(DEFAULT_TEXTS.get(CURRENT_LANG, DEFAULT_TEXTS["ua"]))
        COLORS = list(DEFAULT_COLORS)
        TEXT_COLORS = list(DEFAULT_T_COLORS)
        BUTTON_OPTIONS = list(DEFAULT_OPTIONS.get(CURRENT_LANG, DEFAULT_OPTIONS["ua"]))

        if not os.path.exists(SETTINGS_FILE):
            return

        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    TEXTS = data.get("TEXTS", TEXTS)
                    COLORS = data.get("COLORS", COLORS)
                    TEXT_COLORS = data.get("TEXT_COLORS", TEXT_COLORS)
                    BUTTON_OPTIONS = data.get("BUTTON_OPTIONS", BUTTON_OPTIONS)
            except Exception: pass
        
        load_language(CURRENT_LANG)

def save_settings():
    data = {
        "CURRENT_LANG": CURRENT_LANG,
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
    TEXTS = list(DEFAULT_TEXTS.get(CURRENT_LANG, DEFAULT_TEXTS["ua"]))
    COLORS = list(DEFAULT_COLORS)
    TEXT_COLORS = list(DEFAULT_T_COLORS)
    BUTTON_OPTIONS = list(DEFAULT_OPTIONS.get(CURRENT_LANG, DEFAULT_OPTIONS["ua"]))
    save_settings()

load_settings()