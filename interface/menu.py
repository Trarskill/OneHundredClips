import tkinter as tk

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
        bg="#b3b3b3",
        bd=0,
        activebackground="#d9d9d9",
        cursor="hand2",
        command=show_menu
    )

    btn.place(relx=1.0, x=-20, y=20, anchor="ne")
    return btn