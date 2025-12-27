class Dosen:
    # Konstruktor untuk menginisialisasi nama dan NIDN
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    # Method untuk mengajar mata kuliah
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Instansiasi 2 object dosen
dosen1 = Dosen("Asep Budi", "012345")
dosen2 = Dosen("Aminah", "067890")

# Memanggil method ajar_mata_kuliah
print(dosen1.ajar_mata_kuliah("Pemrograman Python"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))
