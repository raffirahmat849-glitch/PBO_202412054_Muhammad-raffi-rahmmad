class Mahasiswa:
    # Konstruktor untuk menginisialisasi nama dan NIM
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    # Method untuk memperkenalkan diri
    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"


# Pembuatan object mahasiswa
mhs1 = Mahasiswa("Budi Santoso", "TI001")
mhs2 = Mahasiswa("Siti Aminah", "TI002")

# Menampilkan hasil perkenalan setiap mahasiswa
print(mhs1.perkenalan())
print(mhs2.perkenalan())
