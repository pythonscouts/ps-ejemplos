import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("200x100")
root.title("Mostrar Diálogo")


class Dialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Diálogo")
        self.geometry("300x200")

        # Hacer que sea modal
        self.transient(parent)
        self.grab_set()

        # Layout principal
        main_frame = ttk.Frame(self, padding=10)
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Layout del formulario
        form_frame = ttk.Frame(main_frame)
        form_frame.grid(row=0, column=0, sticky="ew")

        labels = ["Nombre:", "Edad:", "Ocupación:", "Dirección:"]
        for i, label in enumerate(labels):
            ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            ttk.Entry(form_frame).grid(row=i, column=1, sticky="ew", pady=5)

        # Expandir columnas
        form_frame.grid_columnconfigure(1, weight=1)

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, pady=10, sticky="ew")

        btn_ok = ttk.Button(button_frame, text="OK", command=self.destroy)
        btn_ok.grid(row=0, column=0, padx=5)

        btn_cancel = ttk.Button(button_frame, text="Cancelar", command=self.destroy)
        btn_cancel.grid(row=0, column=1, padx=5)

        # Centrar los botones
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)


def show_dialog():
    Dialog(root)


button = ttk.Button(root, text="Show Dialog!", command=show_dialog)
button.pack(pady=20)

root.mainloop()
