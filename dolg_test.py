import tkinter as tk
from tkinter import ttk, messagebox
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                status, task = line.strip().split(";", 1)
                tasks.append({"task": task, "status": status == "True"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['status']};{task['task']}\n")

def add_task():
    task_description = new_task_entry.get()
    if task_description:
        tasks.append({"task": task_description, "status": False})
        update_task_list()
        new_task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, введите описание задачи.")

def toggle_complete(index):
    tasks[index]["status"] = not tasks[index]["status"]
    update_task_list()

def edit_task(index):
    def save_edit():
        new_description = edit_entry.get()
        if new_description:
            tasks[index]["task"] = new_description
            update_task_list()
            edit_window.destroy()
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, введите новое описание задачи.")

    edit_window = tk.Toplevel(root)
    edit_window.title("Редактировать задачу")

    edit_label = tk.Label(edit_window, text="Новое описание:")
    edit_label.pack(pady=5)

    edit_entry = tk.Entry(edit_window, width=40)
    edit_entry.insert(0, tasks[index]["task"])
    edit_entry.pack(pady=5)

    save_button = tk.Button(edit_window, text="Сохранить", command=save_edit)
    save_button.pack(pady=10)

def delete_task(index):
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить эту задачу?"):
        del tasks[index]
        update_task_list()

def update_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        task_frame = tk.Frame(task_list_frame)
        task_frame.pack(pady=2, fill=tk.X)

        status_text = "[x]" if task["status"] else "[ ]"
        task_label = tk.Label(task_frame, text=f"{status_text} {task['task']}", anchor=tk.W)
        task_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        complete_button = tk.Button(task_frame, text="Выполнено", command=lambda idx=i: toggle_complete(idx))
        complete_button.pack(side=tk.LEFT, padx=2)

        edit_button = tk.Button(task_frame, text="Редактировать", command=lambda idx=i: edit_task(idx))
        edit_button.pack(side=tk.LEFT, padx=2)

        delete_button = tk.Button(task_frame, text="Удалить", command=lambda idx=i: delete_task(idx))
        delete_button.pack(side=tk.LEFT, padx=2)

