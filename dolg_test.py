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
