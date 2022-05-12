import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To Do List")


def add_task():
    task = entry_task.get()
    # удаляет пробел между заданиями
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        # очищает бокс после занесения задания в главное окно
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")


def load_tasks():
    # rb - read binary
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Can not find tasks.dat")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    # сбрасывает список заданий в выбранную папку/файл wb - write binary
    pickle.dump(tasks, open("tasks.dat", "wb"))


# create GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

# scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

add_task_button = tkinter.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack()

delete_task_button = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
delete_task_button.pack()

load_tasks_button = tkinter.Button(root, text="Load Tasks", width=48, command=load_tasks)
load_tasks_button.pack()

save_tasks_button = tkinter.Button(root, text="Save Tasks", width=48, command=save_tasks)
save_tasks_button.pack()

root.mainloop()
