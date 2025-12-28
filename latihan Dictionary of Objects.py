# a. Membuat class Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"


# b. Dictionary untuk menyimpan objek pelanggan
data_pelanggan = {}


# c. Fungsi tambah, hapus, dan cari pelanggan
def tambah_pelanggan(data, pelanggan):
    data[pelanggan.id_pelanggan] = pelanggan


def hapus_pelanggan(data, id_pelanggan):
    if id_pelanggan in data:
        del data[id_pelanggan]


def cari_pelanggan(data, id_pelanggan):
    return data.get(id_pelanggan)


# ===== Program Utama =====

# Menambah pelanggan
tambah_pelanggan(data_pelanggan, Pelanggan("PL001", "Ahmad", "ahmad@email.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL002", "Budi", "budi@email.com"))
tambah_pelanggan(data_pelanggan, Pelanggan("PL003", "Citra", "citra@email.com"))

# d. Menampilkan seluruh daftar pelanggan
print("=== Daftar Pelanggan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())

# Mencari pelanggan
print("\n=== Pencarian Pelanggan ===")
hasil = cari_pelanggan(data_pelanggan, "PL002")
if hasil:
    print("Pelanggan ditemukan:")
    print(hasil.info())
else:
    print("Pelanggan tidak ditemukan")

# Menghapus pelanggan
hapus_pelanggan(data_pelanggan, "PL001")

# Menampilkan data setelah penghapusan
print("\n=== Daftar Pelanggan Setelah Penghapusan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())

# e. Capture hasil eksekusi dan simpan di GitHub (dilakukan setelah program dijalankan)
