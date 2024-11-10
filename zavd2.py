import tkinter as tk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - shift_base + shift) % 26 + shift_base
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_message():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_cipher(text, shift)
    result_label.config(text=f"Зашифрований текст: {encrypted_text}")

def decrypt_message():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_cipher(text, -shift)
    result_label.config(text=f"Розшифрований текст: {decrypted_text}")

root = tk.Tk()
root.title("Шифр Цезаря")
root.geometry("400x300")
root.configure(bg="lightblue")

label_text = tk.Label(root, text="Введіть текст:", bg="lightblue")
label_text.pack()
entry_text = tk.Entry(root, width=30)
entry_text.pack()

label_shift = tk.Label(root, text="Зсув:", bg="lightblue")
label_shift.pack()
entry_shift = tk.Entry(root, width=5)
entry_shift.pack()

button_encrypt = tk.Button(root, text="Зашифрувати", command=encrypt_message)
button_encrypt.pack()

button_decrypt = tk.Button(root, text="Розшифрувати", command=decrypt_message)
button_decrypt.pack()

result_label = tk.Label(root, text="", bg="lightblue")
result_label.pack()

root.mainloop()
