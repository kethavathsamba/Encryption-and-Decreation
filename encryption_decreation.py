import string
import random
import tkinter as tk
from tkinter import messagebox, scrolledtext


def generate_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha() and char.islower():
            encrypted_text += key[char]
        elif char.isalpha() and char.isupper():
            encrypted_text += key[char.lower()].upper()
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha() and char.islower():
            decrypted_text += reverse_key[char]
        elif char.isalpha() and char.isupper():
            decrypted_text += reverse_key[char.lower()].upper()
        else:
            decrypted_text += char
    return decrypted_text


def open_encrypt_window():
    new_window = tk.Toplevel(window)
    new_window.title("Encryption")
    new_window.geometry("600x400")

    
    input_label = tk.Label(new_window, text="Input Text for Encryption:")
    input_label.pack(pady=5)
    input_text = scrolledtext.ScrolledText(new_window, width=70, height=5)
    input_text.pack()

    
    output_label = tk.Label(new_window, text="Encrypted Text:")
    output_label.pack(pady=5)
    output_text = scrolledtext.ScrolledText(new_window, width=70, height=5)
    output_text.pack()

    
    def perform_encryption():
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to encrypt!")
            return
        encrypted = encrypt(text, key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)

    
    encrypt_button = tk.Button(new_window, text="Encrypt", command=perform_encryption, bg="lightblue", width=15)
    encrypt_button.pack(pady=10)
    clear_button = tk.Button(new_window, text="Clear", command=lambda: (input_text.delete("1.0", tk.END), output_text.delete("1.0", tk.END)), bg="lightblue", width=15)
    clear_button.pack(pady=5)


def open_decrypt_window():
    new_window = tk.Toplevel(window)
    new_window.title("Decryption")
    new_window.geometry("600x400")

    
    input_label = tk.Label(new_window, text="Input Text for Decryption:")
    input_label.pack(pady=5)
    input_text = scrolledtext.ScrolledText(new_window, width=70, height=5)
    input_text.pack()

    
    output_label = tk.Label(new_window, text="Decrypted Text:")
    output_label.pack(pady=5)
    output_text = scrolledtext.ScrolledText(new_window, width=70, height=5)
    output_text.pack()

    def perform_decryption():
        text = input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to decrypt!")
            return
        decrypted = decrypt(text, key)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)

    
    decrypt_button = tk.Button(new_window, text="Decrypt", command=perform_decryption, bg="lightgreen", width=15)
    decrypt_button.pack(pady=10)
    clear_button = tk.Button(new_window, text="Clear", command=lambda: (input_text.delete("1.0", tk.END), output_text.delete("1.0", tk.END)), bg="lightgreen", width=15)
    clear_button.pack(pady=5)


key = generate_key()

window = tk.Tk()
window.title("NS Cryptify")
window.geometry("300x200")
window.resizable(False, False)

encrypt_button = tk.Button(window, text="Encrypt", command=open_encrypt_window, width=20, bg="lightblue")
encrypt_button.pack(pady=20)

decrypt_button = tk.Button(window, text="Decrypt", command=open_decrypt_window, width=20, bg="lightgreen")
decrypt_button.pack(pady=20)

window.mainloop() 