import tkinter as tk
from tkinter import messagebox

def load_tasks():
    try:
        with open("Tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_task.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def save():
    with open("Tasks.txt", "w") as file:
        tasks = listbox_task.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = enter_task.get()
    if task:
        listbox_task.insert(tk.END, task)
        enter_task.delete(0, tk.END)
        save()
    else:
        messagebox.showwarning("Warning", "Task is empty")

def mark_task():
    try:
        selected_task_index = listbox_task.curselection()[0]
        task = listbox_task.get(selected_task_index)
        listbox_task.delete(selected_task_index)
        listbox_task.insert(selected_task_index, f"Completed: {task}")
        save()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task")

def del_task():
    try:
        selected_task_index = listbox_task.curselection()[0]
        listbox_task.delete(selected_task_index)
        save()
    except:
        messagebox.showwarning("Warning", "Please select  a task")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

enter_task = tk.Entry(root, width= 30)
enter_task.pack(pady= 10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

mark_button = tk.Button(btn_frame, text="Complete Task", command=mark_task)
mark_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Task", command=del_task)
delete_button.grid(row=0, column=2, padx=5)

listbox_task = tk.Listbox(root, width=40, height=20, selectmode=tk.SINGLE)
listbox_task.pack(pady=10)

load_tasks()

root.mainloop()
