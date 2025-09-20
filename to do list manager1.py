import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# List to store tasks
tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    listbox.delete(0, tk.END)
    tasks.clear()

# GUI Components
title_label = tk.Label(root, text="To-Do List Manager", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), bg="#f44336", fg="white", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", font=("Helvetica", 12), bg="#FF9800", fg="white", command=clear_tasks)
clear_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Helvetica", 14), width=40, height=15)
listbox.pack(pady=20)

# Run the GUI
root.mainloop()
