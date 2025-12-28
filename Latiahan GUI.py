# a) Membuat class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


# b) List berisi 5 objek buku
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Sang Pemimpi", "Andrea Hirata", 2006),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Hujan", "Tere Liye", 2016)
]


# c) Fungsi mencari buku berdasarkan penulis
def cari_buku_penulis(daftar, penulis):
    hasil = []
    for buku in daftar:
        if buku.penulis.lower() == penulis.lower():
            hasil.append(buku)
    return hasil


# d) Menampilkan hasil pencarian
penulis_dicari = "Andrea Hirata"
hasil = cari_buku_penulis(daftar_buku, penulis_dicari)

print("=== Hasil Pencarian Buku ===")
for buku in hasil:
    print(buku.info())
