import tkinter as tk
from tkinter import messagebox

# a. Membuat aplikasi GUI
root = tk.Tk()
root.title("Aplikasi GUI Sederhana")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Masukkan Nama", font=("Arial", 12))
label.pack(pady=10)

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# b. Fungsi menampilkan isi Entry
def tampilkan_text():
    teks = entry.get()
    if teks:
        messagebox.showinfo("Pesan", teks)
    else:
        messagebox.showwarning("Peringatan", "Entry masih kosong")

# c. Fungsi menghapus isi Entry
def hapus_text():
    entry.delete(0, tk.END)

# Button tampilkan
btn_tampil = tk.Button(root, text="Tampilkan", command=tampilkan_text)
btn_tampil.pack(pady=5)

# Button hapus
btn_hapus = tk.Button(root, text="Hapus", command=hapus_text)
btn_hapus.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
