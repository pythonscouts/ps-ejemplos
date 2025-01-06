import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Diálogo de Archivo Tkinter")
root.geometry("300x200")


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo(
            "Archivo Seleccionado",
            f"Seleccionaste: {file_path}",
        )


tk.Button(root, text="Abrir Archivo", command=open_file).pack(pady=20)

root.mainloop()
