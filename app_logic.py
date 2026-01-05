import tkinter.messagebox as messagebox
import storage as storage

# --- Змінні стану ---
counts = [0, 0, 0]
all_count = 0

ui_label_all = None
ui_counter_labels = []

def init(label_all_widget, counter_labels_list):

    global ui_label_all, ui_counter_labels, counts, all_count
    
    ui_label_all = label_all_widget
    ui_counter_labels = counter_labels_list
    
    counts, all_count = storage.load_data()
    
    update_ui()

def update_ui():
    if ui_label_all:
        ui_label_all.config(text=f"all: {all_count}")
    
    for i, lbl in enumerate(ui_counter_labels):
        lbl.config(text=str(counts[i]))

def on_click(i):
    global all_count
    counts[i] += 1
    all_count += 1
    
    update_ui()
    storage.save_data(counts, all_count)

def perform_reset():
    global all_count, counts
    all_count = 0
    counts = [0, 0, 0]
    
    update_ui()
    storage.save_data(counts, all_count)

def on_reset_request():

    if messagebox.askyesno("Reset", "Підтверджуєте скидання?"):
        perform_reset()

def on_save_report():
    filename = storage.save_daily_report(counts, all_count)
    perform_reset()
    messagebox.showinfo("Save in file", f"Дані збережено у файл:\n{filename}\n\nВсі дані були автоматично скинуті!")