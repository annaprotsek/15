import tkinter as tk
from tkinter import messagebox
import math

def calculate_roots():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            result_label.config(text=f"Корені: x₁={root1:.2f}, x₂={root2:.2f}")
        elif discriminant == 0:
            root = -b / (2 * a)
            result_label.config(text=f"Єдиний корінь: x={root:.2f}")
        else:
            result_label.config(text="Коренів немає (дискримінант < 0)")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення.")

root = tk.Tk()
root.title("Квадратне рівняння")
root.geometry("400x300")
root.configure(bg="green")
label_a = tk.Label(root, text="a:", bg="green")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="b:", bg="green")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="c:", bg="green")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

button_calculate = tk.Button(root, text="Обчислити корені", command=calculate_roots)
button_calculate.pack()

result_label = tk.Label(root, text="", bg="green")
result_label.pack()
root.mainloop()
