import tkinter as tk

def calc():
    name = n.get()
    age = 2024 - int(y.get())
    msg.config(text="Hello " + name + ", you are " + str(age))
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
tk.Label(root, text="Name:").grid(row=0, column=0)
n = tk.Entry(root)
n.grid(row=0, column=1)

tk.Label(root, text="Date:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

tk.Label(root, text="Month:").grid(row=2, column=0)
tk.Entry(root).grid(row=2, column=1)

tk.Label(root, text="Year:").grid(row=3, column=0)
y = tk.Entry(root)
y.grid(row=3, column=1)
tk.Button(root, text="Calculate", command=calc).grid(row=4, column=1)
msg = tk.Label(root, text="")
msg.grid(row=5, column=1)

root.mainloop()
