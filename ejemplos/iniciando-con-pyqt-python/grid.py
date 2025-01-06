import tkinter as tk

root = tk.Tk()
root.title("Disposición en cuadrícula")

positions = ["Botón (0, 0)", "Botón (0, 1)", "Botón (1, 0)", "Botón (1, 1)"]
for i, name in enumerate(positions):
    button = tk.Button(root, text=name)
    button.grid(row=i // 2, column=i % 2, padx=5, pady=5)

button = tk.Button(root, text="Botón (2, 0) + 2 Columnas de Amplitud")
button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
