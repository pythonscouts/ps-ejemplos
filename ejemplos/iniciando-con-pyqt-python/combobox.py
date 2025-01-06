import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Lista desplegable Tkinter")
root.geometry("250x100")

options = ["Tkinter", "PyQt", "PySide", "Kivy", "wxPython"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])

combobox = ttk.Combobox(
    root,
    textvariable=selected_option,
    values=options,
    state="readonly",
)
combobox.pack(pady=20)

root.mainloop()
