import tkinter as tk
import config

def open_language_selector(parent, on_change_callback):
    selector = tk.Toplevel(parent)
    selector.title("Language / Мова / Idioma")
    selector.geometry("360x230")
    selector.configure(bg=config.BG_COLOR)

    selector.transient(parent)             
    selector.attributes("-topmost", True)  
    selector.focus_force()

    selector.grab_set()

    if not config.CURRENT_LANG:
        def disable_close():
            pass
        selector.protocol("WM_DELETE_WINDOW", disable_close)

    selector.grab_set()

    languages = [
        ("🇺🇦 Українська", "ua"),
        ("🇬🇧 English", "en"),
        ("🇪🇸 Español", "es")
    ]

    def set_lang(code):
        config.load_language(code)

        if not config.TEXTS:
            config.TEXTS = list(config.DEFAULT_TEXTS.get(code, config.DEFAULT_TEXTS["ua"]))
            config.COLORS = list(config.DEFAULT_COLORS)
            config.TEXT_COLORS = list(config.DEFAULT_T_COLORS)
            config.BUTTON_OPTIONS = list(config.DEFAULT_OPTIONS.get(code, config.DEFAULT_OPTIONS["ua"]))
            
        config.save_settings()
        on_change_callback()
        selector.destroy()
    
    tk.Frame(selector, bg=config.BG_COLOR, height=15).pack()

    for name, code in languages:
        btn_bg = "#ffffff" if config.CURRENT_LANG != code else "#d1e7ff"
        tk.Button(selector, text=name, font=("Arial", 11), bg=btn_bg, width=20,
                  command=lambda c=code: set_lang(c)).pack(pady=5)
    
    tk.Label(
        selector, 
        text=config.get_text("language_selector.warning"), 
        font=("Arial", 10, "bold"), 
        fg="red",
        bg=config.BG_COLOR,
        wraplength=300,
        pady=10
    ).pack()