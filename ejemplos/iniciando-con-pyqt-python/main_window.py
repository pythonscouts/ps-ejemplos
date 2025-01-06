import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal Tkinter")
root.geometry("250x80")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Menú", menu=file_menu)

tk.Label(root, text="Soy el Widget Central").pack(pady=20)

root.mainloop()
