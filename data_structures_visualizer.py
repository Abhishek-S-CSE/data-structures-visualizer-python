import tkinter as tk

stack = []
queue = []

def push_stack():
    value = entry.get()
    if value != "":
        stack.append(value)
        update_stack()

def pop_stack():
    if stack:
        stack.pop()
        update_stack()

def enqueue():
    value = entry.get()
    if value != "":
        queue.append(value)
        update_queue()

def dequeue():
    if queue:
        queue.pop(0)
        update_queue()

def update_stack():
    stack_list.delete(0, tk.END)
    for item in reversed(stack):
        stack_list.insert(tk.END, item)

def update_queue():
    queue_list.delete(0, tk.END)
    for item in queue:
        queue_list.insert(tk.END, item)

root = tk.Tk()
root.title("Data Structures Visualizer")

entry = tk.Entry(root)
entry.pack()

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Push Stack", command=push_stack).grid(row=0, column=0)
tk.Button(frame, text="Pop Stack", command=pop_stack).grid(row=0, column=1)
tk.Button(frame, text="Enqueue", command=enqueue).grid(row=1, column=0)
tk.Button(frame, text="Dequeue", command=dequeue).grid(row=1, column=1)

stack_list = tk.Listbox(root)
stack_list.pack()

queue_list = tk.Listbox(root)
queue_list.pack()

root.mainloop()
