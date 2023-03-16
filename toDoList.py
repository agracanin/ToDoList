
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
        tk.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Task deletion function
def delete_task():
    try:
        task_i = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_i)
    except:
        tk.messagebox.showwarning(title="Warning!", message="Please select a task for deletion.")

# Save tasks function using pickle
def save_task():
    alltasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(alltasks, open("tasks.dat", "wb"))

# Load tasks function using pickle
def load_task():
    try:
        alltasks = pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0, tk.END)
        for task in alltasks:
            listbox_tasks.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(title="Warning!", message="No saved tasks found.")

# GUI Creation
frame = tk.Frame(root)
frame.pack()

listbox_tasks = tk.Listbox(frame, height=10, width=50, bg="#344e41", fg="#dad7cd")
listbox_tasks.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, bg="#a3b18a", fg="#3a5a40")
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=add_task, bg="#344e41", fg="#dad7cd")
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete task", width=48, command=delete_task, bg="#344e41", fg="#dad7cd")
button_delete_task.pack()

button_save_task = tk.Button(root, text="Save tasks", width=48, command=save_task, bg="#344e41", fg="#dad7cd")
button_save_task.pack()

button_load_task = tk.Button(root, text="Load tasks", width=48, command=load_task, bg="#344e41", fg="#dad7cd")
button_load_task.pack()

root.mainloop()