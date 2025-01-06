import tkinter as tk

root = tk.Tk()
root.title("Botones radiales Tkinter")
root.geometry("250x150")

label = tk.Label(root, text="¿Qué prefieres?")
label.pack(pady=5)

foods = ["Pizza", "Hamburguesa", "Pasta", "Pollo asado"]
selected_food = tk.StringVar(root, foods[0])

for food in foods:
    radio = tk.Radiobutton(
        root,
        text=food,
        variable=selected_food,
        value=food,
    )
    radio.pack(anchor="w", padx=5)

root.mainloop()
