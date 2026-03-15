import tkinter.messagebox as messagebox
import storage

counts = [0, 0, 0]
all_count = 0
sub_counts = [{}, {}, {}]

ui_label_all = None
ui_counter_labels = []

def init(label_all_widget, counter_labels_list, options_list):
    global ui_label_all, ui_counter_labels, counts, all_count, sub_counts
    
    ui_label_all = label_all_widget
    ui_counter_labels = counter_labels_list
    
    loaded_counts, loaded_all, loaded_sub = storage.load_data()
    all_count = loaded_all
    counts = loaded_counts
    
    if len(counts) > len(ui_counter_labels):
        counts = counts[:len(ui_counter_labels)]
    elif len(counts) < len(ui_counter_labels):
        counts.extend([0] * (len(ui_counter_labels) - len(counts)))
        
    sub_counts = []
    for i, opts in enumerate(options_list):
        current_dict = {}
        loaded_dict = loaded_sub[i] if i < len(loaded_sub) else {}
        for opt in opts:
            current_dict[opt] = loaded_dict.get(opt, 0)
        sub_counts.append(current_dict)
        
    update_ui()

def update_ui():
    if ui_label_all:
        ui_label_all.config(text=f"all: {all_count}")
    for i, lbl in enumerate(ui_counter_labels):
        lbl.config(text=str(counts[i]))

def get_sub_count(idx, option_name):
    return sub_counts[idx].get(option_name, 0)

def on_click(idx, option_name=None):
    global all_count
    counts[idx] += 1
    all_count += 1
    
    if option_name is not None and option_name in sub_counts[idx]:
        sub_counts[idx][option_name] += 1
    
    update_ui()
    storage.save_data(counts, all_count, sub_counts)

def perform_reset():
    global all_count, counts, sub_counts
    all_count = 0
    counts = [0] * len(ui_counter_labels)
    
    for d in sub_counts:
        for k in d.keys():
            d[k] = 0
            
    update_ui()
    storage.save_data(counts, all_count, sub_counts)

def on_reset_request():

    if messagebox.askyesno("Скидання", "Ви впевнені, що хочете обнулити лічильники?"):
        perform_reset()

def on_save_report():
    filename = storage.save_daily_report(counts, all_count, sub_counts)
    should_reset = messagebox.askokcancel(
        "Save in file", 
        f"Дані збережено у файл:\n{filename}\n\nБажаєте скинути лічильники?\n\n"
        f"'ОК', щоб почати з нуля.\n"
        f"'Cancel', щоб продовжити рахунок."
    )

    if should_reset:
        perform_reset()