import tkinter as tk

BG_COLOR = "#dddddd"

def create_hamburger_button(root, menu_widget):
    def show_menu():
        try:
            x = btn.winfo_rootx()
            y = btn.winfo_rooty() + btn.winfo_height()

            menu_widget.tk_popup(x, y)
        finally:
            menu_widget.grab_release()

    btn = tk.Button(
        root,
        text="≡",
        font=("Arial", 20, "bold"),
        bg=BG_COLOR,
        bd=0,
        activebackground="#ffffff",
        cursor="hand2",
        command=show_menu
    )

    btn.place(relx=1.0, x=-20, y=20, anchor="ne")
    return btn