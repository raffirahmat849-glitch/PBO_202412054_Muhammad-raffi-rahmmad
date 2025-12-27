class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        print(f"Hallo, nama saya {self.nama}, NIM {self.nim}, dari jurusan {self.jurusan}.")
        print(f"Saya berasal dari {Mahasiswa.universitas}\n")

    # Method update IPK
    def update_ipk(self, ipk_baru):
        # Validasi IPK (agar tidak kurang dari 0 atau lebih dari 4.0)
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}\n")
        else:
            print("Error: IPK harus berada pada rentang 0.0 - 4.0\n")

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        else:
            return "Lulus"

    # Method untuk menampilkan info lengkap mahasiswa
    def info_mahasiswa(self):
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"IPK      : {self.ipk}")
        print(f"Predikat : {self.predikat_kelulusan()}")
        print("-" * 40)
# -----------------------------
# BAGIAN DEMO PEMANGGILAN CLASS
# -----------------------------

m1 = Mahasiswa("Rapi", "2322001", "Informatika", 3.6)
m2 = Mahasiswa("Erizal", "2322002", "Sistem Informasi", 3.1)
m3 = Mahasiswa("Ewrwinur", "2322003", "Teknik Komputer", 2.4)

m1.perkenalan_diri()
m2.perkenalan_diri()
m3.perkenalan_diri()

m1.info_mahasiswa()
m2.info_mahasiswa()
m3.update_ipk(2.7)
m3.info_mahasiswa()
