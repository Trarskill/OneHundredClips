import tkinter as tk
from tkinter import ttk
import src.config as config
import src.storage as storage

def open_history_viewer(parent):
    viewer = tk.Toplevel(parent)
    viewer.title(config.get_text("history_viewer.title"))
    viewer.geometry("900x500")
    viewer.configure(bg=config.BG_COLOR)
    viewer.grab_set()

    list_frame = tk.Frame(viewer, bg=config.BG_COLOR, width=250)
    list_frame.pack(side="left", fill="y", padx=10, pady=10)

    tk.Label(list_frame, text=config.get_text("history_viewer.select_file"), 
             bg=config.BG_COLOR, font=("Arial", 10, "bold")).pack(pady=5)

    file_listbox = tk.Listbox(list_frame, font=("Arial", 10), bg="white")
    file_listbox.pack(fill="both", expand=True)

    table_frame = tk.Frame(viewer, bg="white")
    table_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    columns = ("criteria", "count", "details")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")
    
    tree.heading("criteria", text=config.get_text("history_viewer.header_criteria"))
    tree.heading("count", text=config.get_text("history_viewer.header_count"))
    tree.heading("details", text=config.get_text("history_viewer.header_details"))

    tree.column("criteria", width=200)
    tree.column("count", width=70, anchor="center")
    tree.column("details", width=350)
    tree.pack(fill="both", expand=True)

    def on_file_select(event):
        selection = file_listbox.curselection()
        if not selection: return
        
        filename = file_listbox.get(selection[0])
        data = storage.load_report_file(filename)
        if not data: return

        for row in tree.get_children():
            tree.delete(row)

        raw_counts = data.get("counts", [])
        details = data.get("details", [])

        for i, item in enumerate(raw_counts):
            name = list(item.keys())[0] if isinstance(item, dict) else f"Cat {i+1}"
            val = list(item.values())[0] if isinstance(item, dict) else item
            
            sub_data = details[i] if i < len(details) else {}
            sub_str = ", ".join([f"{k} ({v})" for k, v in sub_data.items() if v > 0])
            
            tree.insert("", "end", values=(name, val, sub_str))

    file_listbox.bind("<<ListboxSelect>>", on_file_select)

    reports = storage.get_all_reports()
    if not reports:
        file_listbox.insert("end", config.get_text("history_viewer.no_files"))
    else:
        for r in reports:
            file_listbox.insert("end", r)