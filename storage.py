import json
import os
from datetime import datetime

DATA_FILE = "data.json"
SAVE_FOLDER = "save"

def load_data():
    if not os.path.exists(DATA_FILE):
        return [0, 0, 0], 0
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("counts", [0, 0, 0]), data.get("all_count", 0)
    except (json.JSONDecodeError, IOError):
        return [0, 0, 0], 0

def save_data(counts, all_count):
    data = {"counts": counts, "all_count": all_count}
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_daily_report(counts, all_count):
    # Отримуємо поточний час
    now = datetime.now()
    
    # Формуємо назву:
    # %Y-рік, %m-місяць, %d-день, %H-години, %M-хвилини
    filename = now.strftime("save_%Y_%m_%d_%H_%M.json")
    
    # Об'єднуємо з папкою: save/save_....json
    full_path = os.path.join(SAVE_FOLDER, filename)
    
    # Якщо папки save раптом немає, створимо її, щоб не було помилки
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    data = {
        "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
        "counts": counts,
        "all_count": all_count
    }
    
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    return full_path