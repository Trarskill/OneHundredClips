import tkinter as tk
from tkinter import colorchooser, messagebox
import config
import app_logic

def open_criteria_editor(parent, on_refresh_callback):
    editor = tk.Toplevel(parent)
    editor.title("Налаштування критеріїв")
    editor.configure(bg=config.BG_COLOR)
    editor.geometry("550x500")
    editor.grab_set()

    info_frame = tk.Frame(editor, bg=config.BG_COLOR)
    info_frame.pack(fill="x", padx=15, pady=(10, 0))

    def show_info():
        messagebox.showinfo(
            "Довідка по символах",
            "Правила форматування тексту критерію:\n\n"
            "• Символ  /  — це візуальний розділювач, використовується для зрічності чітання тексту.\n"
            "• Символ  >  — це прихований маркер переносу рядка. Він не відображається в інтерфейсі, але змушує текст після нього перенестися вниз."
        )

    info_btn = tk.Button(
        info_frame, text=" i ", font=("Arial", 11, "bold"), 
        bg="#2196F3", fg="white", relief="flat", command=show_info,
        padx=5, cursor="hand2"
    )
    info_btn.pack(side="right")
    
    tk.Label(
        info_frame, text="Список поточних критеріїв:", 
        font=("Arial", 11, "bold"), bg=config.BG_COLOR
    ).pack(side="left")

    temp_texts = list(config.TEXTS)
    temp_colors = list(config.COLORS)
    temp_t_colors = list(config.TEXT_COLORS)
    temp_options = list(config.BUTTON_OPTIONS)

    def choose_color(idx):
        color = colorchooser.askcolor(initialcolor=temp_colors[idx])[1]
        if color:
            temp_colors[idx] = color
            draw_list()

    def delete_item(idx):
        if len(temp_texts) <= 2:
            messagebox.showwarning("Увага", "Має бути хоча б 2 критерії.")
            return
        temp_texts.pop(idx)
        temp_colors.pop(idx)
        temp_t_colors.pop(idx)
        temp_options.pop(idx)
        draw_list()

    def add_item():
        if len(temp_texts) >= 5:
            messagebox.showwarning("Ліміт", "Максимум 5 критеріїв.")
            return
        temp_texts.append("Новий критерій")
        temp_colors.append("#888888") # Сірий за замовчуванням
        temp_t_colors.append("white")
        temp_options.append([])
        draw_list()

    def draw_list():
        for widget in list_frame.winfo_children():
            widget.destroy()
            
        for i in range(len(temp_texts)):
            row = tk.Frame(list_frame, bg=config.BG_COLOR)
            row.pack(fill="x", pady=5)
            
            ent = tk.Entry(row, font=("Arial", 11))
            ent.insert(0, temp_texts[i])
            ent.pack(side="left", fill="x", expand=True, padx=5)
            
            # Стрілочна функція для миттєвого оновлення тексту в temp_texts
            ent.bind("<KeyRelease>", lambda e, idx=i, entry=ent: temp_texts.__setitem__(idx, entry.get()))

            btn_color = tk.Button(row, bg=temp_colors[i], width=3, relief="flat", 
                                  command=lambda idx=i: choose_color(idx))
            btn_color.pack(side="left", padx=5)

            btn_del = tk.Button(row, text="🗑️", bg="#ff4d4d", fg="white", 
                                command=lambda idx=i: delete_item(idx))
            btn_del.pack(side="left", padx=5)

    list_frame = tk.Frame(editor, bg=config.BG_COLOR)
    list_frame.pack(fill="both", expand=True, padx=10, pady=10)

    add_btn = tk.Button(editor, text="+ Додати новий критерій", command=add_item, font=("Arial", 10, "bold"))
    add_btn.pack(pady=10)

    # Нижня панель
    bottom = tk.Frame(editor, bg=config.BG_COLOR)
    bottom.pack(side="bottom", fill="x", pady=20)

    def save():
        config.TEXTS = temp_texts
        config.COLORS = temp_colors
        config.TEXT_COLORS = temp_t_colors
        config.BUTTON_OPTIONS = temp_options
        config.save_settings()
        on_refresh_callback()
        editor.destroy()

    def reset():
        if messagebox.askyesno("Скидання", "Повернути до стандартних налаштувань?"):
            config.reset_to_defaults()
            on_refresh_callback()
            editor.destroy()

    tk.Button(bottom, text="Зберегти", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), 
              command=save, padx=20).pack(side="left", padx=30)
    tk.Button(bottom, text="Стандартні", bg="#555555", fg="white", font=("Arial", 11), 
              command=reset, padx=20).pack(side="right", padx=30)

    draw_list()