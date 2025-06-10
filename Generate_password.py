import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    character = char_var.get()
    digit = digit_var.get()
    symbole = sym_var.get()
    try:
        k  = int(length_var.get())
    except ValueError:
        result_var.set("Invalid length")
        return
    pp=''
    if(character=="y"):
        pp+=string.ascii_letters
    if(digit=="y"):
        pp+=string.digits
    if(symbole=="y"):
        pp+=string.punctuation
    if(pp==""):
        print("No Choice selected")
        return
    password="".join(random.choices(pp, k=k ))
    result_var.set(password)
def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")
# gui setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.resizable(False, False)

char_var = tk.StringVar()
digit_var = tk.StringVar()
sym_var = tk.StringVar()
result_var = tk.StringVar()
length_var = tk.StringVar()

tk.Label(root, text="Enter (y/n) if you want to use characters:").pack()
tk.Entry(root, textvariable=char_var).pack()
tk.Label(root, text="Enter (y/n) if you want to use digits:").pack()
tk.Entry(root, textvariable=digit_var).pack()
tk.Label(root, text="Enter (y/n) if you want to use symbols:").pack()
tk.Entry(root, textvariable=sym_var).pack()
tk.Label(root, text= "Enter the length of password:").pack()
tk.Entry(root, textvariable=length_var).pack()
tk.Button(root, text="Generate Password", command=generate_password).pack()
tk.Label(root, text="Generated Password:").pack()
tk.Label(root, textvariable=result_var).pack()
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()
root.mainloop()