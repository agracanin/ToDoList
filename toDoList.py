
import tkinter as tk
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To Do List by Alen Gracanin")
root.configure(bg="#344e41")

# Task creation function


def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(
            title="Warning!", message="You must enter a task.")

# Task deletion function


def delete_task():
    try:
        task_i = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_i)
    except:
        tk.messagebox.showwarning(
            title="Warning!", message="Please select a task for deletion.")

# Save tasks function using pickle


def save_task():
    alltasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(alltasks, open("tasks.dat", "wb"))

# Load tasks function using pickle


def load_task():
    try:
        alltasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tk.END)
        for task in alltasks:
            listbox_tasks.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(
            title="Warning!", message="No saved tasks found.")


# GUI Creation
frame = tk.Frame(root)
frame.pack()
root.configure(bg='#2b2d42')

listbox_tasks = tk.Listbox(frame, height=10, width=60,
                           bg='#2b2d42', fg='#edf2f4')
listbox_tasks.pack(side=tk.LEFT)

entry_task = tk.Entry(root, width=40, bg='#edf2f4')
entry_task.pack(pady=(15, 15))

button_add_task = tk.Button(
    root, text="Add task", width=30, command=add_task, bg='#8d99ae', fg='#edf2f4')
button_add_task.pack()

button_delete_task = tk.Button(
    root, text="Delete task", width=30, command=delete_task, bg='#d90429', fg='#edf2f4')
button_delete_task.pack(pady=(5, 5))

button_save_task = tk.Button(
    root, text="Save tasks", width=30, command=save_task, bg='#8d99ae', fg='#edf2f4')
button_save_task.pack()

button_load_task = tk.Button(
    root, text="Load tasks", width=30, command=load_task, bg='#8d99ae', fg='#edf2f4')
button_load_task.pack(pady=(5, 15))

root.mainloop()
