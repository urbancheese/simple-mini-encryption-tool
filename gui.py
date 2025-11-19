import tkinter as tk
from tkinter import ttk, messagebox
from test import caesar_cipher, xor_cipher, base64_encode, base64_decode, vigenere_cipher

class CryptoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Encryption Tool")
        self.root.geometry("400x650")
        
        self.is_dark_mode = False
        
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.dark_mode_btn = tk.Button(self.main_frame, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_btn.pack(anchor=tk.NE)
        
        self.input_label = tk.Label(self.main_frame, text="Input Text:")
        self.input_label.pack(pady=(5,0), anchor=tk.W)
        self.input_text = tk.Text(self.main_frame, height=5, width=40)
        self.input_text.pack(pady=5)
        self.input_text.bind('<KeyRelease>', self.update_char_count)
        
        self.char_count_label = tk.Label(self.main_frame, text="Characters: 0")
        self.char_count_label.pack(anchor=tk.E)
        
        self.cipher_label = tk.Label(self.main_frame, text="Select Cipher:")
        self.cipher_label.pack(pady=(5,0), anchor=tk.W)
        self.cipher_var = tk.StringVar()
        self.cipher_combo = ttk.Combobox(self.main_frame, textvariable=self.cipher_var)
        self.cipher_combo['values'] = ('Caesar Cipher', 'XOR Cipher', 'Base64', 'Vigenère Cipher')
        self.cipher_combo.current(0)
        self.cipher_combo.pack(pady=5, fill=tk.X)
        self.cipher_combo.bind("<<ComboboxSelected>>", self.update_inputs)
        
        self.key_label = tk.Label(self.main_frame, text="Shift (Integer):")
        self.key_label.pack(pady=(5,0), anchor=tk.W)
        self.key_entry = tk.Entry(self.main_frame)
        self.key_entry.pack(pady=5, fill=tk.X)
        
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=10)
        
        self.encrypt_btn = tk.Button(btn_frame, text="Encrypt / Encode", command=lambda: self.process(encrypt=True))
        self.encrypt_btn.pack(side=tk.LEFT, padx=5)
        
        self.decrypt_btn = tk.Button(btn_frame, text="Decrypt / Decode", command=lambda: self.process(encrypt=False))
        self.decrypt_btn.pack(side=tk.LEFT, padx=5)
        
        util_frame = tk.Frame(self.main_frame)
        util_frame.pack(pady=5)
        
        self.clear_btn = tk.Button(util_frame, text="Clear All", command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.copy_btn = tk.Button(util_frame, text="Copy Output", command=self.copy_output)
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        self.output_label = tk.Label(self.main_frame, text="Result:")
        self.output_label.pack(pady=(5,0), anchor=tk.W)
        self.output_text = tk.Text(self.main_frame, height=5, width=40)
        self.output_text.pack(pady=5)
        
        self.update_inputs()

    def update_char_count(self, event=None):
        text = self.input_text.get("1.0", tk.END).strip()
        count = len(text)
        self.char_count_label.config(text=f"Characters: {count}")

    def update_inputs(self, event=None):
        cipher = self.cipher_var.get()
        if cipher == 'Caesar Cipher':
            self.key_label.config(text="Shift (Integer):")
            self.key_entry.config(state='normal')
        elif cipher == 'XOR Cipher':
            self.key_label.config(text="Key (String):")
            self.key_entry.config(state='normal')
        elif cipher == 'Base64':
            self.key_label.config(text="Key (Not used):")
            self.key_entry.delete(0, tk.END)
            self.key_entry.config(state='disabled')
        elif cipher == 'Vigenère Cipher':
            self.key_label.config(text="Key (String):")
            self.key_entry.config(state='normal')

    def process(self, encrypt):
        cipher = self.cipher_var.get()
        text = self.input_text.get("1.0", tk.END).strip()
        key_val = self.key_entry.get().strip()
        
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text.")
            return
            
        result = ""
        try:
            if cipher == 'Caesar Cipher':
                try:
                    shift = int(key_val)
                    result = caesar_cipher(text, shift, decrypt=not encrypt)
                except ValueError:
                    messagebox.showerror("Input Error", "Shift must be an integer.")
                    return
            elif cipher == 'XOR Cipher':
                if not key_val:
                    messagebox.showwarning("Input Error", "Please enter a key.")
                    return
                result = xor_cipher(text, key_val)
            elif cipher == 'Base64':
                if encrypt:
                    result = base64_encode(text)
                else:
                    result = base64_decode(text)
            elif cipher == 'Vigenère Cipher':
                if not key_val:
                    messagebox.showwarning("Input Error", "Please enter a key.")
                    return
                result = vigenere_cipher(text, key_val, decrypt=not encrypt)
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
            
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.key_entry.delete(0, tk.END)
        self.update_char_count()

    def copy_output(self):
        text = self.output_text.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("Success", "Output copied to clipboard!")

    def toggle_dark_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        
        bg_color = "#2e2e2e" if self.is_dark_mode else "SystemButtonFace"
        fg_color = "white" if self.is_dark_mode else "black"
        text_bg = "#404040" if self.is_dark_mode else "white"
        text_fg = "white" if self.is_dark_mode else "black"
        
        self.root.config(bg=bg_color)
        self.main_frame.config(bg=bg_color)
        
        widgets = [
            self.input_label, self.char_count_label, self.cipher_label, 
            self.key_label, self.output_label
        ]
        
        for widget in widgets:
            widget.config(bg=bg_color, fg=fg_color)
            
        text_widgets = [self.input_text, self.output_text, self.key_entry]
        for widget in text_widgets:
            widget.config(bg=text_bg, fg=text_fg, insertbackground=fg_color)
            
        style = ttk.Style()
        if self.is_dark_mode:
            style.theme_use('alt')
            style.configure("TCombobox", fieldbackground=text_bg, background=bg_color, foreground=fg_color)
        else:
            style.theme_use('vista')

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoApp(root)
    root.mainloop()
