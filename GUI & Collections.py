# a. Membuat class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"


# b. Membuat list berisi 5 objek buku
daftar_buku = [
    Buku("Laskar Pelangi", "Andrea Hirata", 2005),
    Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    Buku("Sang Pemimpi", "Andrea Hirata", 2006),
    Buku("Bumi", "Tere Liye", 2014),
    Buku("Hujan", "Tere Liye", 2016)
]


# c. Fungsi mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(daftar, nama_penulis):
    hasil = []
    for buku in daftar:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# d. Menampilkan hasil pencarian
print("=== Daftar Buku ===")
for buku in daftar_buku:
    print(buku.info())

penulis_dicari = "Andrea Hirata"
print(f"\n=== Buku karya {penulis_dicari} ===")

hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
