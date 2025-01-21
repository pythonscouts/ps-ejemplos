import tkinter as tk

root = tk.Tk()
root.title("Disposición vertical")
root.geometry("290x130")

buttons = ["Arriba", "Centro", "Abajo"]
for position in buttons:
    button = tk.Button(root, text=position)
    button.pack(fill="x", padx=5, pady=5)

root.mainloop()
