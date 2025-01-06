import tkinter as tk

root = tk.Tk()
root.title("Botones Tkinter")
root.geometry("190x240")

buttons = ["Ok", "Cancelar", "Aplicar", "Sí", "No", "Cerrar"]
for text in buttons:
    button = tk.Button(root, text=text)
    button.pack(fill="x", padx=5, pady=5)

root.mainloop()
