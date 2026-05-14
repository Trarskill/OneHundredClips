import json
import os
from datetime import datetime
import tkinter.messagebox as messagebox
import config

DATA_FILE = "data.json"
SAVE_FOLDER = "save"

def load_data():
    if not os.path.exists(DATA_FILE):
        return [], 0, [] 
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            raw_counts = data.get("counts", [])
            parsed_counts = []
            for item in raw_counts:
                if isinstance(item, dict):
                    parsed_counts.append(list(item.values())[0])
                else:
                    parsed_counts.append(item)
                    
            return (
                parsed_counts, 
                data.get("all_count", 0),
                data.get("sub_counts", []) 
            )
    except (json.JSONDecodeError, IOError):
        now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        corrupted_name = f"data_corrupted_{now_str}.json"
        
        try:
            os.rename(DATA_FILE, corrupted_name)
            messagebox.showerror(
                "Помилка читання даних",
                f"Файл {DATA_FILE} було пошкоджено!\n\n"
                f"Щоб не втратити дані, його перейменовано на:\n{corrupted_name}\n\n"
                f"Програму запущено з нульовими лічильниками."
            )
        except Exception as e:
            messagebox.showerror("Помилка", f"Файл пошкоджено, і його не вдалося перейменувати: {e}")

        return [], 0, []

def get_formatted_counts(counts):
    formatted_counts = []
    for i, count in enumerate(counts):
        if i < len(config.TEXTS):
            name = config.TEXTS[i].split('/')[0].strip()
        else:
            name = f"Категорія {i+1}"
            
        formatted_counts.append({name: count})
    return formatted_counts

def save_data(counts, all_count, sub_counts):
    data = {
        "counts": get_formatted_counts(counts),
        "all_count": all_count,
        "sub_counts": sub_counts
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_daily_report(counts, all_count, sub_counts):
    now = datetime.now()
    filename = now.strftime("save_%Y_%m_%d_%H_%M.json")
    full_path = os.path.join(SAVE_FOLDER, filename)
    
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    data = {
        "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
        "counts": get_formatted_counts(counts),
        "all_count": all_count,
        "details": sub_counts
    }
    
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    return full_path