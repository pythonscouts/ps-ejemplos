import tkinter as tk

root = tk.Tk()
root.title("Disposición horizontal")
root.geometry("290x80")

buttons = ["Izquierda", "Centro", "Derecha"]
for position in buttons:
    button = tk.Button(root, text=position)
    button.pack(side="left", expand=True, padx=5, pady=5)

root.mainloop()
