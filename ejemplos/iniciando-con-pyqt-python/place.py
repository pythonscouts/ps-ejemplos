import tkinter as tk

root = tk.Tk()
root.title("Disposición por posición")
root.geometry("300x200")

tk.Button(root, text="x=0, y=0").place(x=0, y=0)
tk.Button(root, text="x=50, y=50").place(x=50, y=50)
tk.Button(root, text="x=100, y=100").place(x=100, y=100)
tk.Button(root, text="x=150, y=150").place(x=150, y=150)

root.mainloop()
