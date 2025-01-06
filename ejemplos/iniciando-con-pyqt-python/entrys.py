import tkinter as tk

root = tk.Tk()
root.title("Campos de texto Tkinter")
root.geometry("250x120")

fields = ["Nombre", "Usuario", "Contraseña"]
for field in fields:
    entry = tk.Entry(root, foreground="lightgrey")
    entry.insert(0, field)
    entry.pack(padx=5, pady=5)

root.mainloop()
