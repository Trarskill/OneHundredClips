import tkinter as tk
from interface.wrap_text import WrapText
from interface import menu
from interface.options_editor import open_options_editor
from interface.criteria_editor import open_criteria_editor
import app_logic
import config

# ----------------- вікно -----------------
root = tk.Tk()
root.title("OneHundredClips v0.4")
root.configure(bg=config.BG_COLOR)
root.geometry("920x440")
root.minsize(640, 360)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# ----------------- all -----------------
label_all = tk.Label(root, text="all: 0", font=("Times New Roman", 32, "bold"), bg=config.BG_COLOR)
label_all.grid(row=0, column=0, pady=(25, 15))

use_dropdown_var = tk.BooleanVar(value=True)

canvas_text_ids = []

# ----------------- функції -----------------
# Функція, яка оновлює текст на всіх кнопках
def update_button_texts():
    is_active = use_dropdown_var.get()
    
    for i, (canvas, text_id) in enumerate(canvas_text_ids):
        if is_active and len(config.BUTTON_OPTIONS[i]) > 0:
            new_text = "Select ▼"
        else:
            new_text = "click"
            
        canvas.itemconfig(text_id, text=new_text)

def rebuild_interface():
    for widget in grid.winfo_children():
        widget.destroy()
    canvas_text_ids.clear()
    counter_labels.clear()
    
    num_criteria = len(config.TEXTS)
    
    ideal_width = max(640, num_criteria * 310)
    root.geometry(f"{ideal_width}x460")
    root.minsize(num_criteria * 220, 360) 
    

    for c in range(5):
        grid.columnconfigure(c, weight=0, uniform="")

    for c in range(num_criteria):
        grid.columnconfigure(c, weight=1, uniform="col")

    # Створюємо кнопки заново
    for i in range(num_criteria):
        tk.Label(
            grid, text=WrapText(config.TEXTS[i]),
            font=("Times New Roman", 16, "bold"), 
            bg=config.BG_COLOR, justify="center"
        ).grid(row=0, column=i, sticky="nsew", padx=10)

        # Кнопка (Canvas)
        canvas = tk.Canvas(grid, bg=config.BG_COLOR, highlightthickness=0)
        canvas.grid(row=1, column=i, sticky="nsew", padx=15, pady=10)

        btn_id = rounded_rect(canvas, 0, 0, 0, 0, r=18, fill=config.COLORS[i], outline="", tags="btn_click")
        
        display_text = "Select ▼" if use_dropdown_var.get() and len(config.BUTTON_OPTIONS[i]) > 0 else "click"
        text_id = canvas.create_text(0, 0, text=display_text, font=("Arial", 14, "bold"), 
                                     fill=config.TEXT_COLORS[i], tags="btn_click")

        canvas_text_ids.append((canvas, text_id))
        canvas.bind("<Configure>", make_resize_handler(canvas, btn_id, text_id))
        canvas.tag_bind("btn_click", "<Button-1>", lambda e, idx=i: handle_button_click(e, idx))

        # Лічильник
        lbl = tk.Label(grid, text="0", font=("Times New Roman", 28, "bold"), bg=config.BG_COLOR)
        lbl.grid(row=2, column=i)
        counter_labels.append(lbl)

    # Переініціалізуємо логіку 
    app_logic.init(label_all, counter_labels, config.BUTTON_OPTIONS, root)

def rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = [
        x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2,
        x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# ----------------- меню -----------------

popup_menu = tk.Menu(root, tearoff=0, font=("Arial", 12))

popup_menu.add_checkbutton(
    label="🔠 Показувати списки вибору", 
    variable=use_dropdown_var, 
    command=update_button_texts
)
popup_menu.add_command(
    label="📝 Оновити список вибору", 
    command=lambda: open_options_editor(root, update_button_texts)
)

popup_menu.add_command(
    label="⚙️ Налаштування критеріїв", 
    command=lambda: open_criteria_editor(root, rebuild_interface)
)
popup_menu.add_command(label="💾 Зберегти в файл", command=app_logic.on_save_report)
popup_menu.add_command(label="🔄 Скинути лічильники", command=app_logic.on_reset_request)

popup_menu.add_separator()
popup_menu.add_command(label="❌ Вийти", command=app_logic.on_closing)

menu_btn = menu.create_hamburger_button(root, popup_menu)

# ----------------- Панель -----------------

counter_labels = []

num_criteria = len(config.TEXTS)

grid = tk.Frame(root, bg=config.BG_COLOR)
grid.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 20))

for c in range(num_criteria): 
    grid.columnconfigure(c, weight=1, uniform="col")

grid.rowconfigure(0, minsize=95)
grid.rowconfigure(1, weight=1, minsize=100)
grid.rowconfigure(2, minsize=60)

def show_dropdown(event, idx):
    dropdown = tk.Menu(root, tearoff=0, font=("Arial", 12))
    for option in config.BUTTON_OPTIONS[idx]:
        count = app_logic.get_sub_count(idx, option)
        label_text = f"{option}  ({count})"
        dropdown.add_command(label=label_text, command=lambda i=idx, opt=option: app_logic.on_click(i, opt))
    dropdown.tk_popup(event.x_root, event.y_root)
    
def handle_button_click(event, idx):
    if use_dropdown_var.get() and len(config.BUTTON_OPTIONS[idx]) > 0:
        show_dropdown(event, idx)
    else:
        app_logic.on_click(idx, None)

# Функція-фабрика, яка створює обробник зміни розміру для кожної кнопки
def make_resize_handler(cvs, btn_id, text_id):
    def on_resize(event):
        w, h = event.width, event.height
        if w < 40 or h < 40: return 
        
        pad = 10

        button_height = 85 
        
        y_center = h / 2
        y1 = y_center - (button_height / 2)
        y2 = y_center + (button_height / 2)
        
        if y1 < pad:
            y1 = pad
            y2 = h - pad
            
        x1 = pad
        x2 = w - pad
        r = 18 
        
        points = [
            x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2,
            x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1
        ]
        
        cvs.coords(btn_id, *points)
        cvs.coords(text_id, w / 2, h / 2)
        
    return on_resize

# ----------------- ІНІЦІАЛІЗАЦІЯ -----------------
rebuild_interface()

root.protocol("WM_DELETE_WINDOW", app_logic.on_closing)

root.mainloop()