import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# =========================
# Class Mahasiswa
# =========================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return (self.nim, self.nama, self.jurusan, self.ipk)

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# =========================
# Aplikasi GUI
# =========================
class AppMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Mahasiswa")
        self.root.geometry("850x600")

        self.data_mahasiswa = {}  # dictionary: key = NIM

        self.create_widgets()

    # =========================
    # GUI Components
    # =========================
    def create_widgets(self):
        # Frame Input
        frame_input = ttk.LabelFrame(self.root, text="Input Data Mahasiswa")
        frame_input.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_input, text="NIM").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(frame_input, text="Nama").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(frame_input, text="Jurusan").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(frame_input, text="IPK").grid(row=3, column=0, padx=5, pady=5)

        self.entry_nim = ttk.Entry(frame_input)
        self.entry_nama = ttk.Entry(frame_input)
        self.entry_jurusan = ttk.Entry(frame_input)
        self.entry_ipk = ttk.Entry(frame_input)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

        # Tombol CRUD
        frame_button = ttk.Frame(frame_input)
        frame_button.grid(row=0, column=2, rowspan=4, padx=10)

        ttk.Button(frame_button, text="Tambah", command=self.tambah).pack(fill="x", pady=2)
        ttk.Button(frame_button, text="Update IPK", command=self.update_ipk).pack(fill="x", pady=2)
        ttk.Button(frame_button, text="Hapus", command=self.hapus).pack(fill="x", pady=2)
        ttk.Button(frame_button, text="Export", command=self.export_data).pack(fill="x", pady=2)

        # Frame Search & Filter
        frame_search = ttk.LabelFrame(self.root, text="Pencarian & Filter")
        frame_search.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_search, text="Cari (NIM / Nama):").grid(row=0, column=0)
        self.entry_cari = ttk.Entry(frame_search)
        self.entry_cari.grid(row=0, column=1)
        ttk.Button(frame_search, text="Cari", command=self.cari).grid(row=0, column=2, padx=5)

        ttk.Label(frame_search, text="Filter Jurusan:").grid(row=1, column=0)
        self.entry_filter = ttk.Entry(frame_search)
        self.entry_filter.grid(row=1, column=1)
        ttk.Button(frame_search, text="Filter", command=self.filter_jurusan).grid(row=1, column=2, padx=5)
        ttk.Button(frame_search, text="Reset", command=self.tampilkan_semua).grid(row=1, column=3)

        # Treeview
        columns = ("NIM", "Nama", "Jurusan", "IPK")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Frame Info Tambahan
        frame_info = ttk.Frame(self.root)
        frame_info.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_info, text="Rata-rata IPK", command=self.rata_rata_ipk).pack(side="left", padx=5)
        ttk.Button(frame_info, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side="left", padx=5)

    # =========================
    # Validasi
    # =========================
    def validasi_input(self):
        if not self.entry_nim.get() or not self.entry_nama.get() \
           or not self.entry_jurusan.get() or not self.entry_ipk.get():
            messagebox.showwarning("Validasi", "Semua field harus diisi")
            return False

        try:
            ipk = float(self.entry_ipk.get())
            if ipk < 0 or ipk > 4:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "IPK harus angka 0 - 4")
            return False

        return True

    # =========================
    # CRUD Operations
    # =========================
    def tambah(self):
        if not self.validasi_input():
            return

        nim = self.entry_nim.get()
        if nim in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM sudah terdaftar")
            return

        mhs = Mahasiswa(
            nim,
            self.entry_nama.get(),
            self.entry_jurusan.get(),
            float(self.entry_ipk.get())
        )

        self.data_mahasiswa[nim] = mhs
        self.tampilkan_semua()
        self.clear_input()

    def update_ipk(self):
        nim = self.entry_nim.get()
        if nim not in self.data_mahasiswa:
            messagebox.showerror("Error", "NIM tidak ditemukan")
            return

        try:
            ipk_baru = float(self.entry_ipk.get())
        except ValueError:
            messagebox.showerror("Error", "IPK tidak valid")
            return

        self.data_mahasiswa[nim].update_ipk(ipk_baru)
        self.tampilkan_semua()

    def hapus(self):
        nim = self.entry_nim.get()
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            self.tampilkan_semua()
        else:
            messagebox.showerror("Error", "NIM tidak ditemukan")

    def cari(self):
        keyword = self.entry_cari.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if keyword in mhs.nim.lower() or keyword in mhs.nama.lower():
                self.tree.insert("", "end", values=mhs.info())

    def filter_jurusan(self):
        jurusan = self.entry_filter.get().lower()
        self.tree.delete(*self.tree.get_children())

        for mhs in self.data_mahasiswa.values():
            if jurusan in mhs.jurusan.lower():
                self.tree.insert("", "end", values=mhs.info())

    def tampilkan_semua(self):
        self.tree.delete(*self.tree.get_children())
        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", "end", values=mhs.info())

    # =========================
    # Fitur Tambahan
    # =========================
    def rata_rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"Rata-rata IPK: {rata:.2f}")

    def ipk_tertinggi(self):
        if not self.data_mahasiswa:
            return
        mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
        messagebox.showinfo("IPK Tertinggi",
                            f"{mhs.nama} ({mhs.nim}) - IPK: {mhs.ipk}")

    def export_data(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if not file:
            return

        with open(file, "w") as f:
            for mhs in self.data_mahasiswa.values():
                f.write(f"{mhs.nim}, {mhs.nama}, {mhs.jurusan}, {mhs.ipk}\n")

        messagebox.showinfo("Export", "Data berhasil diexport")

    def clear_input(self):
        self.entry_nim.delete(0, tk.END)
        self.entry_nama.delete(0, tk.END)
        self.entry_jurusan.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# =========================
# Main Program
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppMahasiswa(root)
    root.mainloop()
