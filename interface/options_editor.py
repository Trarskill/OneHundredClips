import tkinter as tk
import config
import app_logic

# Функція для відкриття вікна редагування опцій
def open_options_editor(parent, on_save_callback):
    editor = tk.Toplevel(parent)
    editor.title("Редагування списків вибору")
    editor.configure(bg=config.BG_COLOR)
    editor.geometry("750x380") 
    editor.minsize(600, 300)
    editor.grab_set()
    editor.columnconfigure((0, 1, 2), weight=1)

    entries_by_col = [] 

    for i in range(3):
        col_frame = tk.Frame(editor, bg=config.BG_COLOR)
        col_frame.grid(row=0, column=i, padx=15, pady=15, sticky="nsew")

        tk.Label(
            col_frame, 
            text=f"Категорія {i+1}", 
            bg=config.COLORS[i], 
            fg=config.TEXT_COLORS[i], 
            font=("Arial", 12, "bold")
        ).pack(fill="x", pady=(0, 10))

        col_entries = []
        for j in range(6):
            ent = tk.Entry(col_frame, font=("Arial", 11))
            ent.pack(fill="x", pady=3)
            
            if j < len(config.BUTTON_OPTIONS[i]):
                ent.insert(0, config.BUTTON_OPTIONS[i][j])
                
            col_entries.append(ent)
            
        entries_by_col.append(col_entries)

    def save_new_options():
        for i in range(3):
            new_opts = []
            for ent in entries_by_col[i]:
                val = ent.get().strip()
                if val: 
                    new_opts.append(val)
                    
            config.BUTTON_OPTIONS[i] = new_opts
            app_logic.update_sub_counts_keys(i, new_opts)

        config.save_settings()

        if on_save_callback:
            on_save_callback()
        editor.destroy()

    btn_frame = tk.Frame(editor, bg=config.BG_COLOR)
    btn_frame.grid(row=1, column=0, columnspan=3, pady=15, sticky="ew")
    
    save_btn = tk.Button(
        btn_frame, 
        text="Зберегти зміни", 
        command=save_new_options, 
        font=("Arial", 12, "bold"), 
        bg="#4CAF50", 
        fg="white", 
        padx=30, 
        pady=5)
    save_btn.pack()