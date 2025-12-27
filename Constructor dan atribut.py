class Buku:
    # Class attribute (milik semua objek)
    perpustakaan = "Perpustakaan STITEK"

    # Constructor untuk menginisialisasi atribut objek
    def __init__(self, judul, penulis, tahun):
        self.judul = judul       # Instance attribute
        self.penulis = penulis   # Instance attribute
        self.tahun = tahun       # Instance attribute

    # Method untuk menampilkan informasi buku
    def info_buku(self):
        return f"Buku '{self.judul}' oleh {self.penulis} ({self.tahun})"


# Instansiasi object (membuat objek buku)
buku1 = Buku("Pemrograman Python", "John Doe", 2023)
buku2 = Buku("Struktur Data", "Jane Doe", 2022)

# Menampilkan informasi buku
print(buku1.info_buku())
print(buku2.info_buku())

# Mengakses class attribute
print(f"Lokasi: {Buku.perpustakaan}")