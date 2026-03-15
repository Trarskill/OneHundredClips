import tkinter as tk
from interface.button_stylistic import rounded_rect
from interface.wrap_text import WrapText
from interface import menu
import app_logic

BG_COLOR = "#dddddd"

# ----------------- вікно -----------------
root = tk.Tk()
root.title("OneHundredClips v0.2")
root.configure(bg=BG_COLOR)
root.minsize(800, 400)

root.columnconfigure((0, 1, 2), weight=1)
root.rowconfigure((0, 1, 2, 3), weight=1)

# ----------------- all -----------------
label_all = tk.Label(root, text="all: 0", font=("Times New Roman", 32, "bold"), bg=BG_COLOR)
label_all.grid(row=0, column=0, columnspan=3, pady=15)

use_dropdown_var = tk.BooleanVar(value=True)

# ----------------- меню -----------------
popup_menu = tk.Menu(root, tearoff=0, font=("Arial", 12))

popup_menu.add_checkbutton(label="🔠 Показувати списки вибору", variable=use_dropdown_var)
popup_menu.add_command(label="💾 SAVE in file", command=app_logic.on_save_report)
popup_menu.add_command(label="🔄 Reset", command=app_logic.on_reset_request)

popup_menu.add_separator()
popup_menu.add_command(label="❌ Exit", command=root.quit)

menu_btn = menu.create_hamburger_button(root, popup_menu)

# ----------------- параметри -----------------
texts = [
    "веселий / > чи продуктивний для мене",
    "нейтральний / > чи нічого б не втратив не подивившись",
    "поганий / > чи деградуючий для мене",
]
# texts = [
#     "Короткий текст",
#     "Дуже довгий текст який не повинен ламати інтерфейс",
#     "Ще один надзвичайно довгий підпис кнопки",
# ]
colors = ["#28b44b", "#ffeb00", "#b01217"]
text_colors = ["black", "black", "black"]

button_options = [
    ["приємні", "мотиваційні", "смішні", "пізнавальний"],               
    [],                
    ["Інше"]  
]

counter_labels = []

grid = tk.Frame(root, bg=BG_COLOR)
grid.grid(row=1, column=0, columnspan=3, sticky="nsew")

for c in range(3):
    grid.columnconfigure(c, weight=1, uniform="col")

grid.rowconfigure(0, minsize=80)
grid.rowconfigure(1, minsize=100)
grid.rowconfigure(2, minsize=60)

def show_dropdown(event, idx):
    dropdown = tk.Menu(root, tearoff=0, font=("Arial", 12))
    for option in button_options[idx]:
        count = app_logic.get_sub_count(idx, option)
        label_text = f"{option}  ({count})"
        dropdown.add_command(label=label_text, command=lambda i=idx, opt=option: app_logic.on_click(i, opt))
    dropdown.tk_popup(event.x_root, event.y_root)
    
def handle_button_click(event, idx):
    if use_dropdown_var.get() and len(button_options[idx]) > 0:
        show_dropdown(event, idx)
    else:
        app_logic.on_click(idx, None)

for i in range(3):
    tk.Label(
        grid, 
        text=WrapText(texts[i]),
        font=("Times New Roman", 16, "bold"), 
        bg=BG_COLOR, 
        anchor="center", 
        justify="center"
    ).grid(row=0, column=i, sticky="nsew", padx=10)

    # Малюємо красиві кнопки
    canvas = tk.Canvas(grid, width=180, height=70, bg=BG_COLOR, highlightthickness=0)
    canvas.grid(row=1, column=i)

    btn = rounded_rect(
        canvas, 10, 10, 170, 60,
        r=18,
        fill=colors[i],
        outline="",
        tags="btn_click"
    )

    display_text = "Select ▼" if len(button_options[i]) > 0 else "click"

    arrow = canvas.create_text(85, 35, text=display_text, font=("Arial", 14, "bold"), fill=text_colors[i], tags="btn_click")

    canvas.tag_bind("btn_click", "<Button-1>", lambda e, idx=i: handle_button_click(e, idx))

    # Лічильник
    lbl = tk.Label(grid, text="0", font=("Times New Roman", 28, "bold"), bg=BG_COLOR)
    lbl.grid(row=2, column=i)
    counter_labels.append(lbl)

# ----------------- ІНІЦІАЛІЗАЦІЯ -----------------
app_logic.init(label_all, counter_labels, button_options)

root.mainloop()