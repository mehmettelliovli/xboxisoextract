import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# extract-xiso binary bu dosyanin bulunduğu klasörde
EXTRACT_XISO_PATH = os.path.join(os.path.dirname(__file__), "extract-xiso")

def select_iso():
    iso_path.set(filedialog.askopenfilename(
        title="Select ISO File",
        filetypes=[("ISO Files", "*.iso")]
    ))

def select_output():
    output_path.set(filedialog.askdirectory(title="Select Output Folder"))

def run_extract():
    iso = iso_path.get()
    out = output_path.get()

    if not iso or not out:
        messagebox.showerror("Hata", "Lütfen hem ISO dosyasını hem de hedef klasörü seçin.")
        return

    if not os.path.exists(EXTRACT_XISO_PATH):
        messagebox.showerror("Hata", f"'extract-xiso' dosyası bulunamadı:\n{EXTRACT_XISO_PATH}")
        return

    try:
        subprocess.run([EXTRACT_XISO_PATH, "-d", out, iso], check=True)
        messagebox.showinfo("Başarılı", "ISO başarıyla çıkarıldı!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Çıkarma işlemi başarısız oldu.\n\n{e}")

# GUI Penceresi
root = tk.Tk()
root.title("Xbox 360 ISO Extractor (macOS)")
root.geometry("520x200")
root.resizable(False, False)

iso_path = tk.StringVar()
output_path = tk.StringVar()

# ISO Seç
tk.Label(root, text="1. ISO Dosyasini Seç:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=iso_path, width=65).pack(padx=10)
tk.Button(root, text="Gözat", command=select_iso).pack(pady=5)

# Hedef Klasör Seç
tk.Label(root, text="2. Hedef Klasörü Seç:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=output_path, width=65).pack(padx=10)
tk.Button(root, text="Gözat", command=select_output).pack(pady=5)

# Extract Butonu
tk.Button(root, text="ISO'yu Çikar", command=run_extract,
          bg="#4CAF50", fg="white", width=20, height=2).pack(pady=10)

root.mainloop()
