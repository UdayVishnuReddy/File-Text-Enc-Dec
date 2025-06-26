import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt(text):
    return text[::-1]

def decrypt(text):
    return text[::-1]

def process_file(mode):
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text Files", "*.txt")])
    
    if not file_path:
        return
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        if mode == 'encrypt':
            processed = encrypt(content)
            output_file = "encrypted_" + file_path.split("/")[-1]
        else:
            processed = decrypt(content)
            output_file = "decrypted_" + file_path.split("/")[-1]

        with open(output_file, 'w') as file:
            file.write(processed)

        messagebox.showinfo("Success", f"File saved as '{output_file}'")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Window setup
window = tk.Tk()
window.title("File Encryption & Decryption")
window.geometry("300x150")

tk.Label(window, text="Choose an Option:").pack(pady=10)

tk.Button(window, text="Encrypt File", command=lambda: process_file('encrypt')).pack(pady=5)
tk.Button(window, text="Decrypt File", command=lambda: process_file('decrypt')).pack(pady=5)

window.mainloop()
