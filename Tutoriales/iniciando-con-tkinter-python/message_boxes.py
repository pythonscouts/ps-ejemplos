import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Diálogo Tkinter")
root.geometry("300x200")


def show_message():
    messagebox.showinfo("Información", "Este es un mensaje informativo.")


tk.Button(root, text="Mostrar Mensaje", command=show_message).pack(pady=20)

root.mainloop()
