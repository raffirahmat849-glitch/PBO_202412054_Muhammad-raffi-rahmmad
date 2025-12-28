import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


# Class Tugas
class Tugas:
    def __init__(self, judul, selesai=False):
        self.judul = judul
        self.selesai = selesai


# Class Aplikasi GUI
class AplikasiTodo:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Tugas")
        self.root.geometry("600x400")

        # List of objects untuk menyimpan tugas
        self.daftar_tugas = []

        # ===== Frame Input =====
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Nama Tugas").grid(row=0, column=0, sticky=tk.W)
        self.entry_tugas = tk.Entry(frame_input, width=30)
        self.entry_tugas.grid(row=0, column=1, padx=5)

        tk.Button(frame_input, text="Tambah", command=self.tambah_tugas)\
            .grid(row=0, column=2, padx=5)

        # ===== Frame Tombol =====
        frame_tombol = tk.Frame(root, padx=10, pady=10)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Edit", command=self.edit_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Selesai", command=self.tandai_selesai)\
            .pack(side=tk.LEFT, padx=5)

        # ===== Treeview =====
        frame_tabel = tk.Frame(root, padx=10, pady=10)
        frame_tabel.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(
            frame_tabel,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            frame_tabel, orient=tk.VERTICAL, command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Tambah Tugas =====
    def tambah_tugas(self):
        judul = self.entry_tugas.get()
        if judul:
            tugas = Tugas(judul)
            self.daftar_tugas.append(tugas)
            self.tree.insert("", tk.END, values=(judul, "Belum"))
            self.entry_tugas.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Nama tugas tidak boleh kosong")

    # ===== Hapus Tugas =====
    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.tree.delete(selected[0])
            self.daftar_tugas.pop(index)
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu")

    # ===== Edit Tugas =====
    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]

            judul_baru = simpledialog.askstring(
                "Edit Tugas", "Masukkan nama tugas baru:", initialvalue=tugas.judul
            )
            if judul_baru:
                tugas.judul = judul_baru
                status = "Selesai" if tugas.selesai else "Belum"
                self.tree.item(selected[0], values=(judul_baru, status))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu")

    # ===== Tandai Selesai =====
    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            tugas = self.daftar_tugas[index]
            tugas.selesai = True
            self.tree.item(selected[0], values=(tugas.judul, "Selesai"))
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu")


# ===== Program Utama =====
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTodo(root)
    root.mainloop()

